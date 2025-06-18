from pathlib import Path
import subprocess


class Exporter:
    """Export markdown notebooks to different formats using pandoc if available."""

    def __init__(self, source: str):
        self.source = Path(source)

    def to_docx(self, output: str):
        if not self.source.exists():
            raise FileNotFoundError(self.source)
        try:
            subprocess.run([
                'pandoc', str(self.source), '-o', output
            ], check=True)
            print(f"Exported DOCX to {output}")
        except FileNotFoundError:
            print("Pandoc not found. Please install pandoc to enable DOCX export")

    def to_pdf(self, output: str):
        if not self.source.exists():
            raise FileNotFoundError(self.source)
        try:
            subprocess.run([
                'pandoc', str(self.source), '-o', output
            ], check=True)
            print(f"Exported PDF to {output}")
        except FileNotFoundError:
            print("Pandoc not found. Please install pandoc to enable PDF export")
