from dataclasses import dataclass, field
from typing import List
from webanno_spacy_converter.models.annotation_sentence import AnnotationSentence

@dataclass
class MultiWordExpression:
    """
    Represents a multi-word expression (MWE) that may be non-contiguous.

    Attributes:
        lemma (str): Canonical (lemmatized) form of the expression.
        token_count (int): Number of tokens in the expression.
        token_indices (List[int]): List of token indices within the sentence.
    """
    lemma: str
    token_count: int
    token_indices: List[int]


@dataclass
class AnnotatedSentenceWithMWEs(AnnotationSentence):
    """
    Extends AnnotationSentence to include multi-word expressions (MWEs).

    Attributes:
        mwes (List[MultiWordExpression]): List of multi-word expressions.
    """
    mwes: List[MultiWordExpression] = field(default_factory=list)

    def get_expression_spans(self) -> List[str]:
        """
        Return the actual token strings of each MWE.

        Returns:
            List[str]: One string per expression, built from the token list.
        """
        return [" ".join(self.tokens[i].text for i in mwe.token_indices) for mwe in self.mwes]