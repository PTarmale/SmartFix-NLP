import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

print("SMART FIX - EXPERIMENT 8")
print("-------------------------")

text = input("Enter news text: ")

words = word_tokenize(text)
tags = pos_tag(words)

tree = ne_chunk(tags)

print("\nNamed Entities:")

for item in tree:
    if hasattr(item, "label"):
        entity = " ".join(word for word, tag in item.leaves())
        print(entity, "->", item.label())