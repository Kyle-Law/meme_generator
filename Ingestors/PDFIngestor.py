import os
import subprocess
from .TextIngestor import TextIngestor
from QuoteEngine import IngestorInterface

class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
       if not cls.can_ingest(path):
          raise Exception('cannot ingest extension')

        text_file = './test.txt'
        command = f"./pdftotext -layout -nopgbrk {path} {text_file}"

        subprocess.call(command, shell=True, stderr=subprocess.STDOUT)

        quotes = TextIngestor.parse(text_file)

        os.remove(text_file)
        return quotes
