from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime

app = FastAPI(title="SmartFix NLP")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


# =========================
# COMPLAINT DATA
# =========================

complaints = {
    "Machine Problem": [
        "machine not working",
        "motor stopped",
        "motor broken",
        "machine stopped",
        "conveyor not running",
        "equipment not working",
        "machine failure",
        "motor failure"
    ],

    "Quality Problem": [
        "product defective",
        "product defect",
        "poor product quality",
        "product damaged",
        "product scratches",
        "items defective",
        "quality issue",
        "defective item"
    ],

    "Production Delay": [
        "production delayed",
        "production late",
        "work taking too long",
        "production stopped",
        "shipment delayed",
        "delivery late",
        "production slow",
        "production line late"
    ],

    "Material Problem": [
        "material missing",
        "raw material unavailable",
        "not enough material",
        "material shortage",
        "raw material missing",
        "material unavailable"
    ]
}


solutions = {

    "Machine Problem":
        "Check the machine power supply, motor, wiring and control panel. Schedule maintenance if required.",

    "Quality Problem":
        "Inspect the defective product, check the production process and perform quality control.",

    "Production Delay":
        "Check the production schedule, identify the reason for the delay and update the responsible team.",

    "Material Problem":
        "Check the inventory, identify the material shortage and arrange the required raw materials."
}


departments = {

    "Machine Problem": "Maintenance",

    "Quality Problem": "Quality Control",

    "Production Delay": "Production",

    "Material Problem": "Stores / Materials",

    "General Complaint": "Customer Support"
}


stop_words = {
    "the",
    "is",
    "are",
    "a",
    "an",
    "my",
    "with",
    "and",
    "has",
    "have",
    "problem",
    "issue",
    "there",
    "this",
    "that",
    "not",
    "very"
}


# =========================
# PRIORITY
# =========================

def detect_priority(text):

    high_words = {
        "urgent",
        "critical",
        "emergency",
        "danger",
        "safety",
        "completely",
        "stopped",
        "immediately"
    }

    medium_words = {
        "delay",
        "late",
        "damaged",
        "missing",
        "shortage",
        "defective"
    }

    words = set(text.lower().split())

    if words.intersection(high_words):
        return "HIGH"

    if words.intersection(medium_words):
        return "MEDIUM"

    return "LOW"


# =========================
# SENTIMENT
# =========================

def detect_sentiment(text):

    positive_words = {
        "good",
        "great",
        "excellent",
        "happy",
        "satisfied",
        "helpful",
        "working"
    }

    negative_words = {
        "bad",
        "poor",
        "broken",
        "failed",
        "failure",
        "damaged",
        "defective",
        "delay",
        "late",
        "stopped",
        "missing",
        "shortage",
        "angry",
        "not"
    }

    words = set(text.lower().split())

    positive = len(words.intersection(positive_words))
    negative = len(words.intersection(negative_words))

    if negative > positive:
        return "Negative"

    if positive > negative:
        return "Positive"

    return "Neutral"


# =========================
# COMPLAINT ANALYSIS
# =========================

def analyze_complaint(text):

    text = text.lower()

    for character in ",.!?;:":
        text = text.replace(character, " ")

    words = set(text.split())

    scores = {}

    for category, examples in complaints.items():

        score = 0

        for example in examples:

            example_words = set(example.split())

            useful_words = example_words - stop_words

            matches = useful_words.intersection(words)

            score += len(matches)

        scores[category] = score

    best_category = max(scores, key=scores.get)

    if scores[best_category] == 0:

        return (
            "General Complaint",
            "Review the complaint and assign it to the appropriate department.",
            50
        )

    confidence = min(95, 60 + scores[best_category] * 10)

    return (
        best_category,
        solutions[best_category],
        confidence
    )


# =========================
# HOME
# =========================

@app.get("/")
def home():

    return {
        "message": "SmartFix NLP Backend is Running"
    }


# =========================
# SMARTFIX ANALYZER
# =========================

@app.post("/api/analyze")
def analyze(data: dict):

    text = data.get("text", "").strip()

    if not text:

        return {
            "message": "Please enter a complaint."
        }

    category, solution, confidence = analyze_complaint(text)

    priority = detect_priority(text)

    sentiment = detect_sentiment(text)

    department = departments.get(
        category,
        "Customer Support"
    )

    ticket_id = "SF-" + datetime.now().strftime("%Y%m%d%H%M%S")

    return {

        "ticket_id": ticket_id,

        "complaint": text,

        "category": category,

        "department": department,

        "priority": priority,

        "sentiment": sentiment,

        "confidence": confidence,

        "solution": solution
    }


# =========================
# WORD SENSE DISAMBIGUATION
# =========================

@app.post("/api/wsd")
def wsd(data: dict):

    text = data.get("text", "").lower()

    if (
        "river" in text
        or "water" in text
        or "fisherman" in text
    ):

        meaning = "River Bank"

    else:

        meaning = "Financial Bank"

    return {
        "meaning": meaning
    }


# =========================
# TEXT SIMILARITY
# =========================

similar_complaints = [

    "machine is not working",
    "motor stopped working",
    "conveyor is not running",
    "product is defective",
    "product has scratches",
    "poor product quality",
    "production is delayed",
    "production line is running late",
    "delivery is late",
    "raw material is missing",
    "not enough raw material",
    "material shortage"

]


@app.post("/api/similarity")
def text_similarity(data: dict):

    text = data.get("text", "").strip()

    if not text:

        return {
            "message": "Please enter some text."
        }

    documents = similar_complaints + [text]

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(documents)

    input_vector = vectors[-1]

    existing_vectors = vectors[:-1]

    similarities = cosine_similarity(
        input_vector,
        existing_vectors
    )[0]

    best_index = similarities.argmax()

    score = similarities[best_index] * 100

    return {

        "input": text,

        "similar_complaint":
            similar_complaints[best_index],

        "similarity":
            round(float(score), 2)
    }