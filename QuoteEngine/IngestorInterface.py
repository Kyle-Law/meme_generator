from typing import List

def IngestorInterface(self, parameter_list):
  """
  A Ingestor Interface class.
  """
  @classmethod
  def can_ingest(cls,path):
    return path.split('.')[-1] in ['txt','csv','pdf','docx']

  @classmethod
  def parse(cls,path:str) -> List:
    pass
