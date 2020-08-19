import marshmallow as m
from marshmallow_dataclass import class_schema
from typing import (
    Any,
    Dict,
    Mapping,
    Optional,
    Type,
)
from urllib.parse import unquote_plus


__all__ = [
    "JsonModelMetaclass",
    "JsonModelBaseclass",
    "QuotedStringField",
]


class JsonModelMetaclass(type):

    # noinspection PyPep8Naming
    @property
    def Schema(cls) -> Type[m.Schema]:
        return class_schema(cls)


class JsonModelBaseclass(metaclass=JsonModelMetaclass):
    class Meta:
        unknown = m.EXCLUDE


# noinspection DuplicatedCode
class QuotedStringField(m.fields.Field):
    def _serialize(
            self,
            value: Optional[str],
            attr: str,
            obj: Any,
            **kwargs: Dict[str, Any]  # Type: ignore
    ) -> Optional[str]:
        if value is None:
            return None
        return

    def _deserialize(
            self,
            value: Optional[str],
            attr: Optional[str],
            data: Optional[Mapping[str, Any]],
            **kwargs: Dict[str, Any]
    ) -> Optional[str]:
        if value is None:
            return None
        return unquote_plus(value)
