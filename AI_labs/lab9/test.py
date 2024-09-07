from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')

text = "Hello, world! How's everything going? All good here"
sentences = sent_tokenize(text)
print(sentences)

from nltk.tokenize import word_tokenize
text = "Hello, world! How's everything going? I can't wait for the weekend"
tokens = word_tokenize(text)
print(tokens)


