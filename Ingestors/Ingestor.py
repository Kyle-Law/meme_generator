from typing import List

from QuoteEngine import QuoteModel
from QuoteEngine import IngestorInterface
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor

class Ingestor(IngestorInterface):
    ingestors = [DocxIngestor, CSVIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
