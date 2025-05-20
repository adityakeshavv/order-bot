from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from .db import SessionLocal
from .models import Order, ProgressEvent

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/orders")
def get_all_orders(order_id: int | None = Query(None, description="Filter by order ID"), db: Session = Depends(get_db)):
    query = db.query(Order)
    if order_id is not None:
        query = query.filter(Order.order_id == order_id)
    return query.all()

@app.get("/orders/{order_id}/progress")
def get_order_progress(order_id: int, db: Session = Depends(get_db)):
    return db.query(ProgressEvent).filter(ProgressEvent.order_id == order_id).all()
