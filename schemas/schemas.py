from pydantic import BaseModel
from typing import List, Optional
# Models for the Patient entity
class PatientModel(BaseModel):
    id: str
    name: str
    city: str
    age: int

# Here, all the above fields are mandatory. If any field is missing, Pydantic will raise a validation error.

class PatientsModel(BaseModel):
    id: str
    name: str
    city: str
    age: int
    diseases: List[str] = None # Optional in nature and if not given, then by default the value is None
    address: Optional[str]