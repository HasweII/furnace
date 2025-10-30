from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .category import CategoryResponse

class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Product name")
    description: Optional[str] = Field(None, min_length=1, max_length=200, description="Product description")
    category_id: int = Field(..., description="Category ID")
    image_url: Optional[str] = Field(None, description="Product image URL")
    
class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int = Field(..., description="Product ID")
    created_at: datetime = Field(..., description="Product creation date")
    
    category: CategoryResponse = Field(..., description="Product category")
    
    class Config:
        from_attributes = True
        
class ProductListResponse(BaseModel):
    products: list[ProductResponse] = Field(..., description="List of products")
    total: int = Field(..., description="Total number of products")
