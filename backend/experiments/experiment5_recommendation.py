from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob


# -------------------------------------------------
# TRAINING DATA
# -------------------------------------------------

training_complaints = [
    "internet is not working",
    "wifi connection is slow",
    "router is not connecting",
    "no internet connection",

    "water pipe is leaking",
    "tap is leaking",
    "water is coming from the pipe",
    "bathroom pipe is broken",

    "electricity is not available",
    "power is gone",
    "there is a power cut",
    "electricity connection is not working",

    "refrigerator is not cooling",
    "washing machine is not working",
    "air conditioner is not cooling",
    "fridge has stopped working",

    "laptop software is not working",
    "application is crashing",
    "software has an error",
    "program is not opening"
]


categories = [
    "NETWORK", "NETWORK", "NETWORK", "NETWORK",
    "PLUMBING", "PLUMBING", "PLUMBING", "PLUMBING",
    "ELECTRICITY", "ELECTRICITY", "ELECTRICITY", "ELECTRICITY",
    "APPLIANCE", "APPLIANCE", "APPLIANCE", "APPLIANCE",
    "SOFTWARE", "SOFTWARE", "SOFTWARE", "SOFTWARE"
]


# -------------------------------------------------
# CATEGORY CLASSIFICATION MODEL
# -------------------------------------------------

classifier_vectorizer = TfidfVectorizer()

X = classifier_vectorizer.fit_transform(training_complaints)

classifier = LogisticRegression(max_iter=1000)

classifier.fit(X, categories)


# -------------------------------------------------
# SIMILARITY DATA
# -------------------------------------------------

stored_complaints = [
    "internet connection is not working",
    "wifi is very slow",
    "water pipe is leaking",
    "laptop battery is not charging",
    "electricity power is not available",
    "mobile phone screen is damaged"
]


similarity_vectorizer = TfidfVectorizer()

similarity_matrix = similarity_vectorizer.fit_transform(
    stored_complaints
)


# -------------------------------------------------
# SOLUTIONS
# -------------------------------------------------

solutions = {

    "NETWORK": [
        "Restart your router.",
        "Check the network cables.",
        "Reconnect your WiFi.",
        "Try connecting another device.",
        "Contact your internet provider if the problem continues."
    ],

    "PLUMBING": [
        "Check the leaking pipe or tap.",
        "Turn off the water supply if necessary.",
        "Check the pipe connections.",
        "Contact a plumber if the leakage continues."
    ],

    "ELECTRICITY": [
        "Check whether the main power switch is on.",
        "Check the circuit breaker.",
        "Check whether nearby electrical devices have power.",
        "Contact an electrician if the problem continues."
    ],

    "APPLIANCE": [
        "Check whether the appliance is receiving power.",
        "Restart the appliance.",
        "Check the user manual for error messages.",
        "Contact an authorized service technician if the problem continues."
    ],

    "SOFTWARE": [
        "Restart the application.",
        "Restart your computer.",
        "Check for available software updates.",
        "Check the error message.",
        "Reinstall the application if necessary."
    ],

    "OTHER": [
        "Please provide more details about the problem.",
        "Try restarting the affected device.",
        "Contact the appropriate service provider."
    ]
}


# -------------------------------------------------
# CLASSIFICATION FUNCTION
# -------------------------------------------------

def classify_complaint(complaint):

    complaint_vector = classifier_vectorizer.transform(
        [complaint]
    )

    prediction = classifier.predict(
        complaint_vector
    )

    return prediction[0]


# -------------------------------------------------
# SIMILARITY FUNCTION
# -------------------------------------------------

def find_similar_problem(complaint):

    complaint_vector = similarity_vectorizer.transform(
        [complaint]
    )

    scores = cosine_similarity(
        complaint_vector,
        similarity_matrix
    )[0]

    best_index = scores.argmax()

    return (
        stored_complaints[best_index],
        scores[best_index]
    )


# -------------------------------------------------
# SENTIMENT FUNCTION
# -------------------------------------------------

def analyze_sentiment(complaint):

    polarity = TextBlob(complaint).sentiment.polarity

    if polarity > 0:
        sentiment = "POSITIVE"

    elif polarity < 0:
        sentiment = "NEGATIVE"

    else:
        sentiment = "NEUTRAL"

    return sentiment, polarity


# -------------------------------------------------
# SMART FIX FUNCTION
# -------------------------------------------------

def smart_fix(complaint):

    category = classify_complaint(complaint)

    similar_problem, similarity_score = find_similar_problem(
        complaint
    )

    sentiment, polarity = analyze_sentiment(
        complaint
    )

    recommended_solutions = solutions.get(
        category,
        solutions["OTHER"]
    )

    return {
        "category": category,
        "similar_problem": similar_problem,
        "similarity_score": similarity_score,
        "sentiment": sentiment,
        "polarity": polarity,
        "solutions": recommended_solutions
    }


# -------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------

if __name__ == "__main__":

    print("\n========== SMART FIX - EXPERIMENT 5 ==========")

    complaint = input("\nEnter your complaint: ")

    result = smart_fix(complaint)

    print("\n---------------------------------------------")
    print("SMART FIX RESULT")
    print("---------------------------------------------")

    print("\nComplaint:")
    print(complaint)

    print("\nCategory:")
    print(result["category"])

    print("\nMost Similar Problem:")
    print(result["similar_problem"])

    print("\nSimilarity Score:")
    print(round(result["similarity_score"], 3))

    print("\nSentiment:")
    print(result["sentiment"])

    print("\nPolarity:")
    print(round(result["polarity"], 3))

    print("\nRecommended Solutions:")

    for number, solution in enumerate(
        result["solutions"],
        start=1
    ):
        print(f"{number}. {solution}")