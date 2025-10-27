from pydantic import BaseModel, Field
from typing import Optional

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="The ID of the product")
    review: int = Field(..., ge=0, description="The review of the product")
    
class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="The ID of the product")
    review: int = Field(..., ge=0, description="The review of the product")
    
class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="The name of the product")
    review: int = Field(..., ge=0, description="The review of the product")
    image_url: Optional[str] = Field(None, description="The image URL of the product")
    
class CartResponse(BaseModel):
    itmes: list[CartItem] = Field(..., description="The items in the cart")
    items_count: int = Field(..., description="The number of items in the cart")