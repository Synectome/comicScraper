import datetime


class Comic:
    def __init__(self, title=""):
        self.title = title
        self.publisher : str = ""
        self.writer : str = ""
        self.artist : str = ""
        self.publication_date : datetime.date = ""
        self.completed : bool = ""

    def set_title(self, title):
        self.title = title

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_writer(self, writer):
        self.writer = writer

    def set_artist(self, artist):
        self.artist = artist

    def set_publication_date(self, publication_date):
        self.publication_date = publication_date

    def set_completed(self, completed):
        self.completed = completed

