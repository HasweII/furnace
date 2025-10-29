from sqlalchemy.orm import Session
from typing import Dict
from ..repositories.product import ProductRepository
from ..schemas.cart import CartResponse, CartItem, CartItemCreate, CartItemUpdate

from fastapi import HTTPException, status

class CartService:
    def __init__(self, db: Session):
        self. product_repository = ProductRepository(db)
        
    def add_to_cart(self, cart_data:Dict[int,int], item: CartItemCreate) -> Dict[int,int]:
        product = self.product_repository.get_by_id(item.product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {item.product_id} not found"
            )
        
        if item.product_id in cart_data:
            cart_data[item.product_id] += item.review
        else:
            cart_data[item.product_id] = item.review
            
        return cart_data
    
    def update_cart(self, cart_data:Dict[int,int], item: CartItem) -> Dict[int,int]:
        if item.product_id not in cart_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {item.product_id} not found"
            )
            
        cart_data[item.product_id] = item.review
        return cart_data
    
    def remove_from_cart(self, cart_data:Dict[int,int], product_id: int) -> Dict[int,int]:
        if product_id not in cart_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {product_id} not found"
            )
            
        del cart_data[product_id]
        return cart_data
    
    def get_cart_details(self, cart_data:Dict[int,int]) -> CartResponse:
        if not cart_data:
            return CartResponse(items=[], items_count=0)
        
        product_ids = list(cart_data.keys())
        products = self.product_repository.get_multiple_by_ids(product_ids)
        product_dict = {product.id: product for product in products}
        
        cart_items = []
        total_items = 0
        
        for product_id, review in cart_data.items():
            if product_id in product_dict:
                product = product_dict[product_id]
                
                cart_item = CartItem(product_id=product_id, name=product.name,
                                     review=product.review, image_url=product.image_url)
                
                cart_items.append(cart_item)
                total_items += 1
        
        return CartResponse(items=cart_items, items_count=total_items)