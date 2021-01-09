
import pandas as pd

from QuoteEngine import QuoteModel
from QuoteEngine import IngestorInterface


class CSVIngestor(IngestorInterface):
  @classmethod
  def parse(cls, path):
    csv = pd.read_csv(path)
    return [QuoteModel(**row) for index, row in csv.iterrows()]
