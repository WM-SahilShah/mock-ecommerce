from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from markdown_it import MarkdownIt

router = APIRouter(tags=["home"])

@router.get("/", response_class=HTMLResponse)
async def read_homepage() -> HTMLResponse:
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            readme_content = f.read()
        markdown = MarkdownIt().enable("table")
        html_content = markdown.render(readme_content)
        css_styles = """
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 0;
                background-color: #121212;
                color: #e0e0e0;
                margin: 40px;
            }
            h1, h2, h3 {
                color: #ffffff;
            }
            p {
                margin: 1em 0;
            }
            code {
                background-color: #1e1e1e;
                color: #d4d4d4;
                padding: 0.2em 0.4em;
                border-radius: 4px;
                box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
            }
            pre code {
                background-color: #1e1e1e;
                color: #d4d4d4;
                padding: 10px;
                border-radius: 4px;
                font-size: 1em;
                overflow-x: auto;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                background-color: #1e1e1e;
            }
            table, th, td {
                border: 1px solid #333;
            }
            th, td {
                padding: 8px;
                text-align: left;
                color: #e0e0e0;
            }
            th {
                background-color: #2d2d2d;
            }
            a {
                color: #ffeb3b;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
        """
        full_html_content = f"""
        <html>
            <head>
                <title>README.md</title>
                {css_styles}
            </head>
            <body>
                {html_content}
            </body>
        </html>
        """
        return HTMLResponse(content=full_html_content, status_code=200)
    except FileNotFoundError:
        return HTMLResponse(content="README file not found", status_code=404)
