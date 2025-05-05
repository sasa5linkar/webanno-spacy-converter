from ..converters.webanno_to_spacy import AnnotationSentencesToDocBinConverter
from ..parsers.tsv_parser_v3 import WebAnnoNELParser
import os
import spacy

nlp = spacy.load("my_nlp_el_cnn1")
converter = AnnotationSentencesToDocBinConverter(nlp)
#get all .spacy files in the root directory

spacy_files = [f for f in os.listdir(".") if f.endswith(".spacy")]
reader = WebAnnoNELParser("output.tsv")

senteces = reader.parse()

docbin = converter.convert(senteces)
docbin.to_disk("example.spacy")







