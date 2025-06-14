
---

````markdown
# 🌍 Wiki Outline API

A simple FastAPI-based web API that generates a **Markdown outline** of a country’s Wikipedia page by extracting all headings (`<h1>` to `<h6>`). Perfect for educational summaries, content structure extraction, or creating quick overviews.

---

## 📌 Features

- 📖 Fetches real-time Wikipedia content for any country
- 🧠 Parses all heading elements (H1 to H6)
- 📝 Returns a clean Markdown-formatted outline
- 🌐 CORS enabled for GET requests from any frontend
- 🚀 Deployed on Vercel for instant access

---

## 🔗 Live API

Try the API:

```url
https://wiki-outline-api.vercel.app/api/outline?country=India
````

Replace `India` with any other country name like `Japan`, `Germany`, or `United States`.

Response example:

```json
{
  "markdown": "## Contents\n\n# India\n\n## Etymology\n\n## History\n\n### Ancient India\n..."
}
```

---

## ⚙️ How It Works

1. Accepts a `GET` request at:

   ```
   /api/outline?country=CountryName
   ```

2. Internally:

   * Finds the country’s Wikipedia page
   * Extracts all headings (H1 to H6) using BeautifulSoup
   * Converts them into Markdown with `#` prefixes
   * Returns a structured Markdown outline as JSON

---

## 📁 Project Structure

```
wiki-outline-api/
├── api/
│   └── index.py         # Main FastAPI app
├── requirements.txt     # Python dependencies
└── vercel.json          # Vercel deployment config
```

---

## 🧪 Local Testing

```bash
git clone https://github.com/VS-Abhijith/wiki-outline-api.git
cd wiki-outline-api
pip install -r requirements.txt
uvicorn api.index:app --reload
```

Test locally by visiting:
👉 `http://127.0.0.1:8000/api/outline?country=India`

---

## 🚀 Deploying on Vercel

1. Push your code to GitHub.
2. Go to [https://vercel.com](https://vercel.com) and import the GitHub repo.
3. Use Python as the project language.
4. Set the root directory and ensure `vercel.json` exists.
5. Your API will be live at:

```
https://your-project-name.vercel.app/api/outline?country=India
```

---

## 👨‍💻 Author

**Abhijith VS**
📘 [LinkedIn](https://www.linkedin.com/in/vsabhijith)
💻 [GitHub](https://github.com/VS-Abhijith)

---