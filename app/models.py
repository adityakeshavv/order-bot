from sqlalchemy import Column, Integer, String, Date, Numeric, TIMESTAMP, ForeignKey, Text
from .db import Base

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, nullable=False)
    material_grade = Column(String(30))
    quantity_ton = Column(Numeric(10, 2))
    order_date = Column(Date)
    expected_delivery = Column(Date)
    status = Column(String(15))
    last_update_ts = Column(TIMESTAMP)

class ProgressEvent(Base):
    __tablename__ = "progress_events"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.order_id", ondelete="CASCADE"))
    event_time = Column(TIMESTAMP)
    location = Column(String(50))
    event = Column(Text)
    notes = Column(Text)
