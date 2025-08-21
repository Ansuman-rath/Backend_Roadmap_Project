from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, Session

import markdown
import language_tool_python

# ---------- DB setup ----------
SQLALCHEMY_DATABASE_URL = "sqlite:///./notes.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content_md = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------- Schemas ----------
class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    text: str = Field(..., min_length=1)

class NoteOut(BaseModel):
    id: int
    title: str
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True  # SQLAlchemy -> Pydantic

class GrammarIssue(BaseModel):
    message: str
    offset: int
    length: int
    replacements: List[str] = []
    rule_id: Optional[str] = None

class GrammarCheckIn(BaseModel):
    text: str

# ---------- Grammar tool (offline if possible; fallback to public API) ----------
def init_tool():
    try:
        # Offline server (needs Java installed)
        return language_tool_python.LanguageTool("en-US")
    except Exception:
        # Fallback (rate-limited public API)
        return language_tool_python.LanguageToolPublicAPI("en-US")

LT = init_tool()

def check_grammar(text: str) -> List[GrammarIssue]:
    matches = LT.check(text or "")
    issues = []
    for m in matches:
        issues.append(
            GrammarIssue(
                message=m.message,
                offset=m.offset,
                length=m.errorLength,
                replacements=m.replacements[:5],
                rule_id=m.ruleId,
            )
        )
    return issues

# ---------- Markdown renderer ----------
def md_to_html(md_text: str) -> str:
    # Useful extensions for tables, fenced code blocks, etc.
    return markdown.markdown(md_text, extensions=["extra", "codehilite", "toc"])

# ---------- FastAPI app ----------
app = FastAPI(title="Markdown Notes API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@app.get("/", tags=["meta"])
def root():
    return {"ok": True, "message": "See /docs for interactive API"}

# --- 1) Grammar check ---
@app.post("/grammar-check", response_model=List[GrammarIssue], tags=["grammar"])
def grammar_check(payload: GrammarCheckIn):
    return check_grammar(payload.text)

# --- 2) Save note (JSON) ---
@app.post("/notes", response_model=NoteOut, tags=["notes"])
def create_note(payload: NoteCreate, db: Session = Depends(get_db)):
    note = Note(title=payload.title.strip(), content_md=payload.text)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

# --- 2b) Save note (file upload) ---
@app.post("/notes/upload", response_model=NoteOut, tags=["notes"])
async def upload_note(
    file: UploadFile = File(..., description="Upload a .md file"),
    title: Optional[str] = Form(None),
    db: Session = Depends(get_db),
):
    if not file.filename.lower().endswith((".md", ".markdown", ".txt")):
        raise HTTPException(status_code=400, detail="Please upload a markdown (.md) file")
    content = (await file.read()).decode("utf-8", errors="replace")
    note = Note(title=title or file.filename, content_md=content)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

# --- 3) List notes ---
@app.get("/notes", response_model=List[NoteOut], tags=["notes"])
def list_notes(db: Session = Depends(get_db)):
    return db.query(Note).order_by(Note.created_at.desc()).all()

# (optional) Get raw markdown of a note
@app.get("/notes/{note_id}", response_model=NoteCreate, tags=["notes"])
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return NoteCreate(title=note.title, text=note.content_md)

# --- 4) Render HTML ---
@app.get("/notes/{note_id}/render", response_class=HTMLResponse, tags=["render"])
def render_note(note_id: int, db: Session = Depends(get_db)):
    note = db.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    html = md_to_html(note.content_md)
    # Return HTML directly so a browser can display it
    return HTMLResponse(content=html)
