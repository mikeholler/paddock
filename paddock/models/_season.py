import datetime as dt
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Optional,
    List,
)
from paddock.models._common import (
    Category,
    License,
    TimeOfDay,
)
from paddock._dataclasses import require_kwargs_on_init
from paddock._marshmallow import (
    JsonModelBaseclass,
    QuotedStringField,
    UtcMillisecondDateTime,
)
from paddock._util import maybe_value_of


__all__ = [
    "Season",
    "SeasonCar",
    "SeasonTrack",
]


# TODO: Car class.


@dataclass
class SeasonCar(JsonModelBaseclass):
    id: int = field(metadata={"data_key": "id"})
    """
    Unique identifier for the car.
    """

    name: str = field(metadata={
        "marshmallow_field": QuotedStringField(data_key="name")
    })
    """
    Human-readable car name.
    """


@dataclass
class SeasonTrack(JsonModelBaseclass):
    id: int = field(metadata={"data_key": "id"})
    """
    Unique identifier for the track + configuration combination.
    """

    name: str = field(metadata={
        "marshmallow_field": QuotedStringField(data_key="name")
    })
    """
    Human-readable track name.
    """

    configuration_name: Optional[str] = field(metadata={
        "marshmallow_field": QuotedStringField(
            data_key="config",
            deserialize_empty_as_none=True
        )
    })
    """
    Human readable track configuration name.
    """

    race_week: int = field(metadata={"data_key": "raceweek"})
    """
    Race week is 0-indexed, with the first race week being week 0.

    In a normal 12-week series, the range of values is 0..11, inclusive
    on both ends.
    """

    raw_time_of_day: int = field(metadata={"data_key": "timeOfDay"})
    """
    Time of day that the race will take place. This is the raw value. Consider
    using the time_of_day property instead.
    """

    time_of_day: Optional[int] = field(init=False)
    """
    raw_time_of_day coerced into an easy-to-read enum if a recognizable value
    """

    def __post_init__(self):
        self.time_of_day = maybe_value_of(TimeOfDay, self.raw_time_of_day)


@dataclass
class Season(JsonModelBaseclass):
    series_id: int = field(metadata={"data_key": "seriesid"})
    season_id: int = field(metadata={"data_key": "seasonid"})

    year: int = field(metadata={"data_key": "year"})
    """
    4-digit year. E.g., 2020.
    """

    quarter: int = field(metadata={"data_key": "quarter"})
    """
    Quarter of the year. Legal values: 1, 2, 3, 4.
    """

    # TODO: is this current race week at the time of the request?
    # The completed series all have the maximum week, but maybe in progress
    # seasons are different?
    race_week: int = field(metadata={"data_key": "raceweek"})

    series_name: str = field(metadata={
        "marshmallow_field": QuotedStringField(data_key="seriesshortname")
    })

    starts_at: dt.datetime = field(metadata={
        "marshmallow_field": UtcMillisecondDateTime(data_key="start"),
    })
    ends_at: dt.datetime = field(metadata={
        "marshmallow_field": UtcMillisecondDateTime(data_key="end"),
    })

    is_active: bool = field(metadata={"data_key": "active"})
    is_lite: bool = field(metadata={"data_key": "islite"})

    raw_license: int = field(metadata={"data_key": "serieslicgroupid"})
    raw_category: int = field(metadata={"data_key": "catid"})

    category: Optional[int] = field(init=False)
    license: Optional[int] = field(init=False)

    tracks: List[SeasonTrack]
    cars: List[SeasonCar]

    def __post_init__(self):
        self.license = maybe_value_of(License, self.raw_license)
        self.category = maybe_value_of(Category, self.raw_category)


require_kwargs_on_init(Season)
require_kwargs_on_init(SeasonTrack)
