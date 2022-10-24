import string
from random import choices

from flask import url_for


class GenerateTinytUrl:
    """
    Class used to generate short version of the original URL
    """

    def __init__(self, original_url):
        self.original_url = original_url
        self.tiny_url = self.create_tiny_url()

    def create_tiny_url(self):
        """
        Generate unique key to identify tiny URL
        """
        characters = string.digits + string.ascii_letters
        tiny_url = "".join(choices(characters, k=5))

        return url_for("index", _external=True, tiny_url=tiny_url)
