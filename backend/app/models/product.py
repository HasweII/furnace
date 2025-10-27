from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..database import Base

class Category(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    image_url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    category = relationship('Category', back_populates='products')
    
    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', category_id={self.category_id})>"