from typing import List
from spacy.tokens import DocBin, Doc, Span
from webanno_spacy_converter.models.annotation_sentence import AnnotationSentence

class AnnotationSentencesToDocBinConverter:
    """
    Converts a list of AnnotationSentence objects into a spaCy DocBin.

    Attributes:
        nlp: The spaCy language pipeline.
        sentences_per_doc (int): Number of sentences to combine into a single Doc.
    """

    def __init__(self, nlp, sentences_per_doc: int = 10):
        self.nlp = nlp
        self.sentences_per_doc = sentences_per_doc

    def convert(self, sentences: List[AnnotationSentence]) -> DocBin:
        """
        Convert AnnotationSentences into a DocBin.

        Args:
            sentences (List[AnnotationSentence]): List of annotated sentences.

        Returns:
            DocBin: The resulting DocBin object.
        """
        doc_bin = DocBin(store_user_data=True)
        batch: List[Doc] = []

        for sent in sentences:
            doc = self._convert_sentence_to_doc(sent)
            batch.append(doc)
            if len(batch) == self.sentences_per_doc:
                combined = Doc.from_docs(batch)
                doc_bin.add(combined)
                batch = []

        if batch:
            combined = Doc.from_docs(batch)
            doc_bin.add(combined)

        return doc_bin

    def _convert_sentence_to_doc(self, sent: AnnotationSentence) -> Doc:
        """
        Convert a single AnnotationSentence to a spaCy Doc.

        Args:
            sent (AnnotationSentence): The annotated sentence.

        Returns:
            Doc: The spaCy Doc with entities and kb_ids set.
        """
        doc = self.nlp(sent.text)
        if doc:
            doc[0].is_sent_start = True

        spans: List[Span] = []
        for start, end, label, qid in sent.entities:
            span = doc.char_span(start, end, label=label)
            if span:
                span.kb_id_ = qid if qid != "*" else "NIL"
                spans.append(span)
        doc.ents = spans
        return doc

class AnnotationSentencesToDocBinConverterV2(AnnotationSentencesToDocBinConverter):
    """
    Converts a list of AnnotationSentence objects into a spaCy DocBin.

    This version is made for compatibility with spaCy v3.0 and later.

    Especially useful for transformer-based pipelines.
    """

    def __init__(
        self, nlp, sentences_per_doc: int = 10,
        tag_layer: str = None, lemma_layer: str = None,
        ner: bool = False, nel: bool = False,
    ):
        """
        Initialize the converter.
        Args:
            sentences_per_doc (int): Number of sentences to combine into a single Doc.
            nlp: The spaCy language pipeline.
            tag_layer (str): Layer name for tag annotations.
            lemma_layer (str): Layer name for lemma annotations.
            ner (bool): Whether to include NER (named entity recognition) annotations.
            nel (bool): Whether to include NEL (named entity linking) annotations.

        """
        super().__init__(nlp, sentences_per_doc)
        self.tag_layer = tag_layer
        self.lemma_layer = lemma_layer
        self.ner = ner
        self.nel = nel



    def _convert_sentence_to_doc(self, sent):
        """
        Convert a single AnnotationSentence to a spaCy Doc.

        Args:
            sent (AnnotationSentence): The annotated sentence.

        Returns:
            Doc: The spaCy Doc with entities and kb_ids set.
        """
        words = sent.get_token_texts()
        # spaces are detrnied by comparing the end postion of the token with the start position of the next token
        # if it same it is not a space, otherwise it is a space. Last token is always not a space
        tokens = sent.tokens
        spaces = [False] * (len(tokens) - 1) + [True]
        for i in range(len(tokens) - 1):
            if tokens[i].end == tokens[i + 1].start:
                spaces[i] = True
        if self.tag_layer:
            tags = [token.layers.get(self.tag_layer, "_") for token in tokens]
        else:
            tags = ["_"] * len(tokens)
        if self.lemma_layer:
            lemmas = [token.layers.get(self.lemma_layer, "_") for token in tokens]
        else:
            lemmas = ["_"] * len(tokens)

        doc = Doc(self.nlp.vocab, words=words, spaces=spaces, tags=tags, lemmas=lemmas)
        if doc:
            doc[0].is_sent_start = True
        if self.ner:
            spans: List[Span] = []
            for start, end, label, qid in sent.entities:
                span = doc.char_span(start, end, label=label)
                if span is not None:
                    if self.nel:
                        span.kb_id_ = qid if qid != "*" else "NIL"
                    spans.append(span)
            doc.ents = spans


                


