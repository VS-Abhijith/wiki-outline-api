from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/outline")
def get_outline(country: str):
    try:
        url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
        response = requests.get(url)

        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Wikipedia page not found.")

        soup = BeautifulSoup(response.text, "html.parser")
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

        markdown = "## Contents\n\n"
        for tag in headings:
            level = int(tag.name[1])
            title = tag.text.strip()
            markdown += f"{'#' * level} {title}\n\n"

        return {"country": country, "markdown_outline": markdown.strip()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    return {"message": "Welcome to the Wikipedia Outline API. Use /api/outline?country=CountryName"}
