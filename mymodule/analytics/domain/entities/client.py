from dataclasses import dataclass, field


@dataclass(frozen=True)
class Client:
    id: str = field(init=True) 
    active: int
    prediction_horizon: str
    airport: bool
    weather: bool
    lead_time: int
