from dataclasses import dataclass


@dataclass
class Employee:
    id: int
    name: str
    cell_number: str
    email: str
    background: str
    positions: list[str]
    linkedin: str
