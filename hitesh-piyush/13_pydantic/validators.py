from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    username: str

    # mention the 'field' you have to validate, verbatim
    @field_validator('username')
    def check_name_length(cls, value):
        if len(value)<4:
            raise ValueError("The name should have at least 4 characters.")
        return value


class SignUpData(BaseModel):
    password: str
    confirm_password: str

    # model_validator takes the field values at once and then allows us to perform validation

    @model_validator(mode='after')
    def password_same(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("The passwords don't match bro :( ")
        return values
            
