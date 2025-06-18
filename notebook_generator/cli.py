import argparse
from pathlib import Path
from .generator import NotebookGenerator


def generate_notebook(files, output):
    ng = NotebookGenerator()
    notebook_parts = []
    for file_path in files:
        text = Path(file_path).read_text(encoding="utf-8")
        topic = Path(file_path).stem
        chapter = ng.add_chapter(topic, text)
        notebook_parts.append(chapter)
    notebook = '\n'.join(notebook_parts)
    Path(output).write_text(notebook, encoding="utf-8")
    print(f"Notebook written to {output}")


def main():
    parser = argparse.ArgumentParser(description="Generate structured notebook from text files")
    parser.add_argument('files', nargs='+', help='Input text files, each representing a chapter')
    parser.add_argument('-o', '--output', default='notebook.md', help='Output markdown file')
    args = parser.parse_args()
    generate_notebook(args.files, args.output)


if __name__ == '__main__':
    main()
