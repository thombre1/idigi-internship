from pydantic import BaseModel, field_validator, model_validator

class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator('first_name', 'last_validator')
    def name_must_be_capital(cls, v):
        if not v.istitle():
            raise ValueError("Name is not in CapitalFormat.")
        return v

class User(BaseModel):
    email: str

    @field_validator
    def email_sanitation(cls, v):
        return v.lower().strip()


class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime
    
    @model_validator(mode="after")
    def check_date(cls, values):
        if values.start_date > values.end_date:
            raise ValueError("The start date exceeds end date. Correct it Please")
        return values
