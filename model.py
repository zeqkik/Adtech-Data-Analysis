import joblib
import pandas as pd

model = joblib.load('model_encoders/lR_model.joblib')

def preprocess_data(input_data):
    target_encoder = joblib.load('model_encoders/target_encoder.joblib')

    #Applying label encoding to the high cardinality columns
    for col in ['advertiser_id', 'order_id', 'ad_unit_id']:
        le = joblib.load(f'model_encoders/{col}_label_encoder.joblib')
        try:
            input_data[col] = le.transform(input_data[col])
        except Exception as e:
            print(f"Error transforming {col}: {e}")

    #Applying target encoding to the low cardinality columns
    low_cardinality_column = ['site_id', 'ad_type_id', 'device_category_id', 'line_item_type_id', 'os_id', 'monetization_channel_id']
    input_data[low_cardinality_column] = target_encoder.transform(input_data[low_cardinality_column])

    #Drop useless columns
    input_data = input_data.drop(columns = ['geo_id','date','integration_type_id', 'revenue_share_percent', 'ad_unit_id', 'date'])

    return input_data

def predict(data):
     preprocessed_data = preprocess_data(data)

     return model.predict(preprocessed_data)