from ..converters.webanno_to_spacy import AnnotationSentencesToDocBinConverter
from ..parsers.tsv_parser_v3 import WebAnnoNELParser
import os
import spacy

nlp = spacy.load("my_nlp_el_cnn1")
converter = AnnotationSentencesToDocBinConverter(nlp)

reader = WebAnnoNELParser("output.tsv")

senteces = reader.parse()

docbin = converter.convert(senteces)
docbin.to_disk("example.spacy")







