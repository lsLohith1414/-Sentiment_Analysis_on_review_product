from pydantic import BaseModel, Field
from typing import Annotated


class Review(BaseModel):

    review : Annotated[str, Field(..., description="Review of the product", examples=["This product is good","This product is bad"])]
    