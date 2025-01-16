"""
This module serves the home page with the README.md content and provides a download link 
for the API collection (`E-Commerce API Collection.json`).
"""

import os
from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse, FileResponse
from markdown_it import MarkdownIt

router = APIRouter(tags=["Home"])
DOCS_FILENAME = "E-Commerce Files.zip"

def html_page(content: str) -> str:
    return f"""
    <html>
        <head>
            <title>README.md</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0; background-color: #121212; color: #e0e0e0; margin: 40px; }}
                h1, h2, h3 {{ color: #ffffff; }}
                p {{ margin: 1em 0; }}
                code {{ background-color: #1e1e1e; color: #d4d4d4; padding: 0.2em 0.4em; border-radius: 4px; box-shadow: 0 0 5px rgba(0, 0, 0, 0.5); }}
                pre code {{ background-color: #1e1e1e; color: #d4d4d4; padding: 10px; border-radius: 4px; font-size: 1em; overflow-x: auto; }}
                table {{ width: 100%; border-collapse: collapse; margin: 20px 0; background-color: #1e1e1e; }}
                table, th, td {{ border: 1px solid #333; }}
                th, td {{ padding: 8px; text-align: left; color: #e0e0e0;}}
                th {{ background-color: #2d2d2d; }}
                a {{ color: #ffeb3b; text-decoration: none; }}
                a:hover {{ text-decoration: underline; }}
                .download-btn {{ display: inline-block; margin-top: 20px; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; border-radius: 4px; text-align: center; }}
                .download-btn:hover {{ background-color: #45a049; }}
            </style>
        </head>
        <body>
            {content}
            <a href="/download" class="download-btn" download>Download API Collection</a>
        </body>
    </html>
    """

@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def read_homepage() -> HTMLResponse:
    "Converts the markdown content from `README.md` and display it on the front page"
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            readme_content = f.read()
        markdown = MarkdownIt().enable("table")
        html_content = markdown.render(readme_content)
        return HTMLResponse(content=html_page(html_content),
                            status_code=status.HTTP_200_OK)
    except FileNotFoundError:
        return HTMLResponse(content="File 'README.md' not found",
                            status_code=status.HTTP_404_NOT_FOUND)

@router.get("/download", include_in_schema=False)
async def download_file():
    file_path = os.path.join("files", DOCS_FILENAME)
    try:
        return FileResponse(path=file_path,
                            filename=DOCS_FILENAME,
                            status_code=status.HTTP_200_OK)
    except FileNotFoundError:
        return HTMLResponse(content=f"File '{DOCS_FILENAME}' not found",
                            status_code=status.HTTP_404_NOT_FOUND)
