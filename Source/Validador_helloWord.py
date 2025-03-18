from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(default="123")

user = User()
print(user)

    