import nltk
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize

def character_tokenization(text):
    return list(text)

def subword_tokenization(text):
    return wordpunct_tokenize(text)

text = "Hello, World!"

char_tokens = character_tokenization(text)
print("Character Tokenization:", char_tokens)

subword_tokens = subword_tokenization(text)
print("Subword Tokenization:", subword_tokens)
