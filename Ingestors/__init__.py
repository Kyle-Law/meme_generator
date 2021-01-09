import os

from QuoteEngine import IngestorInterface
from Ingestors import TextIngestor, DocxIngestor, PDFIngestor, CSVIngestor
# from Ingestors import DocxIngestor
# from Ingestors import PDFIngestor
# from Ingestors import CSVIngestor


class Ingestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        filename, suffix = os.path.splitext(path)
        if suffix == '.txt':
          return TextIngestor.parse(path)
        if suffix == '.docx':
          return DocxIngestor.parse(path)
        if suffix == '.pdf':
          return PDFIngestor.parse(path)
        if suffix == '.csv':
          return CSVIngestor.parse(path)
