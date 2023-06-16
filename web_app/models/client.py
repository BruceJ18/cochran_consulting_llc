from dataclasses import dataclass


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
