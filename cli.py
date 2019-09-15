from engine import TransliterationEngine
from translators import TRANSLATORS

import argparse

parser = argparse.ArgumentParser(
    description='Language to romaji convertion')


class PyRomaji:

    def _init_argparser(self):
        parser.add_argument('-l', '--lang', action='store',
                            default='en', help='language code')
        parser.add_argument('-f', '--file', action='store',
                            help='path to text file to convert')
        parser.add_argument('-i', '--input', action='store_true',
                            help='input mode')

    def main(self):
        args = parser.parse_args()

        lang = args.lang
        file_path = args.file
        input_text = args.input

        translator = TRANSLATORS[lang]

        engine = TransliterationEngine(translator=translator())
        print("PyRomaji CLI v 0.1 - using \"{}\" translator".format(engine.translator.language_code))

        text = ''

        if file_path:
            try:
                with open(file_path, 'r+', encoding="utf-8") as text_file:
                    text = text_file.read()
            except FileNotFoundError as ex:
                print('The required file @ {} was not found!'.format(file_path))
        if input_text:
            print("\nInput mode\n")
            text = input("Enter text in your native language: ")

        if text:
            converted = engine.to_romaji(text)
            print("\nResult: \n\n{}".format(converted))
        else:
            print("Bye!")
            exit(0)

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description='Language to romaji convertion')
        self._init_argparser()
        self.main()


if __name__ == '__main__':
    PyRomaji()
