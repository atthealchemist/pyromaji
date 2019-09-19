from .base import BaseTranslator


class EnglishTranslator(BaseTranslator):
    def transliterate(self, word):
        romaji = []

        # source_text = source_text.lower()

        for idx, letter in enumerate(word):
            syllable = letter
            next_letter_in_range_of_text = idx + 1 < len(word)
            if next_letter_in_range_of_text:
                next_letter = word[idx + 1]

                two_consonant_letters = letter in self.consonants and next_letter in self.consonants
                consonant_ending_letters = letter in self.consonants or letter in self.special and next_letter == ' '
                next_letter_is_vowel = next_letter in self.vowels

                if two_consonant_letters or consonant_ending_letters:
                    syllable = letter + 'u'
                if next_letter_is_vowel:
                    syllable = letter
            else:
                # last letter in text
                if letter in self.consonants:
                    syllable = letter + 'u'

            for char, replacement in self.additional:
                if letter == char:
                    syllable = replacement

            romaji.append(syllable)

        translated = ''.join(romaji)

        translated = translated.replace('l', 'r')

        return translated

    def __init__(self):
        super().__init__()

        self.language_code = 'en'
        self.vowels = ('a', 'u', 'i', 'o', 'e')
        self.consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                           'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                           'z')
        self.charmap = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                        "abcdefghijkrmnopqrstubwxyzABCDEFGHIJKRMNOPQRSTUBWXYZ")
