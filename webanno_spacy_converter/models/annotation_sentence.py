from dataclasses import dataclass, field
from typing import List, Tuple
from .annotation_token import AnnotationToken

@dataclass
class AnnotationSentence:
    """Represents a sentence with its tokens and annotations.

    Attributes:
        text (str): The text of the sentence.
        tokens (List[AnnotationToken]): List of tokens in the sentence.
        entities (List[Tuple[int, int, str, str]]): List of entity spans in the format (start, end, type, link).
    """

    text: str
    tokens: List[AnnotationToken]
    entities: List[Tuple[int, int, str, str]] = field(default_factory=list)

    def get_token_texts(self) -> List[str]:
        """Return the text of all tokens in the sentence."""
        return [token.text for token in self.tokens]

    def get_entity_spans(self) -> List[str]:
        """Return the text of all entity spans in the sentence."""
        return [self.text[start:end] for start, end, *_ in self.entities]

    def __repr__(self) -> str:
        return (
            f"AnnotationSentence(text={self.text!r}, "
            f"tokens={len(self.tokens)} tokens, "
            f"entities={len(self.entities)} entities)"
        )