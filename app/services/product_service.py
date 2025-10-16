from sqlalchemy.orm import Session
from app.models import models, schemas
from typing import List, Optional

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 100, category: Optional[str] = None, search: Optional[str] = None):
    query = db.query(models.Product)
    if category:
        query = query.filter(models.Product.category == category)
    if search:
        search_term = f"%{search}%"
        query = query.filter(
            models.Product.name.ilike(search_term) |
            models.Product.description.ilike(search_term)
        )
    return query.offset(skip).limit(limit).all()

def get_categories(db: Session):
    return db.query(models.Product.category).distinct().all()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = get_product(db, product_id)
    if db_product is None:
        return None
    
    for key, value in product.dict().items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if db_product is None:
        return False
    
    db.delete(db_product)
    db.commit()
    return True