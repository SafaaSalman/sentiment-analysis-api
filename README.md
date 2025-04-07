# Sentiment Analysis API

This project provides a RESTful API for sentiment analysis using a pre-trained transformer model. The API can classify text as positive, negative, or neutral with a confidence score.

## Features
- **Endpoints**:
  - `/predict`: Analyze the sentiment of a given text.
  - `/health`: Check the health status of the API and model.
- **Model**: Uses Hugging Face's `distilbert-base-uncased-finetuned-sst-2-english` for sentiment analysis.
- **Error Handling**: Handles invalid or empty input gracefully.

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd sentiment-analysis-api
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage Instructions

### Running the API
1. Start the API server using `uvicorn`:
   ```bash
   uvicorn app.main:app --reload
   ```

2. The API will be available at `http://localhost:8000`.

### API Endpoints
- **Health Check**:
  - URL: `http://localhost:8000/health`
  - Method: `GET`
  - Response: 
    ```json
    {
      "status": "healthy",
      "model_loaded": true
    }
    ```

- **Predict Sentiment**:
  - URL: `http://localhost:8000/predict`
  - Method: `POST`
  - Request Body:
    ```json
    {
      "text": "Your input text here"
    }
    ```
  - Response:
    ```json
    {
      "sentiment": "positive",
      "confidence": 0.98
    }
    ```

---

## Testing the API

### Using the Test Script
1. Run the provided `test_api.py` script to test the API:
   ```bash
   python test_api.py
   ```

2. The script will test the following cases:
   - Health check
   - Positive sentiment
   - Negative sentiment
   - Neutral sentiment
   - Empty text input

3. Example output:
   ```
   Testing API endpoints...

   1. Testing health check:
   Status Code: 200
   Response Body:
   {
     "status": "healthy",
     "model_loaded": true
   }

   2. Testing positive sentiment:
   Status Code: 200
   Response Body:
   {
     "sentiment": "positive",
     "confidence": 0.98
   }
   ```

### Manual Testing
You can also test the API manually using tools like [Postman](https://www.postman.com/) or `curl`.

Example `curl` command for sentiment prediction:
```bash
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{"text": "I love this product!"}'
```

---

## Notes
- Ensure the model is loaded successfully before making predictions.
- If you encounter issues, check the logs for detailed error messages.

---
