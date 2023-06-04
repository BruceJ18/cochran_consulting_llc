from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Client:
    client_name: str 
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
    name: str
    price: str
    location: str
    rooms: int
    baths: int
    sqft: int
    sold: False
