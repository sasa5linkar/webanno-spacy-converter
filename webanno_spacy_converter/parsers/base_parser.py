from abc import ABC, abstractmethod
from typing import List
from ..models.annotation_sentence import AnnotationSentence

class BaseWebAnnoTSVParser(ABC):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.sentences: List[AnnotationSentence] = []

    @abstractmethod
    def parse(self) -> List[AnnotationSentence]:
        """Parse the TSV file and return a list of AnnotationSentence objects."""
        pass

    def load_lines(self) -> List[str]:
        """Utility to load all lines from file."""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f]