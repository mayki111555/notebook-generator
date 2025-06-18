class NotebookGenerator:
    """Simple notebook generator for medical students."""

    GLOSSARY = {
        "Neuron": "נוירון",
        "Synapse": "סינפסה",
        "DNA": "דנ\"א",
        "RNA": "רנ\"א",
        "Mitochondria": "מיטוכונדריה",
    }

    def __init__(self):
        self.chapter_count = 0

    def _bold_terms(self, text: str) -> str:
        for term, hebrew in self.GLOSSARY.items():
            text = text.replace(term, f"**{term}** ({hebrew})")
        return text

    def _split_paragraphs(self, text: str) -> list:
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        paragraphs = []
        current = []
        for line in lines:
            if line.endswith((':', '-')):
                if current:
                    paragraphs.append(' '.join(current))
                    current = []
                paragraphs.append(line)
            else:
                current.append(line)
        if current:
            paragraphs.append(' '.join(current))
        return paragraphs

    def _format_section(self, heading: str, body: list) -> str:
        formatted = [f"### {heading}"]
        for paragraph in body:
            bolded = self._bold_terms(paragraph)
            formatted.append(bolded)
        return '\n'.join(formatted)

    def add_chapter(self, topic: str, raw_text: str) -> str:
        self.chapter_count += 1
        chapter_title = f"פרק {self.chapter_count}: {topic}"
        sections = []
        paragraphs = self._split_paragraphs(raw_text)
        if paragraphs:
            intro_lines = [self._bold_terms(p) for p in paragraphs[:2]]
            sections.append('\n'.join(intro_lines))
            paragraphs = paragraphs[2:]
        current_heading = None
        current_body = []
        for para in paragraphs:
            if para.endswith((':', '-')):
                if current_heading:
                    sections.append(self._format_section(current_heading, current_body))
                    current_body = []
                current_heading = para.rstrip(':-')
            else:
                current_body.append(para)
        if current_heading:
            sections.append(self._format_section(current_heading, current_body))
        return f"# {chapter_title}\n\n" + '\n\n'.join(sections) + '\n'
