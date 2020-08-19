from dataclasses import dataclass, field
from paddock._dataclasses import require_kwargs_on_init
from paddock._marshmallow import (
    JsonModelBaseclass,
    QuotedStringField,
)


__all__ = [
    "CarRecord",
]


@dataclass(frozen=True)
class CarRecord(JsonModelBaseclass):
    id: int = field(metadata={"data_key": "carid"})
    name: str = field(metadata={
        "marshmallow_field": QuotedStringField(data_key="car_name")
    })


require_kwargs_on_init(CarRecord)
