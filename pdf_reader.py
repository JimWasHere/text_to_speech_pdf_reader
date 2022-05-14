from PyPDF2 import PdfFileReader
from text_to_speech import speak


class PdfReader:
    """Reads pdf files out loud to the user"""
    reader = None

    def __init__(self, filepath):
        self.file = filepath
        self.reader = PdfFileReader(self.file, strict=False)
        self.number_of_pages = 0

    def extract(self, page_num):
        """Returns entire text string from a particular page of the pdf file and removes most special characters"""
        page = self.reader.pages[page_num]
        text = " ".join([x for x in page.extractText().split(" ") if "" not in x])
        return text

    def page_numbers(self):
        """Returns a list of all of the page numbers in a pdf file from 0 to total numbers"""
        num_pages = []
        self.number_of_pages = self.reader.numPages
        for _ in range(1, self.number_of_pages):
            num_pages.append(_)
        return num_pages

    def read_out_loud(self, page):
        """Reads the entire contents of pdf file"""
        page = page - 1
        speak(self.extract(page), "en", save=False, speak=True)