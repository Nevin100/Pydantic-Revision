# 1) Pydantic Library : Used for data validation and settings management using Python type annotations.

from fastapi import FastAPI, HTTPException, status
import json

# 2) Importing Pydantic Schemas
from schemas.schemas import PatientModel

# Define the FastAPI app
app = FastAPI()

# Function to load existing patient data from a JSON file
def load_Data():
    with open("./patients.json", "r") as f:
        return json.load(f)

# POST Endpoint to create a new patient record
@app.post("/patients/create-patient", status_code=status.HTTP_201_CREATED)
# patient parameter will be automatically validated against the Patient model 
def create_patient(patient: PatientModel):
    data = load_Data()

    if patient.id in data:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Patient with this ID already exists"
        )
    
    data[patient["id"]] = patient

    with open("./patients.json", "w") as f:
        json.dump(data, f, indent=4)

    return {"message": "Patient record created successfully"}

