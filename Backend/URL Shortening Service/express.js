import express from "express";
import mongoose from "mongoose";
import shortid from "shortid";

const app = express();
app.use(express.json());

// MongoDB Schema
const urlSchema = new mongoose.Schema({
  url: { type: String, required: true },
  shortCode: { type: String, unique: true },
  accessCount: { type: Number, default: 0 },
}, { timestamps: true });

const Url = mongoose.model("Url", urlSchema);

app.get("/", (req, res) => {
    res.send("🚀 URL Shortener API is running!");
  });
  

// 1. Create Short URL
app.post("/shorten", async (req, res) => {
  const { url } = req.body;
  if (!url) return res.status(400).json({ error: "URL is required" });

  const shortCode = shortid.generate();
  const newUrl = new Url({ url, shortCode });
  await newUrl.save();

  res.status(201).json(newUrl);
});

// 2. Retrieve Original URL (Redirect)
app.get("/:shortCode", async (req, res) => {
    const { shortCode } = req.params;
    const record = await Url.findOne({ shortCode });
  
    if (!record) return res.status(404).send("Not found");
  
    record.accessCount++;
    await record.save();
  
    // Redirect to original URL
    res.redirect(record.url);
  });
  

// 3. Update Short URL
app.put("/shorten/:shortCode", async (req, res) => {
  const { shortCode } = req.params;
  const { url } = req.body;

  const record = await Url.findOneAndUpdate(
    { shortCode },
    { url, updatedAt: new Date() },
    { new: true }
  );

  if (!record) return res.status(404).json({ error: "Not found" });
  res.status(200).json(record);
});

// 4. Delete Short URL
app.delete("/shorten/:shortCode", async (req, res) => {
  const { shortCode } = req.params;
  const deleted = await Url.findOneAndDelete({ shortCode });
  if (!deleted) return res.status(404).json({ error: "Not found" });

  res.sendStatus(204);
});

// 5. Get URL Statistics
app.get("/shorten/:shortCode/stats", async (req, res) => {
  const { shortCode } = req.params;
  const record = await Url.findOne({ shortCode });
  if (!record) return res.status(404).json({ error: "Not found" });

  res.status(200).json(record);
});

// Start Server
mongoose.connect("mongodb://localhost:27017/urlshortener")
  .then(() => {
    app.listen(3000, () => console.log("🚀 Server running on http://localhost:3000"));
  })
  .catch(err => console.error(err));
