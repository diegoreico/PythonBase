from dataclasses import dataclass, field


@dataclass(frozen=True)
class Person:
    name: str = field(init=True) 
    age: int = None
    address: str = None
