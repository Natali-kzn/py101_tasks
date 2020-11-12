
"""
Программа считает Топ-100 слов для переданного ей текстого файла.
Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk
Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""

# считываем файл, записываем в text, переводим в нижний регистр
f = open('text.txt', "r", encoding="utf-8")
text = f.read()
text = text.lower()
f.close

# в модуле string содержится стандартный набор символов пунктуации
import string
text = text.replace('\n', ' ')
spec_chars = string.punctuation + '\xa0«»\t—…'

# разделим text на символы, оставим только символы, не входящие в spec_chars, снова объединим в строку, также уберем цифры
def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars])

text = remove_chars_from_text(text, spec_chars)
text = remove_chars_from_text(text, string.digits)

# разбиваем текст на токены (слова)
from nltk import word_tokenize
text_tokens = word_tokenize(text)

import nltk
text = nltk.Text(text_tokens)

# удалим стоп-слова
from nltk.corpus import stopwords
russian_stopwords = stopwords.words("russian")
english_stopwords = stopwords.words("english")

def delete_stop_words(text):
    text_without_stop_words = []
    for word in text:
        if word not in russian_stopwords or english_stopwords:
           text_without_stop_words.append(word)
    return text_without_stop_words

# считаем частоту слов в тексте
from nltk.probability import FreqDist
fdist = FreqDist(text_without_stop_words)
fdist = fdist.most_common(100)
print(fdist)
