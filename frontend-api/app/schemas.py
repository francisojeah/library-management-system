from pydantic import BaseModel

class UserCreate(BaseModel):
    firstname: str
    lastname: str
    email: str

    class Config:
        from_attributes = True
