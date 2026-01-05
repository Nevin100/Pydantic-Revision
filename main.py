# Import necessary libraries
# 1) Pydantic Library : Used for data validation and settings management using Python type annotations.
from fastapi import FastAPI, HTTPException, status
import json
from pydantic import BaseModel

# Define the FastAPI app
app = FastAPI()

#1.) Define a Pydantic model for the request body
class Patient(BaseModel):
    id: str
    name: str
    city: str
    age: int

# Function to load existing patient data from a JSON file
def load_Data():
    with open("./patients.json", "r") as f:
        return json.load(f)

# POST Endpoint to create a new patient record
@app.post("/patients/create-patient", status_code=status.HTTP_201_CREATED)

# patient parameter will be automatically validated against the Patient model 
def create_patient(patient: Patient):
    data = load_Data()

    if patient["id"] in data:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Patient with this ID already exists"
        )
    
    data[patient["id"]] = patient

    with open("./patients.json", "w") as f:
        json.dump(data, f, indent=4)

    return {"message": "Patient record created successfully"}

