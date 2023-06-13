from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Client:
    id: int
    name: str 
    business_name: str 
    email: str
    cell_number: str
    website_address: str
    annual_revenue: int
    questions_or_comments: str 


@dataclass
class Employee:
    id: int
    name: str
    cell_number: str
    email: str
    background: str
    positions: list[str]
    linkedin: str

@dataclass
class Business:
    id: int
    name: str
    business_desc: str
    link: str
    sold: False

@dataclass
class Real_Estate:
    id: int
    price: str
    location: str
    rooms: int
    baths: int
    sqft: int
    link: str
    sold: False
