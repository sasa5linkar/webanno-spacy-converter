from ..converters.webanno_to_spacy import AnnotationSentencesToDocBinConverterV2
from ..parsers.tsv_parser_v3 import WebAnnoNELParser
import spacy

def main():
    nlp = spacy.load("my_nlp_el_cnn1")
    converter = AnnotationSentencesToDocBinConverterV2(nlp)
    reader = WebAnnoNELParser("test_data/output.tsv")
    sentences = reader.parse()
    docbin = converter.convert(sentences)
    docbin.to_disk("test_data/examplev2.spacy")

if __name__ == "__main__":
    main()







