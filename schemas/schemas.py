from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from typing import List, Optional, Annotated
# Models for the Patient entity
class PatientModel(BaseModel):
    id: str
    name: str
    city: str
    age: int

# Here, all the above fields are mandatory. If any field is missing, Pydantic will raise a validation error.

# Example 2:
class PatientsModel(BaseModel):
    id: str
    name: str
    city: str
    age: int
    diseases: List[str] = None # Optional in nature and if not given, then by default the value is None
    address: Optional[str]

# Example 3:
class NewModels(BaseModel):
    id:str
    name:str
    email:EmailStr # Built in Type Validation present in Pydantic
    weight: float = Field(gt = 0)  # Field Attribute used to validate the data
    phone: int
    age: int = Field(gt = 0, lt = 60)  # Range of Age : (0,60)
    allergies: List[str] = Field(max_length = 5) # Maximum Length of Diseases : 5

#Example 4:
class Patent(BaseModel):
    name: Annotated[str, Field(max_length = 20,default = 'None', title = "Name of the Patent", description = "Make sure the name to be less than 20 Characters")]
    # Annotated : helps to include further details regarding the field

# Example 5: PS : Check whther the email consists the 'HDFC | ICICI bak name (eg : abdfg@hdfc.com..)
class PatientBank(BaseModel): 
    id: str
    name: str
    age: int
    amount:int = 50000
    email: EmailStr 

    # field_validator() ->  valiudates the fields
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']

        domain_names = value.split('@')[-1] # abdf@gmail.com --> abdf & gmail.com : [-1] index
        if domain_names not in valid_domains:
            raise ValueError("Not a Valid Bank Domain")
        
        return value

# Example 6: PS : no check multiple fields and validate them

class PatientBankName(BaseModel): 
    id: str
    name: str
    age: int
    amount:int = 50000
    email: EmailStr 

    # model_validator() ->  valiudates the fields
    @model_validator(mode='after')
    def amount_validator(cls, model):
        if model.amount <= 0 and model.age < 18:
            raise ValueError("Cant Proceed , either the amount is less than 0 or age is below 18 ")
        else:
            return model
        
