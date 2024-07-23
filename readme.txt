- run the API: uvicorn app:app --reload
- upload the JSON file: 
    curl -X POST "http://127.0.0.1:8000/predict/" \
     -H "Content-Type: application/json" \
     -d @input/input_sample.json