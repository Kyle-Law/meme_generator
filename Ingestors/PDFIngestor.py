import os
import subprocess
from Ingestors import TextIngestor
from QuoteEngine import IngestorInterface

class PDFIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        text_file = './test.txt'
        cmd = f"./pdftotext -layout -nopgbrk {path} {text_file}"
        subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        quotes = TextIngestor.parse(text_file)
        os.remove(text_file)
        return quotes
