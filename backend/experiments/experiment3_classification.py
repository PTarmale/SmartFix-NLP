from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# Training data
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


# Categories
categories = [
    "NETWORK",
    "NETWORK",
    "NETWORK",
    "NETWORK",

    "PLUMBING",
    "PLUMBING",
    "PLUMBING",
    "PLUMBING",

    "ELECTRICITY",
    "ELECTRICITY",
    "ELECTRICITY",
    "ELECTRICITY",

    "APPLIANCE",
    "APPLIANCE",
    "APPLIANCE",
    "APPLIANCE",

    "SOFTWARE",
    "SOFTWARE",
    "SOFTWARE",
    "SOFTWARE"
]


# Convert text into TF-IDF vectors
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(training_complaints)


# Train classification model
model = LogisticRegression(max_iter=1000)

model.fit(X, categories)


def classify_complaint(complaint):

    complaint_vector = vectorizer.transform([complaint])

    prediction = model.predict(complaint_vector)

    return prediction[0]


if __name__ == "__main__":

    print("\n========== SMART FIX - EXPERIMENT 3 ==========")

    complaint = input("\nEnter your complaint: ")

    category = classify_complaint(complaint)

    print("\nYour Complaint:")
    print(complaint)

    print("\nPredicted Category:")
    print(category)