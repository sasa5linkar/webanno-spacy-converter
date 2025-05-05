from setuptools import setup, find_packages

setup(
    name="webanno_spacy_converter",
    version="0.1.1",
    description="Tools to convert between WebAnno TSV and spaCy formats",
    author="SasaP",
    packages=find_packages(),
    install_requires=[
        "spacy>=3.5",
        "cyrtranslit"
    ],
    python_requires=">=3.7"
)
