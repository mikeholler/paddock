import marshmallow as m
from marshmallow_dataclass import class_schema
from typing import Type


__all__ = [
    "JsonModelMetaclass",
    "JsonModelBaseclass",
]


class JsonModelMetaclass(type):

    # noinspection PyPep8Naming
    @property
    def Schema(cls) -> Type[m.Schema]:
        return class_schema(cls)


class JsonModelBaseclass(metaclass=JsonModelMetaclass):
    class Meta:
        unknown = m.EXCLUDE
