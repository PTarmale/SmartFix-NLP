import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

print("SMART FIX - EXPERIMENT 7")
print("-------------------------")

text = input("Enter a sentence: ")

words = word_tokenize(text)
tags = pos_tag(words)

grammar = "NP: {<DT>?<JJ>*<NN.*>+}"

chunker = RegexpParser(grammar)
tree = chunker.parse(tags)

print("\nChunks:")

for subtree in tree.subtrees():
    if subtree.label() == "NP":
        print(" ".join(word for word, tag in subtree.leaves()))