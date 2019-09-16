class Rule:
    def check(self):
        pass

    def __init__(self, text):
        self.text = text
        self.vowels = ('a', 'u', 'i', 'o', 'e')
        self.consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                           'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                           'z')


class TwoConsonantLettersRule(Rule):
    '''
    Rule definition:

    Two consonant letters should divide by 'u'.

    Example:

    hello -> heruro
    '''
    def check(self):
        romaji = []

        for idx, letter in self.text:
            syllable = letter
            next_letter_in_bounds_of_text = idx + 1 < len(
                self.text) and idx >= 0
            if next_letter_in_bounds_of_text:
                next_letter = self.text[idx + 1]

                two_consonant_letters = letter in self.consonants \
                    and next_letter in self.consonants
                if two_consonant_letters:
                    syllable = letter + 'u'

                romaji.append(syllable)

        return ''.join(romaji)


class ConsonantEndingRule(Rule):
    '''
    Rule definition:

    If word ending with consonant, 'u' should be added to end.
    '''
    def check(self):
        romaji = []

        for idx, letter in self.text:
            syllable = letter
            next_letter_in_bounds_of_text = idx + 1 < len(
                self.text) and idx >= 0
            if next_letter_in_bounds_of_text:
                next_letter = self.text[idx + 1]

                consonant_ending_letters = letter in self.consonants \
                    or letter in self.special and next_letter == ' '

                if consonant_ending_letters:
                    syllable = letter + 'u'

                romaji.append(syllable)

        return ''.join(romaji)

    def __init__(self, text):
        self.text = text
