import csv

class TransliterationEngine:

    def __init__(self, translator):
        self.translator = translator

    def _get_replacements(self):
        replacements = []
        with open('assets/syllables_{lang}.csv'.format(lang=self.translator.language_code), encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            for idx, row in enumerate(reader):
                if idx < 1:
                    continue
                replacements.append(row)
        
        return tuple(replacements)

    def from_romaji(self, source_text):
        pass

    def to_romaji(self, source_text):
        '''
        При конвертации в ромадзи происходит несколько этапов:
        1. Мы меняем слоги на "заменители"
        2. Мы меняем согласные на "слоги", добавляя к ним гласную букву (u)
        3. Мы транслитерируем всё остальное.
        '''

        romaji = self.translator.transliterate(source_text)
        translated = romaji.translate(self.translator.transliteration)
        return translated.replace("\'", "")