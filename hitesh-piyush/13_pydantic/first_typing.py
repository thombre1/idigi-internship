from pydantic import BaseModel
from typing import List, Optional, Dict

# We use pydantic BaseModel for primitive data types like int, float, bool, str
# typing for more advanced data types
class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: int
    price: Dict[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    # Image url cn be there else it will by default be set to None, we have aditionally added None here( it was not needed)
    image_url: Optional[str] = None

