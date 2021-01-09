from typing import List
import pandas

from QuoteEngine import QuoteModel
from QuoteEngine import IngestorInterface


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest extension')
        quotes = []
        df = pandas.read_csv(path,header=0)

        for index, row in df.iterrows():
            print(row)
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
