# 📝 Markdown Note-taking App

[Markdown Note-taking App](https://roadmap.sh/projects/markdown-note-taking-app)

A simple **Note-taking API** built with **FastAPI** that supports:

- 📥 Uploading notes (Markdown text or `.md` file)  
- 🧹 Grammar checking using [LanguageTool](https://languagetool.org/)  
- 💾 Saving notes in a database (SQLite)  
- 📜 Listing and retrieving notes  
- 🌐 Rendering Markdown into clean **HTML**  

---

## 🚀 Features

- **Grammar Check** → Send text and get grammar/spelling corrections.  
- **Save Notes** → Save Markdown text or upload `.md` files.  
- **List Notes** → Retrieve saved notes with metadata.  
- **Render Notes** → Convert Markdown into HTML for display in browsers.  
- **Interactive API Docs** → Swagger UI (`/docs`) & ReDoc (`/redoc`).  

---

## ⚙️ Tech Stack

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/)  
- **Database:** SQLite (via SQLAlchemy)  
- **Markdown Parsing:** `markdown` Python library  
- **Grammar Checking:** `language-tool-python`  

---

## 📂 Installation & Setup

### 1. Clone the repo
```bash
git clone https://github.com/Ansuman-rath/Backend_Roadmap_Project
cd markdown-notes-api
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the server

```bash
uvicorn main:app --reload
```

Server runs at: **[http://localhost:8000](http://localhost:8000)**

---

## 📑 API Endpoints

### 🔹 Meta

* `GET /` → Root (health check)

### 🔹 Grammar

* `POST /grammar-check`
  **Request JSON**:

  ```json
  {
    "text": "This are bad notes."
  }
  ```

  **Response**:

  ```json
  [
    {
      "message": "Possible agreement error — use 'is' instead of 'are'.",
      "offset": 5,
      "length": 3,
      "replacements": ["is"],
      "rule_id": "SVA"
    }
  ]
  ```

### 🔹 Notes

* `POST /notes` → Save a note (Markdown text)
* `POST /notes/upload` → Upload a `.md` file
* `GET /notes` → List all saved notes
* `GET /notes/{note_id}` → Get raw Markdown

### 🔹 Render

* `GET /notes/{note_id}/render` → Render note as **HTML**

---

## 🖥️ Testing

### Swagger UI

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

### ReDoc

Visit: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### cURL (Windows CMD Example)

```cmd
curl -X POST http://localhost:8000/grammar-check -H "Content-Type: application/json" -d "{\"text\":\"This are bad notes.\"}"
```

### cURL (Linux/macOS Example)

```bash
curl -X POST http://localhost:8000/grammar-check \
  -H "Content-Type: application/json" \
  -d '{"text":"This are bad notes."}'
```

---

## 📌 Roadmap / Future Improvements

* ✏️ Add update/delete note endpoints
* 💾 Cache rendered HTML for faster response
* 🌍 Deploy with Docker & Gunicorn
* 🔐 Authentication for personal notes
