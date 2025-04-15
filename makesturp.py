# Update setup.py and pyproject.toml to include multiple authors

updated_setup_py = """\
from setuptools import setup, find_packages

setup(
    name='webanno-spacy-converter',
    version='0.1.0',
    description='Convert between WebAnno TSV and spaCy training formats',
    author='Sasha Petalinkar, Milica Ikonic Nesic',
            author_email='your@email.com, collaborator@email.com',
    url='https://github.com/yourusername/webanno-spacy-converter',
    packages=find_packages(),
    install_requires=[
        'spacy>=3.0.0',
    ],
    python_requires='>=3.8',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
"""

updated_pyproject_toml = """\
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "webanno-spacy-converter"
version = "0.1.0"
description = "Convert between WebAnno TSV and spaCy training formats"
authors = [
    { name="Your Name", email="your@email.com" },
    { name="Collaborator Name", email="collaborator@email.com" }
]
dependencies = [
    "spacy>=3.0.0"
]
requires-python = ">=3.8"
"""

# Overwrite the files with the updated metadata
with open("webanno_spacy_converter/setup.py", "w", encoding="utf-8") as f:
    f.write(updated_setup_py)

with open("webanno_spacy_converter/pyproject.toml", "w", encoding="utf-8") as f:
    f.write(updated_pyproject_toml)

"Authors updated in setup.py and pyproject.toml."
