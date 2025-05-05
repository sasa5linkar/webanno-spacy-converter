from typing import List
from spacy.tokens import DocBin, Doc, Span
from webanno_spacy_converter.models.annotation_sentence import AnnotationSentence

class AnnotationSentencesToDocBinConverter:
    """
    Converts a list of AnnotationSentence objects into a spaCy DocBin.

    Attributes:
        nlp: The spaCy language pipeline.
        sentences_per_doc: Number of sentences to combine into a single Doc.
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
        batch = []

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
        doc[0].is_sent_start = True

        spans = []
        for start, end, label, qid in sent.entities:
            span = doc.char_span(start, end, label=label)
            if span:
                span.kb_id_ = qid if qid != "*" else "NIL"
                spans.append(span)
        doc.ents = spans

        return doc
