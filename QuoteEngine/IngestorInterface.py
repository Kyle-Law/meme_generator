from typing import List
from .QuoteModel import QuoteModel
from abc import ABC, abstractmethod

def IngestorInterface(ABC):
  """
  A Ingestor Interface class.
  """
  allowed_extensions = ['txt','csv','pdf','docx']

  @classmethod
  def can_ingest(cls, path: str) -> bool:
    ext = path.split('.')[-1]
    return ext in cls.allowed_extensions

  @classmethod
  @abstractmethod
  def parse(cls, path: str) -> List(QuoteModel):
    pass
