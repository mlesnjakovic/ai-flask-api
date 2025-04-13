from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd

FEATURE_ORDER = [
    'AI Adoption Rate (%)',
    'AI-Generated Content Volume (TBs per year)',
    'Job Loss Due to AI (%)',
    'Human-AI Collaboration Rate (%)',
    'Consumer Trust in AI (%)',
    'Market Share of AI Companies (%)'
]

app = Flask(__name__)
CORS(app)

model = joblib.load("ai_revenue_model.pkl")

print("✅ Flask API je pokrenut.")
print("📊 Model očekuje značajke u sljedećem redoslijedu:")
for i, feature in enumerate(FEATURE_ORDER, start=1):
    print(f"{i}. {feature}")

@app.route('/')
def home():
    return "AI Revenue Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_features = data.get("features", [])
        
        if len(input_features) != len(FEATURE_ORDER):
            return jsonify({
                "error": f"Broj značajki ({len(input_features)}) nije ispravan. Očekuje se {len(FEATURE_ORDER)} značajki u ovom redoslijedu: {FEATURE_ORDER}"
            }), 400

        features = pd.DataFrame([input_features], columns=FEATURE_ORDER)
        prediction = model.predict(features)
        return jsonify({"prediction": prediction[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
