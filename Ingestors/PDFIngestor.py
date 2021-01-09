from typing import List

import os
import subprocess
from .TextIngestor import TextIngestor
from QuoteEngine import QuoteModel
from QuoteEngine import IngestorInterface

class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest extension')

        rendered_pdf = './rendered_pdf.txt'
        command = f"pdftotext {path} {rendered_pdf}"

        subprocess.call(command, shell=True, stderr=subprocess.STDOUT)

        quotes = TextIngestor.parse(rendered_pdf)

        os.remove(rendered_pdf)
        return quotes
