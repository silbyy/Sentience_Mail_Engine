import re
import json
import logging
from textblob import TextBlob

# Professional Logging Configuration
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SentienceEngine:
    def __init__(self):
        """Initializes the engine and loads the intent configuration."""
        self.intents = {
            "Refund/Return": ["refund", "return", "money back", "reimbursement", "iade"],
            "Logistics": ["shipping", "delivery", "track", "cargo", "kargo", "arrived"],
            "Technical": ["login", "error", "bug", "broken", "hata", "not working"],
            "Greetings": ["hello", "hi", "morning", "merhaba", "greetings"]
        }
        logger.info("Sentience Engine initialized successfully.")

    def _clean_text(self, text):
        """Internal method to preprocess and sanitize text for analysis."""
        text = text.lower()
        # Remove email addresses
        text = re.sub(r'\S*@\S*\s?', '', text) 
        # Remove special characters and numbers, keeping basic Turkish English characters
        text = re.sub(r'[^a-zğüşıöç\s]', '', text) 
        return text.strip()

    def analyze(self, raw_text):
        """Core analysis engine with integrated Error Handling and Sentiment Analysis."""
        try:
            # Input Validation
            if not raw_text or not isinstance(raw_text, str):
                logger.warning("Invalid input received: Expected a non-empty string.")
                return {"status": "error", "message": "Invalid input: Text expected."}

            cleaned = self._clean_text(raw_text)
            
            # Checking if text is empty after sanitization 
            if not cleaned:
                logger.warning("Text is empty after preprocessing.")
                return {"status": "error", "message": "No processable text found."}

            # SSentiment Analysis
            blob = TextBlob(cleaned)
            sentiment = blob.sentiment.polarity
            
            # Intent Classification
            detected_intent = "General"
            for intent, keywords in self.intents.items():
                if any(kw in cleaned for kw in keywords):
                    detected_intent = intent
                    break
            
            # Decision Logic (Priority Mapping)
            priority = "High" if sentiment < -0.2 else "Normal"
            
            logger.info(f"Analysis successful. Intent detected: {detected_intent}")
            return {
                "intent": detected_intent,
                "sentiment_score": round(sentiment, 2),
                "priority": priority,
                "status": "success"
            }

        except Exception as e:
            # Catching unexpected technical failures here
            logger.error(f"An unexpected error occurred: {str(e)}")
            return {"status": "error", "message": "Internal processing error."}

# testtt
if __name__ == "__main__":
    engine = SentienceEngine()
    
    # Chaos List urraa
    test_cases = [
        "I am very angry, I want a refund!", # Valid english input
        "",                                  # Empty string
        999999,                              # Invalid type (Integer)
        "!!! ???",                           # Just punctuations
        "Merhaba, kargom nerede?"            # Valid Turkish input
    ]
    
    print("\n STARTING SYSTEM STRESS TEST \n")
    for case in test_cases:
        print(f"Input: {case}")
        result = engine.analyze(str(case) if not isinstance(case, str) else case)
        print(json.dumps(result, indent=2))
        print("-" * 40)