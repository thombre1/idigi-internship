from pydantic import BaseModel, Field
from typing import Optional
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length = 3,
        max_length = 50,
        description = "Employee Name",
        examples = "Hitesh Choudhary"
    )

    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        # Greater than or Equal To
        ge = 10000

        #Less than or equal to
        le = 1000000
        )
    
    # ... means that field is required(I know WTF)
class User(BaseModel):
    email: str = Field(..., regex=r'')
    phone: str = Field(..., regex=r'')
    discount: float = Field(
        ge=0,
        le=100,
        Description = "Discount in percentage"
    )
