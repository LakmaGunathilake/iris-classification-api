from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.pkl")

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

species_map = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

@app.post("/predict")
def predict_species(features: IrisFeatures):
    data = np.array([[features.sepal_length, features.sepal_width,
                      features.petal_length, features.petal_width]])
    prediction = model.predict(data)[0]
    species = species_map.get(prediction, "Unknown")
    return {
        "predicted_class": int(prediction),
        "species": species
    }