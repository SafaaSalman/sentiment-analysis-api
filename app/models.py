from transformers import pipeline, logging
import logging as python_logging

# Set up logging
logging.set_verbosity_error()
python_logging.basicConfig(level=python_logging.INFO)
logger = python_logging.getLogger(__name__)

class SentimentModel:
    def __init__(self):
        try:
            logger.info("Loading sentiment analysis model...")
            self.model = pipeline(
                "sentiment-analysis",
                model="distilbert-base-uncased-finetuned-sst-2-english",
                device="cpu"  # Force CPU usage initially
            )
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.error(f"Failed to load model: {str(e)}")
            raise

    def predict(self, text: str):
        try:
            if not text.strip():
                return {"error": "Text cannot be empty"}
            return self.model(text)[0]
        except Exception as e:
            logger.error(f"Prediction failed: {str(e)}")
            return {"error": str(e)}

# Initialize model
try:
    model = SentimentModel()
except Exception as e:
    logger.error(f"Failed to initialize sentiment model: {str(e)}")
    model = None