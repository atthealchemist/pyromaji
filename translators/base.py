class BaseTranslator:

    def __init__(self):
        self.language_code = 'base'
        self.vowels = []
        self.consonants = []
        self.charmap = []
        self.transliteration = {ord(c): ord(d) for c, d in zip(*self.charmap)}