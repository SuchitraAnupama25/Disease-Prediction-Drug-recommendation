from flask import Flask, request, render_template, jsonify
import numpy as np
import joblib
from tensorflow.keras.models import load_model
from symptom_mapping import symptom_list  # your list of symptoms (50–60)
from drug_mapping import drug_mapping      # your disease-drug mapping (100+)

app = Flask(__name__)

# -----------------------------
# Load trained ANN model and encoder
# -----------------------------
model = load_model("disease1_model.keras")
encoder = joblib.load("disease1_label_encoder.pkl")

# -----------------------------
# Helper function for prediction
# -----------------------------
def predict_disease(symptoms_input):
    # Create a binary input vector (1 = symptom present)
    input_vector = np.zeros(len(symptom_list))
    for i, symptom in enumerate(symptom_list):
        if symptom.lower() in [s.lower().strip() for s in symptoms_input]:
            input_vector[i] = 1

    input_vector = input_vector.reshape(1, -1)

    # Predict disease
    prediction = model.predict(input_vector)
    disease_index = np.argmax(prediction)
    disease_name = encoder.inverse_transform([disease_index])[0]

    # Get recommended drug
    recommended_drug = drug_mapping.get(disease_name.lower(), "No recommendation available")

    return disease_name, recommended_drug

# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    symptoms = data.get("symptoms", [])

    if not symptoms:
        return jsonify({"error": "No symptoms provided"}), 400

    disease, drug = predict_disease(symptoms)
    return jsonify({
        "predicted_disease": disease,
        "recommended_drug": drug
    })

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
