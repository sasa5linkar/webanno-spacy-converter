
**webanno-spacy-converter** is a Python module for converting between [WebAnno](https://webanno.github.io/webanno/) TSV format and [spaCy](https://spacy.io/) training data formats. It supports round-trip conversion, and entity linking.  
This tool is particularly suited for researchers and NLP practitioners working on corpus conversion and annotation pipelines.

## 📦 Features

- Convert WebAnno TSV files to spaCy training format
- Convert spaCy format back to WebAnno TSV
- Handles NER, NEL, but more formats are planned for the future
- Supports round-trip consistency
- Designed for Serbian (SR), but adaptable to other languages

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/te-sla/webanno-spacy-converter.git
cd webanno-spacy-converter
```

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install the module

You can install the module locally using:

```bash
pip install .
```

Or, for editable development:

```bash
pip install -e .
```

This installs `webanno_spacy_converter` as a Python module you can use in your own code.

---

## 🛠️ Usage

You can use the module in your own Python scripts.

### Example (Python):

#### ⚡ Quick Start Example

Here’s how to load a WebAnno TSV file, print its contents, and save it back using `webanno_spacy_converter`.

```python
from webanno_spacy_converter.parsers.tsv_parser_v3 import WebAnnoNELParser
from webanno_spacy_converter.writers.webanno_writer import WebAnnoNELWriter

def pretty_print_sentences(sentences):
    for sentence in sentences:
        print(f"Sentence: {sentence.text}")
        for entity in sentence.entities:
            start, end, entity_type, link = entity
            print(f"  Entity: {sentence.text[start:end]} (Type: {entity_type}, Link: {link})")

# Parse the input file
parser = WebAnnoNELParser("alzir.tsv")
parser.parse()

# Inspect the parsed sentences
pretty_print_sentences(parser.sentences)

# Write back to a new TSV file
writer = WebAnnoNELWriter(parser.sentences)
writer.save("output.tsv")
```

> This example assumes you are working with Named Entity Linking (NEL) annotations in WebAnno TSV format.


---

## 📂 Project Structure

```text
webanno_spacy_converter/
├── cli.py               ← Optional CLI utilities
├── config.py
├── converters/          ← spaCy ↔ WebAnno conversion logic
│   ├── spacy_to_webanno.py
│   └── webanno_to_spacy.py
├── models/              ← Data classes (tokens, sentences)
│   ├── annotation_token.py
│   └── annotation_sentence.py
├── parsers/             ← TSV parsing logic
│   ├── base_parser.py
│   └── tsv_parser_v3.py
├── utils/               ← Helpers (chunking, file I/O)
├── writers/             ← Export TSV from internal format
├── tests/               ← Unit tests
├── README.md
├── requirements.txt
├── setup.py
```

---

## 🧩 Modules

- `parsers/`: Parse WebAnno TSV into structured annotation sentences.
- `writers/`: Output annotations back to TSV format.
- `converters/`: Handle bidirectional conversion between annotation structures and spaCy `Doc` objects.
- `models/`: Internal representation of tokens and sentences.
- `utils/`: Chunking and I/O helpers.
- `cli.py`: CLI support (if used).
- `tests/`: Unit tests for parsers, converters, and utils.


## 🔍 Requirements

- Python 3.7+
- spaCy (version 3.0 or higher)


---

## 📄 License

This project is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

You are free to share and adapt the material for any purpose, even commercially, **as long as proper credit is given**.

🔗 [View full license text](https://creativecommons.org/licenses/by/4.0/)


---

## 📬 Contact

For issues, suggestions, or collaboration, please open an [Issue](https://github.com/te-sla/webanno-spacy-converter/issues) or contact the maintainer.
