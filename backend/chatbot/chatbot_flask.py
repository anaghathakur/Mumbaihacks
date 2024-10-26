import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import requests
import replicate
from flask import Flask, request, jsonify, render_template
from fuzzywuzzy import process
import nltk
from nltk.corpus import stopwords

# Download stopwords from NLTK
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Set your Replicate API token
replicate_client = replicate.Client(api_token="r8_ZDm4QEcAEyDmvO92w6Sw57mh3Nc4OP01Boz58")  # Replace with your actual API token

# Set up the Flask app
app = Flask(__name__)

# List of allowed phrases (non-finance related)
allowed_phrases = [
    "good morning", "good afternoon", "good evening", "good night", "hello", 
    "hi", "thank you", "thanks", "yes", "ok", "sure", "yeah", 
    "how are you", "what's up", "how's it going"
]

# Enhanced finance-related keywords
finance_keywords = [
    "loan", "investment", "savings", "financial goals", 
    "budget", "expenditure", "income", "mortgage", "interest", 
    "insurance", "mutual funds", "stocks", "retirement", 
    "debt", "expenses", "financial advice", "SIP", "LIC", "tax", 
    "credit score", "financial planning", "asset allocation",
    "cash flow", "wealth management", "pension", "equities"
]

# Function to extract keywords from user input
def extract_keywords(input_text):
    # Remove stopwords
    words = [word for word in input_text.split() if word not in stop_words]
    return words

# Function to check if input relates to finance
def is_finance_related(input_text):
    keywords = extract_keywords(input_text)
    matched_keywords = []
    
    # Use fuzzy matching to find closest finance keywords
    for word in keywords:
        matched = process.extractBests(word, finance_keywords, score_cutoff=70)
        matched_keywords.extend(matched)

    return len(matched_keywords) > 0

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Chatbot route
@app.route('/chat', methods=['POST'])
def chat():
    # Get user input from JSON
    data = request.get_json()
    user_input = data.get("message", "").strip().lower()

    # Check if the input is allowed
    if any(phrase in user_input for phrase in allowed_phrases):
        bot_response = "I'm here to chat! How can I assist you today?"
    elif is_finance_related(user_input):
        # Make a request to the LLaMA API
        try:
            response = replicate_client.run(
                "meta/llama-2-70b-chat",
                input={"prompt": user_input, "max_new_tokens": 100}
            )
            bot_response = response
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        bot_response = "I'm sorry, but I can only assist with finance-related queries."

    return jsonify({"response": bot_response})

# Run Flask app
if __name__ == '__main__':
    app.run(port=5000, debug=True)
