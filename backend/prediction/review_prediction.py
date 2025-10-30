import pandas as pd
import dill
import numpy as np
import os
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from preprocessing.preprocessing import TextCleaner, TextTokenizerStopwordsRemover, Lemmatization
nltk.download('punkt_tab')

# ===================== Load Models =====================

# Get the current directory (this will be "prediction")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go one level up to reach the project root ("Sentiment_analysis_streamlit")
PROJECT_DIR = os.path.dirname(BASE_DIR)

# Now point to the "models" folder inside the project root
MODEL_DIR = os.path.join(PROJECT_DIR, 'models')

# Load TF-IDF Vectorizer
with open(os.path.join(MODEL_DIR, 'tfidf_vectorizer.pkl'), 'rb') as f:
    tfidf = dill.load(f)

# Load Scaler
with open(os.path.join(MODEL_DIR, 'scaler.pkl'), 'rb') as f:
    scaler = dill.load(f)

# Load PCA
with open(os.path.join(MODEL_DIR, 'pca.pkl'), 'rb') as f:
    pca = dill.load(f)

# Load Final Logistic Model
with open(os.path.join(MODEL_DIR, 'lgb_model.pkl'), 'rb') as f:
    model = dill.load(f)


analyzer = SentimentIntensityAnalyzer()

# ===================== Prediction Function =====================
def predict_sentiment(test_text):
    print(f"Input Text: [{test_text}]\n")

    # Step 1: Clean text
    cleaner = TextCleaner()
    cleaned_text = cleaner.clean(test_text)

    # Step 2: Tokenize & remove stopwords
    tokenizer_remover = TextTokenizerStopwordsRemover()
    tokens = tokenizer_remover.tokenize_and_remove_stopwords(cleaned_text)

    # Step 3: Lemmatize tokens
    lemmatizer = Lemmatization()
    lemmatized_tokens = lemmatizer.lemmatize_tokens_spacy(tokens)

    # Step 4: Join tokens and convert to TF-IDF vector
    final_text = ' '.join(lemmatized_tokens)
    vector = tfidf.transform([final_text])  # shape: (1, n_features)

    # Step 4b: Add VADER sentiment score (same as training setup)
    vader_score = analyzer.polarity_scores(final_text)['compound']
    vector_full = np.hstack([vector.toarray(), [[vader_score]]])  # shape: (1, n_features + 1)

    # Step 5: Scale and apply PCA
    vector_scaled = scaler.transform(vector_full)
    vector_pca = pca.transform(vector_scaled)

    # Step 6: Predict
    predicted_class = model.predict(vector_pca)[0]
    sentiment_labels = {0: "Negative", 1: "Neutral", 2: "Positive"}
    predicted_sentiment = sentiment_labels[predicted_class]

    # Step 7: Get class probabilities and confidence
    probs = model.predict_proba(vector_pca)[0]
    prob_dict = {label: prob for label, prob in zip(sentiment_labels.values(), probs)}
    confidence = max(probs)

    return {
        "sentiment_prediction": predicted_sentiment,
        "class_probabilities": prob_dict,
        "confidence": confidence
    }

