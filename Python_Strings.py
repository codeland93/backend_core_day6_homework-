# Product Review Analysis

# List of reviews
python_reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "This was a poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

# Keywords to highlight
keywords = ["good", "excellent", "bad", "poor", "average"]

# Function to highlight keywords
def highlight_keywords(reviews, keywords):
    highlighted_reviews = []
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        highlighted_reviews.append(review)
    return highlighted_reviews

# Highlight the keywords in the reviews
highlighted_reviews = highlight_keywords(python_reviews, keywords)

# Print the highlighted reviews
for review in highlighted_reviews:
    print(review)

# Sentiment Tally

# List of reviews
python_reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "This was a poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

# Predefined lists of positive and negative words
python_positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
python_negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Function to tally positive and negative words
def tally_sentiments(reviews, positive_words, negative_words):
    sentiment_counts = []
    for review in reviews:
        pos_count = 0
        neg_count = 0
        # Split the review into words
        words = review.lower().split()
        # Tally positive words
        for word in positive_words:
            pos_count += words.count(word)
        # Tally negative words
        for word in negative_words:
            neg_count += words.count(word)
        # Append the counts to the list
        sentiment_counts.append((pos_count, neg_count))
    return sentiment_counts

# Get the sentiment tallies for each review
sentiment_tallies = tally_sentiments(python_reviews, python_positive_words, python_negative_words)

# Print the sentiment tallies
for i, (pos, neg) in enumerate(sentiment_tallies):
    print(f"Review {i+1}: {pos} positive words, {neg} negative words")

# Review Summary

# List of reviews
python_reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "This was a poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

# Function to create a review summary
def review_summary(reviews, summary_length=30):
    summaries = []
    for review in reviews:
        if len(review) <= summary_length:
            summaries.append(review)
        else:
            # Ensure we don't cut off in the middle of a word
            end_index = summary_length
            if review[summary_length] != ' ' and ' ' in review[:summary_length]:
                end_index = review.rfind(' ', 0, summary_length)
            summaries.append(review[:end_index] + "...")
    return summaries

# Generate summaries for each review
review_summaries = review_summary(python_reviews)

# Print the summaries
for i, summary in enumerate(review_summaries):
    print(f"Review {i+1} Summary: {summary}")
