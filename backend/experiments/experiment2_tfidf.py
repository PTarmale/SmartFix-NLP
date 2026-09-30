from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Previously stored complaints
complaints = [
    "internet connection is not working",
    "wifi is very slow",
    "water pipe is leaking",
    "laptop battery is not charging",
    "electricity power is not available",
    "mobile phone screen is damaged"
]


def find_similar_complaint(user_complaint):

    # Add user's complaint to the existing complaints
    all_complaints = complaints + [user_complaint]

    # Convert text into TF-IDF vectors
    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(all_complaints)

    # Compare user's complaint with stored complaints
    similarity_scores = cosine_similarity(
        tfidf_matrix[-1],
        tfidf_matrix[:-1]
    )[0]

    # Find the highest similarity
    best_match_index = similarity_scores.argmax()

    best_match = complaints[best_match_index]
    best_score = similarity_scores[best_match_index]

    return best_match, best_score


if __name__ == "__main__":

    print("\n========== SMART FIX - EXPERIMENT 2 ==========")

    user_complaint = input("\nEnter your complaint: ")

    best_match, score = find_similar_complaint(user_complaint)

    print("\nYour Complaint:")
    print(user_complaint)

    print("\nMost Similar Existing Problem:")
    print(best_match)

    print("\nSimilarity Score:")
    print(round(score, 3))