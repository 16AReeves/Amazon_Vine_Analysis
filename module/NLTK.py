import nltk
from nltk import word_tokenize
text = word_tokenize("I enjoy swimming in pools")
output = nltk.pos_tag(text)
print(output)