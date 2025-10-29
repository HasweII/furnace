from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Dict
from ..database import get_db
from ..services.cart import CartService
from ..schemas.cart import CartItemCreate, CartItemUpdate, CartResponse
from pydantic import BaseModel

router = APIRouter(
    prefix="/api/cart",
    tags=["Cart"]
)

class AddToCartRequest(BaseModel):
    product_id: int
    review: int
    cart: Dict[int,int] = {}
    
class UpdateCartRequest(BaseModel):
    product_id: int
    review: int
    cart: Dict[int,int] = {}
    
class RemoveFromCartRequest(BaseModel):
    cart: Dict[int,int] = {}

@router.get("", response_model=CartResponse, status_code=status.HTTP_200_OK)
def get_cart(cart_data: Dict[int,int], db: Session = Depends(get_db)):
    service = CartService(db)
    return service.get_cart_details(cart_data)

@router.post("/add", status_code=status.HTTP_201_CREATED)
def add_to_cart(request: AddToCartRequest, db: Session = Depends(get_db)):
    services = CartService(db)
    item = CartItemCreate(product_id=request.product_id, review=request.review)
    updated_cart = services.add_to_cart(request.cart, item)
    return {"cart": updated_cart}

@router.put("/update", status_code=status.HTTP_200_OK)
def update_cart_item(request: UpdateCartRequest, db: Session = Depends(get_db)):
    services = CartService(db)
    item = CartItemUpdate(product_id=request.product_id, review=request.review)
    updated_cart = services.update_cart(request.cart, item)
    return {"cart": updated_cart}

@router.delete("/remove/{product_id}", status_code=status.HTTP_200_OK)
def remove_from_cart(product_id: int, request: RemoveFromCartRequest, db: Session = Depends(get_db)):
    service = CartService(db)
    update_cart = service.remove_from_cart(request.cart, product_id)
    return {"cart": update_cart}