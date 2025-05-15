from ..converters.webanno_to_spacy import AnnotationSentencesToDocBinConverter
from ..parsers.tsv_parser_v3 import WebAnnoNELParser
import spacy

def main():
    nlp = spacy.load("my_nlp_el_cnn1")
    converter = AnnotationSentencesToDocBinConverter(nlp)
    reader = WebAnnoNELParser("output.tsv")
    sentences = reader.parse()
    docbin = converter.convert(sentences)
    docbin.to_disk("example.spacy")

if __name__ == "__main__":
    main()







