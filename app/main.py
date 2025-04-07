from fastapi import FastAPI, HTTPException
from app.models import model
from app.schemas import SentimentRequest, SentimentResponse

app = FastAPI()

@app.post("/predict", response_model=SentimentResponse)
async def predict_sentiment(request: SentimentRequest):
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Service unavailable - model not loaded"
        )
    
    try:
        prediction = model.predict(request.text)
        if "error" in prediction:
            raise HTTPException(
                status_code=400,
                detail=prediction["error"]
            )
        return {
            "sentiment": prediction["label"],
            "confidence": prediction["score"]
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )

@app.get("/health")
async def health_check():
    return {
        "status": "healthy" if model is not None else "unhealthy",
        "model_loaded": model is not None
    }