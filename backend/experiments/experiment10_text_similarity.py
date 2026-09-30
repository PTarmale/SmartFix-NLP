from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("SMART FIX - EXPERIMENT 10")
print("-------------------------")

text1 = input("Enter first complaint: ")
text2 = input("Enter second complaint: ")

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform([text1, text2])

similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

print("\nSimilarity Score:", round(similarity * 100, 2), "%")