import os
import joblib
import numpy as np
from flask import Flask, request, jsonify, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder=None)

# Load model + scaler once (cold start), reused across warm invocations
model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))


@app.route("/", methods=["GET"])
def home():
    public_dir = os.path.join(os.path.dirname(BASE_DIR), "public")
    return send_from_directory(public_dir, "index.html")


@app.route("/api/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)

        distance_from_home = float(data.get("distance_from_home", 0))
        distance_from_last_transaction = float(data.get("distance_from_last_transaction", 0))
        ratio_to_median_purchase_price = float(data.get("ratio_to_median_purchase_price", 0))
        repeat_retailer = 1.0 if data.get("repeat_retailer") else 0.0
        used_chip = 1.0 if data.get("used_chip") else 0.0
        used_pin_number = 1.0 if data.get("used_pin_number") else 0.0
        online_order = 1.0 if data.get("online_order") else 0.0

        # Model was trained on 10 features; the original app padded the
        # remaining 3 with zeros, so we do the same here for consistency.
        other_features = [0.0, 0.0, 0.0]

        input_data = np.array(
            [
                distance_from_home,
                distance_from_last_transaction,
                ratio_to_median_purchase_price,
                repeat_retailer,
                used_chip,
                used_pin_number,
                online_order,
            ]
            + other_features
        ).reshape(1, -1)

        input_scaled = scaler.transform(input_data)
        prediction = int(model.predict(input_scaled)[0])
        probability = float(model.predict_proba(input_scaled)[0][1])

        return jsonify(
            {
                "fraud": bool(prediction == 1),
                "fraud_probability": probability,
                "confidence": probability if prediction == 1 else (1 - probability),
            }
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Local dev entrypoint (Vercel imports `app` directly and ignores this)
if __name__ == "__main__":
    app.run(debug=True)
