from ..converters.spacy_to_webanno import DocBinToAnnotationSentencesConverter
from ..writers.webanno_writer import WebAnnoNELWriter
import spacy

nlp = spacy.load("my_nlp_el_cnn1")
converter = DocBinToAnnotationSentencesConverter(nlp)
senteces = converter.convert("srGeoGeography.spacy")

writer = WebAnnoNELWriter(senteces)
writer.save("output1.tsv")




