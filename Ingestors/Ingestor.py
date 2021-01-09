from typing import List

from QuoteEngine import QuoteModel
from QuoteEngine import IngestorInterface
from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter

class Ingestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for importer in importers:
            if importer.can_ingest(path):
                return importer.parse(path)
