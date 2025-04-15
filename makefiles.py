import os

# Define base folder and structure
base_dir = "webanno_spacy_converter"
structure = {
    "": ["__init__.py", "cli.py", "config.py", "README.md", "requirements.txt", "setup.py"],
    "converters": ["__init__.py", "spacy_to_webanno.py", "webanno_to_spacy.py"],
    "parsers": ["__init__.py", "base_parser.py", "tsv_parser_v3.py"],
    "writers": ["__init__.py", "webanno_writer.py"],
    "models": ["__init__.py", "annotation_token.py", "annotation_sentence.py"],
    "utils": ["__init__.py", "chunking.py", "file_io.py"],
    "tests": ["__init__.py", "test_parsers.py", "test_converters.py", "test_chunking.py"]
}

# Create directory structure and empty files
for folder, files in structure.items():
    dir_path = os.path.join(base_dir, folder)
    os.makedirs(dir_path, exist_ok=True)
    for file in files:
        file_path = os.path.join(dir_path, file)
        with open(file_path, "w", encoding="utf-8") as f:
            if file == "README.md":
                f.write("# WebAnno ⇄ spaCy Converter\n\n")
                f.write("This library provides utilities to convert between WebAnno TSV format and spaCy's training formats.\n\n")
                f.write("## Structure\n\n")
                f.write("```text\n")
                for folder_inner, files_inner in structure.items():
                    prefix = os.path.join(base_dir, folder_inner).replace("\\", "/")
                    for f_inner in files_inner:
                        f.write(f"{prefix}/{f_inner}\n")
                f.write("```\n\n")
                f.write("## Modules\n")
                f.write("- `parsers/`: Parses WebAnno TSV files into internal structures.\n")
                f.write("- `writers/`: Writes structured data back into TSV format.\n")
                f.write("- `converters/`: Converts between spaCy Docs and annotation models.\n")
                f.write("- `models/`: Contains data classes like AnnotationToken and AnnotationSentence.\n")
                f.write("- `utils/`: Helper functions like sentence chunking.\n")
                f.write("- `cli.py`: Command-line interface.\n")
                f.write("- `tests/`: Unit tests for all components.\n")

# Return path so user can download if needed
base_dir
