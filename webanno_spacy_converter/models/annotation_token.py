from dataclasses import dataclass, field
from typing import Dict

@dataclass
class AnnotationToken:
    """Represents a token in a sentence with its annotations.

    Attributes:
        sentence_index (int): 1-based index of the sentence in the document.
        token_index (int): 1-based index of the token within the sentence.
        text (str): The text of the token.
        start (int): Start character index of the token in the sentence.
        end (int): End character index of the token in the sentence.
        layers (Dict[str, str]): Dictionary to hold annotation layers and their values.
    """

    sentence_index: int    # 1-based index from WebAnno
    token_index: int       # 1-based index within sentence
    text: str
    start: int
    end: int
    layers: Dict[str, str] = field(default_factory=dict)

    def get_layer(self, name: str) -> str | None:
        """Get the value of a specific annotation layer.

        Args:
            name (str): The name of the annotation layer.

        Returns:
            str | None: The value of the annotation layer, or None if it doesn't exist.
        """
        return self.layers.get(name)

    def add_layer(self, name: str, value: str):
        """Add or update an annotation layer.

        Args:
            name (str): The name of the annotation layer.
            value (str): The value of the annotation layer.
        """
        self.layers[name] = value

    def has_annotation(self, name: str) -> bool:
        """Check if the token has a specific annotation layer.
        Args:


            name (str): The name of the annotation layer.

        Returns:
            bool: True if the annotation layer exists, False otherwise.
        """

        return name in self.layers