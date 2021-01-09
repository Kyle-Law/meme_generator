from QuoteEngine import QuoteModel
from QuoteEngine import IngestorInterface

class TextIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
       if not cls.can_ingest(path):
            raise Exception('cannot ingest extension')
        file = open(path, "r", encoding="utf-8-sig")
        lines = file.readlines()
        file.close()
        quotes = []
        for quote in lines:
            parsed = quote.rstrip("\n").split(" - ")
            body = parsed[0]
            author = parsed[1]
            new_quote = QuoteModel(body,author)
            quotes.append(new_quote)

        return quotes
