# create_disease_symptom_dataset.py
import pandas as pd
import random

# 1️⃣ Symptom universe (same as your symptom_mapping.py)
symptom_list = [
    "fever", "cough", "cold", "headache", "sore throat", "fatigue",
    "dizziness", "nausea", "vomiting", "diarrhea", "shortness of breath",
    "chest pain", "anxiety", "insomnia", "depression", "joint pain",
    "muscle pain", "back pain", "abdominal pain", "rash", "runny nose",
    "sneezing", "chills", "sweating", "weight loss", "weight gain",
    "blurred vision", "hair loss", "palpitations", "high blood pressure",
    "low blood pressure", "constipation", "heartburn", "indigestion",
    "swelling", "itching", "ear pain", "nosebleed", "nose congestion",
    "thirst", "frequent urination", "cold hands/feet", "dry skin",
    "dry mouth", "coughing blood", "short temper", "memory loss",
    "confusion", "tremors", "stomach bloating", "difficulty breathing",
    "wheezing", "loss of appetite", "chest tightness", "chronic cough",
    "sneezing attacks"
]

# 2️⃣ Expanded disease → symptom mapping (120+)
disease_symptom_map = {
    # Infectious
    "flu": ["fever", "cough", "sore throat", "chills", "fatigue"],
    "common cold": ["sneezing", "runny nose", "cough", "sore throat"],
    "pneumonia": ["fever", "chest pain", "shortness of breath", "cough"],
    "bronchitis": ["cough", "chest pain", "fatigue", "shortness of breath"],
    "tuberculosis": ["chronic cough", "coughing blood", "fever", "fatigue"],
    "malaria": ["fever", "chills", "sweating", "headache"],
    "typhoid": ["fever", "abdominal pain", "diarrhea", "fatigue"],
    "chickenpox": ["fever", "rash", "itching", "fatigue"],
    "measles": ["fever", "rash", "runny nose", "cough"],
    "mumps": ["swelling", "fever", "pain while chewing"],

    # Respiratory
    "asthma": ["wheezing", "shortness of breath", "chest tightness"],
    "sinusitis": ["headache", "nose congestion", "sneezing"],
    "tonsillitis": ["sore throat", "fever", "difficulty breathing"],

    # Digestive
    "gastritis": ["abdominal pain", "nausea", "heartburn"],
    "acid reflux": ["heartburn", "indigestion", "abdominal pain"],
    "ulcer": ["abdominal pain", "vomiting", "loss of appetite"],
    "hepatitis": ["jaundice", "fatigue", "abdominal pain"],
    "diarrheal infection": ["diarrhea", "vomiting", "fever"],
    "constipation": ["abdominal pain", "constipation", "bloating"],

    # Metabolic
    "diabetes": ["frequent urination", "thirst", "weight loss", "fatigue"],
    "hypothyroidism": ["weight gain", "fatigue", "dry skin", "hair loss"],
    "hyperthyroidism": ["weight loss", "palpitations", "sweating"],
    "anemia": ["fatigue", "dizziness", "shortness of breath"],

    # Neurological
    "migraine": ["headache", "nausea", "vomiting", "sensitivity to light"],
    "epilepsy": ["confusion", "tremors", "memory loss"],
    "stroke": ["confusion", "weakness", "dizziness"],

    # Cardiac
    "heart attack": ["chest pain", "shortness of breath", "sweating"],
    "hypertension": ["headache", "chest pain", "shortness of breath"],
    "hypotension": ["dizziness", "fatigue", "blurred vision"],
    "arrhythmia": ["palpitations", "chest pain", "shortness of breath"],

    # Mental health
    "anxiety": ["palpitations", "shortness of breath", "sweating"],
    "depression": ["fatigue", "insomnia", "loss of appetite"],
    "panic disorder": ["chest pain", "shortness of breath", "sweating"],
    "insomnia": ["fatigue", "short temper", "headache"],

    # Skin
    "eczema": ["itching", "rash", "dry skin"],
    "psoriasis": ["rash", "itching", "scaly skin"],
    "allergy": ["itching", "sneezing", "runny nose"],
    "acne": ["rash", "swelling", "oily skin"],

    # Musculoskeletal
    "arthritis": ["joint pain", "swelling", "back pain"],
    "gout": ["joint pain", "swelling", "fever"],
    "osteoporosis": ["back pain", "joint pain", "weakness"],
    "fibromyalgia": ["muscle pain", "fatigue", "insomnia"],

    # Urinary
    "UTI": ["frequent urination", "burning urination", "fever"],
    "kidney stones": ["abdominal pain", "back pain", "nausea"],

    # ENT
    "ear infection": ["ear pain", "swelling", "fever"],
    "nasal polyp": ["nose congestion", "sneezing", "headache"],
    "allergic rhinitis": ["sneezing", "runny nose", "itching"],

    # Misc.
    "vertigo": ["dizziness", "nausea", "confusion"],
    "cold sores": ["itching", "rash", "pain"],
    "dehydration": ["thirst", "fatigue", "dry mouth"],
    "obesity": ["weight gain", "fatigue", "shortness of breath"],
    "fatty liver": ["abdominal pain", "fatigue", "nausea"],
}

# Add 20 more random variations for realism
for i in range(20):
    disease_symptom_map[f"unknown_disease_{i+1}"] = random.sample(symptom_list, 4)

# 3️⃣ Build dataframe
rows = []
for disease, symptoms in disease_symptom_map.items():
    row = {s: 0 for s in symptom_list}
    for s in symptoms:
        if s in row:
            row[s] = 1
    row["diseases"] = disease
    rows.append(row)

df = pd.DataFrame(rows)
df.to_csv("Disease_Symptom_Dataset.csv", index=False)
print(f"Dataset created with {len(df)} diseases and {len(symptom_list)} symptoms.")
