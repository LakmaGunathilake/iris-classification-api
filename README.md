# 🌸 Iris Classification API

This project is a FastAPI-based web service that predicts the species of an Iris flower using a trained machine learning model.

---

## 📦 Project Structure

iris_classification_api/ ├── main.py              
# FastAPI app ├── model.pkl            
# Trained ML model (RandomForestClassifier) ├── load_iris_data.py    
# Data loading and preprocessing ├── README.md            
# Project documentation ├── screenshots/         
# Saved screenshots for documentation

---

## 🚀 How to Run the API

1️⃣ Create and activate Anaconda environment
```bash
conda create -n iris_api_env python=3.11
conda activate iris_api_env

2️⃣ Install dependencies
pip install fastapi uvicorn joblib numpy scikit-learn


3️⃣ Run the server
uvicorn main:app --reload


4️⃣ Test the API
Open your browser and go to:
http://127.0.0.1:8000/docs
Use Swagger UI to send a POST request to /predict with:
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}


Expected response:
{
  "predicted_class": 0,
  "species": "Setosa"
}

Model Details
- Algorithm: RandomForestClassifier
- Training: Done in Google Colab using the Iris dataset
- Export: Saved as model.pkl using joblib

📸 Screenshots
🔹 Project Folder Structure
Project Folder Structure
🔹 Swagger UI Response 1
Swagger UI Response 1
🔹 Swagger UI Response 2
Swagger UI Response 2
🔹 Terminal Running Server
Terminal Running Server

✍️ Author
- Name: Lakma Gunathilake
- Course: Intelligence Systems
- Institution: Horizon Campus


