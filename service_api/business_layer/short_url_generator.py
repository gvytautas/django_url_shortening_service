from string import ascii_lowercase, ascii_uppercase, digits
import secrets


class ShortUrlGenerator:
    def __init__(self, length: int):
        self.length = length
        self.characters = ascii_uppercase + ascii_lowercase + digits

    def generate_short_url(self):
        short_url = ''.join(secrets.choice(self.characters) for _i in range(self.length))
        return short_url
