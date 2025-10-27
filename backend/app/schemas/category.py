from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name = Field(..., min_length=3, max_length=100, description="Category name")
    slug = Field(..., min_length=3, max_length=100, description="Category slug")
    
class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int = Field(..., description="Category ID")
    
    class Config:
        from_attributes = True