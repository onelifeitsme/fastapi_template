from sqlalchemy.orm import Session
from models.product import Product
from schemas.product import ProductCreate


def create_product(db: Session, product: ProductCreate):
    db_product = Product(name=product.name)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()
