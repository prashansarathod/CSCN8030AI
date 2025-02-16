import joblib
import pandas as pd

MODEL_PATH = "dev/adoption_model.pkl"

def load_model():
    """Load the trained model."""
    return joblib.load(MODEL_PATH)

def predict_outcome(animal_data):
    """Predict the adoption outcome using the trained model."""
    model = load_model()
    
    df = pd.DataFrame([animal_data])
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0].max()
    
    return {"predicted_outcome": prediction, "adoption_probability": probability}
