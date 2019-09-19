from translators.rules import ConsonantEndingRule, TwoConsonantLettersRule
from translators.base import BaseTranslator


class JapaneseTranslator(BaseTranslator):
    def transliterate(self, word):
        romaji = []
        word = word.translate(self.transliteration)

        for idx, letter in enumerate(word):
            next_letter_in_range_of_text = idx + 1 < len(word)
            if next_letter_in_range_of_text:
                syllable = letter
                next_letter = word[idx + 1]

                if syllable:

                    current_letter_is_consonant = letter.lower(
                    ) in self.consonants
                    next_letter_is_consonant = next_letter.lower(
                    ) in self.consonants

                    current_letter_is_vowel = letter.lower() in self.vowels
                    next_letter_is_vowel = next_letter.lower() in self.vowels

                    next_letter_is_end_of_word = next_letter.lower() == ' '

                    two_consonant_letters = current_letter_is_consonant \
                        and next_letter_is_consonant
                    consonant_ending_letters = current_letter_is_consonant \
                        and next_letter_is_end_of_word
                    vowel_ending_letters = current_letter_is_vowel \
                        and next_letter_is_end_of_word
                    next_letter_is_same = next_letter == letter
                    stripped_syllable = syllable.lower().strip()

                    if current_letter_is_vowel:
                        continue
                    if next_letter_is_vowel:
                        stripped_syllable = letter + next_letter
                    if vowel_ending_letters:
                        stripped_syllable = letter

                    if two_consonant_letters:
                        stripped_syllable = letter + 'u'
                    if consonant_ending_letters:
                        stripped_syllable = letter + 'u'
                    if next_letter_is_consonant:
                        stripped_syllable = next_letter
                    if next_letter_is_same:
                        stripped_syllable = ''

                    hiragana, katakana = self.alphabet[stripped_syllable]
                    if self.mode == 'katakana':
                        romaji.append(katakana)
                    else:
                        romaji.append(hiragana)
            else:
                # last letter in text
                if current_letter_is_consonant:
                    syllable = letter + 'u'

        return ''.join(romaji)

    def __init__(self):
        super().__init__()

        self.language_code = 'jp'
        self.mode = 'hiragana'
        self.vowels = ('a', 'u', 'i', 'o', 'e')
        self.consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                           'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                           'z')
        self.charmap = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                        "abkdefghijkrmnopqrstubwxyzABKDEFGHIJKRMNOPQRSTUBWXYZ")
        self.alphabet = {
            'a': ('あ', 'ア'),
            'i': ('い', 'イ'),
            'u': ('う', 'ウ'),
            'e': ('え', 'エ'),
            'o': ('お', 'オ'),
            'ka': ('か', 'カ'),
            'ki': ('き', 'キ'),
            'ku': ('く', 'ク'),
            'ke': ('け', 'ケ'),
            'ko': ('こ', 'コ'),
            'sa': ('さ', 'サ'),
            'si': ('し', 'シ'),
            'su': ('す', 'ス'),
            'se': ('せ', 'セ'),
            'so': ('そ', 'ソ'),
            'ta': ('た', 'タ'),
            'ti': ('ち', 'チ'),
            'tu': ('つ', 'ツ'),
            'te': ('て', 'テ'),
            'to': ('と', 'ト'),
            'na': ('な', 'ナ'),
            'ni': ('に', 'ニ'),
            'nu': ('ぬ', 'ヌ'),
            'ne': ('ね', 'ネ'),
            'no': ('の', 'ノ'),
            'ha': ('は', 'ハ'),
            'hi': ('ひ', 'ヒ'),
            'hu': ('ふ', 'フ'),
            'he': ('へ', 'ヘ'),
            'ho': ('ほ', 'ホ'),
            'ma': ('ま', 'マ'),
            'mi': ('み', 'ミ'),
            'mu': ('む', 'ム'),
            'me': ('め', 'メ'),
            'mo': ('も', 'モ'),
            'ya': ('や', 'ヤ'),
            'yu': ('ゆ', 'ユ'),
            'yo': ('よ', 'ヨ'),
            'ra': ('ら', 'ラ'),
            'ri': ('り', 'リ'),
            'ru': ('る', 'ル'),
            're': ('れ', 'レ'),
            'ro': ('ろ', 'ロ'),
            'wa': ('わ', 'ワ'),
            'wo': ('を', 'ヲ'),
            'n': ('ん', 'ン'),
            'ga': ('が', 'ガ'),
            'gi': ('ぎ', 'ギ'),
            'gu': ('ぐ', 'グ'),
            'ge': ('げ', 'ゲ'),
            'go': ('ご', 'ゴ'),
            'za': ('ざ', 'ザ'),
            'zi': ('じ', 'ジ'),
            'zu': ('ず', 'ズ'),
            'ze': ('ぜ', 'ゼ'),
            'zo': ('ぞ', 'ゾ'),
            'da': ('だ', 'ダ'),
            'di': ('ぢ', 'ヂ'),
            'du': ('づ', 'ヅ'),
            'de': ('で', 'デ'),
            'do': ('ど', 'ド'),
            'ba': ('ば', 'バ'),
            'bi': ('び', 'ビ'),
            'bu': ('ぶ', 'ブ'),
            'be': ('べ', 'ベ'),
            'bo': ('ぼ', 'ボ'),
            'pa': ('ぱ', 'パ'),
            'pi': ('ぴ', 'ピ'),
            'pu': ('ぷ', 'プ'),
            'pe': ('ぺ', 'ペ'),
            'po': ('ぽ', 'ポ'),
            'kya': ('きゃ', 'キャ'),
            'kyu': ('きゅ', 'キュ'),
            'kyo': ('きょ', 'キョ'),
            'sya': ('しゃ', 'シャ'),
            'syu': ('しゅ', 'シュ'),
            'syo': ('しょ', 'ショ'),
            'tya': ('ちゃ', 'チャ'),
            'tyu': ('ちゅ', 'チュ'),
            'tyo': ('ちょ', 'チョ'),
            'nya': ('にゃ', 'ニャ'),
            'nyu': ('にゅ', 'ニュ'),
            'nyo': ('にょ', 'ニョ'),
            'hya': ('ひゃ', 'ヒャ'),
            'hyu': ('ひゅ', 'ヒュ'),
            'hyo': ('ひょ', 'ヒョ'),
            'mya': ('みゃ', 'ミャ'),
            'myu': ('みゅ', 'ミュ'),
            'myo': ('みょ', 'ミョ'),
            'rya': ('りゃ', 'リャ'),
            'ryu': ('りゅ', 'リュ'),
            'ryo': ('りょ', 'リョ'),
            'gya': ('ぎゃ', 'ギャ'),
            'gyu': ('ぎゅ', 'ギュ'),
            'gyo': ('ぎょ', 'ギョ'),
            'zya': ('じゃ', 'ジャ'),
            'zyu': ('じゅ', 'ジュ'),
            'zyo': ('じょ', 'ジョ'),
            'dya': ('ぢゃ', 'ヂャ'),
            'dyu': ('ぢゅ', 'ヂュ'),
            'dyo': ('ぢょ', 'ヂョ'),
            'bya': ('びゃ', 'ビャ'),
            'byu': ('びゅ', 'ビュ'),
            'byo': ('びょ', 'ビョ'),
            'pya': ('ぴゃ', 'ピャ'),
            'pyu': ('ぴゅ', 'ピュ'),
            'pyo': ('ぴょ', 'ピョ'),
        }
