from pydantic import BaseModel

# Models for the Patient entity
class PatientModel(BaseModel):
    id: str
    name: str
    city: str
    age: int

# Here, all the above fields are mandatory. If any field is missing, Pydantic will raise a validation error.
