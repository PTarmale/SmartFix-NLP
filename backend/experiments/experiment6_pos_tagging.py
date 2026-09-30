import nltk
from nltk import word_tokenize, pos_tag

print("SMART FIX - EXPERIMENT 6")
print("-------------------------")

text = input("Enter a sentence: ")

words = word_tokenize(text)
tags = pos_tag(words)

print("\nPOS Tags:")

for word, tag in tags:
    print(word, "->", tag)