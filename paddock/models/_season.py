from dataclasses import dataclass, field
from marshmallow_enum import EnumField
from typing import (
    Optional,
    List,
)
from paddock.models._common import Category
from paddock._dataclasses import require_kwargs_on_init
from paddock._marshmallow import (
    JsonModelBaseclass,
    QuotedStringField,
    NumericBooleanField,
)


__all__ = [
    "Season",
    "SeasonCar",
    "SeasonTrack",
]


# TODO: Car class.


@dataclass(frozen=True)
class SeasonCar(JsonModelBaseclass):
    id: int = field(metadata={"data_key": "id"})

    name: str = field(metadata={
        "marshmallow_field": QuotedStringField(data_key="name")
    })


@dataclass(frozen=True)
class SeasonTrack(JsonModelBaseclass):
    id: int = field(metadata={"data_key": "id"})

    name: str = field(metadata={
        "marshmallow_field": QuotedStringField(data_key="name")
    })

    configuration_name: Optional[str] = field(metadata={
        "marshmallow_field": QuotedStringField(
            data_key="config",
            deserialize_empty_as_none=True
        )
    })

    race_week: int = field(metadata={"data_key": "raceweek"})

    # TODO: Figure out what this is and decode it into an enum? Or some other
    # specialized type, or else document.
    time_of_day: int = field(metadata={"data_key": "timeOfDay"})


@dataclass(frozen=True)
class Season(JsonModelBaseclass):
    series_id: int = field(metadata={"data_key": "seriesid"})
    season_id: int = field(metadata={"data_key": "seasonid"})

    year: int = field(metadata={"data_key": "year"})
    quarter: int = field(metadata={"data_key": "quarter"})
    # TODO: is this current race week at the time of the request?
    # The completed series all have the maximum week, but maybe in progress
    # seasons are different?
    race_week: int = field(metadata={"data_key": "raceweek"})

    series_name: str = field(metadata={
        "marshmallow_field": QuotedStringField(data_key="seriesshortname")
    })

    # TODO: fix to parse out milliseconds into date time.
    starts_at_millis: int = field(metadata={"data_key": "start"})
    ends_at_millis: int = field(metadata={"data_key": "end"})

    is_active: bool = field(metadata={"data_key": "active"})
    is_lite: bool = field(metadata={"data_key": "islite"})

    # TODO: Parse out license group like Category with enum
    series_license_group: int = field(metadata={"data_key": "serieslicgroupid"})

    category: Category = field(metadata={
        "marshmallow_field": EnumField(
            enum=Category,
            by_value=True,
            data_key="catid",
        )
    })
    """
    Category of racing e.g., Category.road
    """

    tracks: List[SeasonTrack]
    cars: List[SeasonCar]


require_kwargs_on_init(Season)
require_kwargs_on_init(SeasonTrack)
