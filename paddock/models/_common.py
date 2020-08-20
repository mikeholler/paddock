from enum import Enum


__all__ = [
    "Category",
    "License",
]


class Category(Enum):
    oval = 1
    road = 2
    dirt_oval = 3
    dirt_road = 4


class License(Enum):
    R = 1
    D = 2
    C = 3
    B = 4
    A = 5
    PRO = 6
    PRO_WORLD_CUP = 7



