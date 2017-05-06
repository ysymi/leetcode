#! coding=utf8
# ideas:
# hash简单应用
# gains:
#
import random
import string


class Codec:
    def __init__(self):
        self.long2short = {}
        self.short2long = {}
        self.seq = string.letters + string.digits

    def generate_uniq_short(self, width=6):
        """Generate a uniq short url

        :type width: int
        :rtype: str
        """

        result = ''
        for _ in range(width):
            result += random.choice(self.seq)

        if result not in self.short2long:
            return result
        else:
            return self.generate_uniq_short(width)

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        short = self.generate_uniq_short()
        self.short2long.update({short: longUrl})
        self.long2short.update({longUrl: short})
        return short

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.short2long.get(shortUrl)
