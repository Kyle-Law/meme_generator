from typing import List
from docx import Document

from QuoteEngine import QuoteModel
from QuoteEngine import IngestorInterface

class DocxIngestor(IngestorInterface):
    print(IngestorInterface)
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
          raise Exception('cannot ingest extension')
        document = Document(path)
        quotes = []
        for para in document.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                quote = QuoteModel(parse[0],parse[1])
                quotes.append(quote)
        return quotes
