from dataclasses import dataclass, field
from typing import List, Dict, Tuple
from .annotation_token import AnnotationToken

@dataclass
class AnnotationSentence:
    """Represents a sentence with its tokens and annotations.

    attributes:
        sentence_index (int): 1-based index of the sentence in the document.
        text (str): The text of the sentence.
        tokens (List[AnnotationToken]): List of tokens in the sentence.
        entities (List[Tuple[int, int, str, str]]): List of entity spans in the format (start, end, type, link).
    """

    text: str
    tokens: List[AnnotationToken]
    entities: List[Tuple[int, int, str, str]] = field(default_factory=list)

    def get_token_texts(self) -> List[str]:
        """Get the text of all tokens in the sentence.

        Returns:
            List[str]: List of token texts.
        """

        return [token.text for token in self.tokens]

    def get_entity_spans(self) -> List[str]:
        """Get the text of all entity spans in the sentence.

        Returns:
            List[str]: List of entity texts.
        """

        return [self.text[start:end] for start, end, _ in self.entities]

    def __repr__(self):
        return (
            f"AnnotationSentence(text={self.text!r}, \n"
            f"tokens={len(self.tokens)} tokens, \n"
            f"entities={len(self.entities)} entities, \n"

        )