from pydantic import BaseModel


class userCreate(BaseModel):

    name: str
    email: str
