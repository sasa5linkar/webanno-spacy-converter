# WebAnno ⇄ spaCy Converter

This library provides utilities to convert between WebAnno TSV format and spaCy's training formats.

## Structure

```text
webanno_spacy_converter//__init__.py
webanno_spacy_converter//cli.py
webanno_spacy_converter//config.py
webanno_spacy_converter//README.md
webanno_spacy_converter//requirements.txt
webanno_spacy_converter//setup.py
webanno_spacy_converter/converters/__init__.py
webanno_spacy_converter/converters/spacy_to_webanno.py
webanno_spacy_converter/converters/webanno_to_spacy.py
webanno_spacy_converter/parsers/__init__.py
webanno_spacy_converter/parsers/base_parser.py
webanno_spacy_converter/parsers/tsv_parser_v3.py
webanno_spacy_converter/writers/__init__.py
webanno_spacy_converter/writers/webanno_writer.py
webanno_spacy_converter/models/__init__.py
webanno_spacy_converter/models/annotation_token.py
webanno_spacy_converter/models/annotation_sentence.py
webanno_spacy_converter/utils/__init__.py
webanno_spacy_converter/utils/chunking.py
webanno_spacy_converter/utils/file_io.py
webanno_spacy_converter/tests/__init__.py
webanno_spacy_converter/tests/test_parsers.py
webanno_spacy_converter/tests/test_converters.py
webanno_spacy_converter/tests/test_chunking.py
```

## Modules
- `parsers/`: Parses WebAnno TSV files into internal structures.
- `writers/`: Writes structured data back into TSV format.
- `converters/`: Converts between spaCy Docs and annotation models.
- `models/`: Contains data classes like AnnotationToken and AnnotationSentence.
- `utils/`: Helper functions like sentence chunking.
- `cli.py`: Command-line interface.
- `tests/`: Unit tests for all components.
