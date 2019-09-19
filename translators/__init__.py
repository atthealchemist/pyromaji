
from .english import EnglishTranslator
from .russian import RussianTranslator
from .japanese import JapaneseTranslator

TRANSLATORS = {
    'en': EnglishTranslator,
    'ru': RussianTranslator,
    'jp': JapaneseTranslator
}
