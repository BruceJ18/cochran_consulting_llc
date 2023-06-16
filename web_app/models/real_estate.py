from dataclasses import dataclass


@dataclass
class Real_Estate:
    id: int
    name: str
    price: str
    location: str
    rooms: int
    baths: int
    sqft: int
    link: str
    sold: False
