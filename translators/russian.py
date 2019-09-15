from .base import BaseTranslator


class RussianTranslator(BaseTranslator):

    def transliterate(self, source_text):
        romaji = []

        source_text = source_text.lower()

        for idx, letter in enumerate(source_text):
            syllable = letter
            next_letter_in_range_of_text = idx + 1 < len(source_text)
            if next_letter_in_range_of_text:
                next_letter = source_text[idx + 1]

                two_consonant_letters = letter in self.consonants and next_letter in self.consonants
                consonant_ending_letters = letter in self.consonants or letter in self.special and next_letter == ' '
                next_letter_is_vowel = next_letter in self.vowels

                if two_consonant_letters or consonant_ending_letters:
                    syllable = letter + 'у'
                if next_letter_is_vowel:
                    syllable = letter
            else:
                # last letter in text
                if letter in self.consonants:
                    syllable = letter + 'у'

            for char, replacement in self.additional:
                if letter == char:
                    syllable = replacement

            romaji.append(syllable)

        return ''.join(romaji)

    def __init__(self):

        self.language_code = 'ru'
        self.additional = (
            ('ё', 'yo'),
            ('ц', 'tsu'),
            ('ч', 'chu'),
            ('ш', 'shi'),
            ('щ', 'shi'),
            ('ю', 'yu'),
            ('я', 'ya'),
            ('й', 'ji'),
            ('ъе', 'ye'),
            ('цы', 'tsi'),
        )
        self.vowels = ('а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')
        self.consonants = ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л',
                           'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ')
        self.special = ('ъ', 'ь')
        self.charmap = ("абвгдежзиклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЪЭЮЯ",
                        "abbgdejzikrmnoprstufhцчшщ'i'euaABBGDEJZIKRMNOPRSTUFHЦЧШЦ'I'EUA")
        self.transliteration = {ord(c): ord(d) for c, d in zip(*self.charmap)}
