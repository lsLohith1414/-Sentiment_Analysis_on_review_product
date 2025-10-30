import re
from fastapi import FastAPI
from schema.user_input import Review
from prediction.review_prediction import predict_sentiment
from fastapi.responses import JSONResponse

import sys
app = FastAPI()


@app.get("/")
def home():
    return {"message":"home page of the API"}


@app.get("/about")
def about():
    return {"message":"About page of the API"}



@app.post("/predict")
def review_prediction(review_text: Review):
    try:
        prediction = predict_sentiment(review_text.review)
        return {"Response": prediction}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
        


