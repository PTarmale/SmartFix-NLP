import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# Download required NLTK data if needed
try:
    stop_words = set(stopwords.words("english"))
except LookupError:
    nltk.download("stopwords")
    stop_words = set(stopwords.words("english"))

try:
    word_tokenize("test")
except LookupError:
    nltk.download("punkt")


def preprocess_text(text: str):
    """
    Clean and preprocess a complaint.
    """

    # 1. Convert to lowercase
    text = text.lower()

    # 2. Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # 3. Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # 4. Tokenize
    tokens = word_tokenize(text)

    # 5. Remove stopwords
    filtered_tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    # 6. Join tokens
    cleaned_text = " ".join(filtered_tokens)

    return {
        "original_text": text,
        "tokens": tokens,
        "filtered_tokens": filtered_tokens,
        "cleaned_text": cleaned_text
    }


if __name__ == "__main__":

    complaint = input("Enter your complaint: ")

    result = preprocess_text(complaint)

    print("\n========== SMART FIX - EXPERIMENT 1 ==========")

    print("\nOriginal Text:")
    print(result["original_text"])

    print("\nTokens:")
    print(result["tokens"])

    print("\nAfter Stopword Removal:")
    print(result["filtered_tokens"])

    print("\nFinal Cleaned Text:")
    print(result["cleaned_text"])