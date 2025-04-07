from fastapi import FastAPI
from app.models import model
from app.schemas import SentimentRequest, SentimentResponse

app = FastAPI(
    title="Sentiment Analysis API",
    description="API for analyzing text sentiment using DistilBERT",
    version="1.0.0"
)

@app.post("/predict", response_model=SentimentResponse)
async def predict_sentiment(request: SentimentRequest):
    prediction = model.predict(request.text)
    return {
        "sentiment": prediction["label"],
        "confidence": prediction["score"]
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}