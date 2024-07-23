import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from model import predict
from datetime import datetime


app = FastAPI()

class PredictionInput(BaseModel):
    date: datetime  
    site_id: int
    ad_type_id: int
    geo_id: int
    device_category_id: int
    advertiser_id: int
    order_id: int
    line_item_type_id: int
    os_id: int
    integration_type_id: int
    monetization_channel_id: int
    ad_unit_id: int
    total_impressions: int
    viewable_impressions: int
    measurable_impressions: int
    revenue_share_percent: int

@app.get('/')
def index():
    return {'message': 'Revenue in Ads Predictor'}

@app.post("/predict/")
def make_prediction(input_data: PredictionInput):
    input_df = pd.DataFrame([input_data.dict()])
    try:
        prediction = predict(input_df)
        return {"The prediction is": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
