import csv


class TransliterationEngine:
    def __init__(self, translator):
        self.translator = translator

    def to_romaji(self, text):
        '''
        При конвертации в ромадзи происходит несколько этапов:
        1. Мы меняем слоги на "заменители"
        2. Мы меняем согласные на "слоги", добавляя к ним гласную букву (u)
        3. Мы транслитерируем всё остальное.
        '''
        result = []
        SPACE_CHAR = ' '

        if SPACE_CHAR in text:

            words = text.split(SPACE_CHAR)
            for word in words:
                romaji = self.translator.transliterate(word)
                translated = romaji.translate(self.translator.transliteration)
                result.append(translated)

            translated = SPACE_CHAR.join(result).lstrip()
        else:
            romaji = self.translator.transliterate(text)
            translated = romaji.translate(self.translator.transliteration)

        return translated.replace("\'", "")
