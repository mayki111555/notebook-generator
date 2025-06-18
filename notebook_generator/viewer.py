from http.server import SimpleHTTPRequestHandler, HTTPServer
from pathlib import Path

try:
    import markdown
except ImportError:  # pragma: no cover
    markdown = None


class NotebookViewer:
    """Serve a markdown notebook as HTML for interactive reading."""

    def __init__(self, markdown_file: str, port: int = 8000):
        self.markdown_file = Path(markdown_file)
        self.port = port

    def serve(self):
        if not self.markdown_file.exists():
            raise FileNotFoundError(self.markdown_file)
        if markdown is None:
            raise ImportError("markdown package is required for viewing")
        html = markdown.markdown(self.markdown_file.read_text(encoding="utf-8"))
        html_page = f"<html><body>{html}</body></html>"
        temp_html = self.markdown_file.with_suffix('.html')
        temp_html.write_text(html_page, encoding="utf-8")
        handler = SimpleHTTPRequestHandler
        httpd = HTTPServer(('localhost', self.port), handler)
        print(f"Serving on http://localhost:{self.port}")
        httpd.serve_forever()
