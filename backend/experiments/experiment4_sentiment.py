from textblob import TextBlob


def analyze_sentiment(text):

    blob = TextBlob(text)

    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "POSITIVE"
    elif polarity < 0:
        sentiment = "NEGATIVE"
    else:
        sentiment = "NEUTRAL"

    return sentiment, polarity


if __name__ == "__main__":

    print("\n========== SMART FIX - EXPERIMENT 4 ==========")

    complaint = input("\nEnter your complaint: ")

    sentiment, polarity = analyze_sentiment(complaint)

    print("\nYour Complaint:")
    print(complaint)

    print("\nSentiment:")
    print(sentiment)

    print("\nPolarity Score:")
    print(round(polarity, 3))