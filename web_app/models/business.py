from dataclasses import dataclass


@dataclass
class Business:
    id: int
    name: str
    business_desc: str
    link: str
    sold: False