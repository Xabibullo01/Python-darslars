from pydantic import BaseModel

class Products(BaseModel):
    title: str
    description: str
    price: float
    image: str
    quantity: int

banana = Products(
    title="Banana",
    description="this is fuit",
    price=2.4,
    image="kbjvvhv.jpg",
    quantity=10,
)

print(banana.model_dump())