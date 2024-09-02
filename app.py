from flask import Flask, request, jsonify
import joblib
from pydantic import BaseModel, ValidationError

app = Flask(__name__)
model = joblib.load("finalized_model.pkl")

class PredictionRequest(BaseModel):
    home_odds: float
    away_odds: float
    total_goals: float

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [PredictionRequest(**item) for item in request.json]
        predictions = [model.predict([item.dict().values()])[0] for item in data]
        return jsonify(predictions)
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
