from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from .. import _config
from ..utils import log

from copy import deepcopy


class MathObject(ABC):
    @abstractmethod
    def tokenize(self) -> tuple[str, ...]:
        raise NotImplementedError

    @abstractmethod
    def __repr__(self) -> str:
        raise NotImplementedError


###
###
###


@dataclass(frozen=True)
class Point(MathObject):
    name: str

    def tokenize(self) -> tuple[str, ...]:
        return ("point_start", self.name, "point_end")

    def __repr__(self) -> str:
        return f"Point(name={self.name})"


@dataclass(frozen=True)
class LineSegment(MathObject):
    points: tuple[Point, Point]
    length: float

    def tokenize(self) -> tuple[str, ...]:
        return (
            "line_segment_start",
            *self.points[0].tokenize(),
            *self.points[1].tokenize(),
            "line_segment_end",
        )

    def __repr__(self) -> str:
        return f"LineSegment(points=[{self.points[0], self.points[1]}], length={self.length})"


@dataclass(frozen=True)
class Angle(MathObject):
    points: tuple[Point, Point, Point]
    angle: float

    def tokenize(self) -> tuple[str, ...]:
        return (
            "angle_start",
            *self.points[0].tokenize(),
            *self.points[1].tokenize(),
            *self.points[2].tokenize(),
            "angle_end",
        )

    def __repr__(self) -> str:
        return f"Angle(points=[{self.points[0]}, {self.points[1]}, {self.points[2]}], angle={self.angle})"


###
###
###

###
###
###


class Problem:
    def __init__(
        self, facts: list[MathObject] | set[MathObject], init_facts: bool = True
    ) -> None:
        self.facts = set(facts)
        self.cache_line_segment = {}

        if _config.logging:
            log("established a problem with initial facts:", seperate=True, dist=2)
        if init_facts:
            for fact in facts:
                self.add_fact(fact, append=False)
                if _config.logging:
                    log(str(fact))

    def clone(self) -> Problem:
        p = Problem(self.facts, init_facts=False)
        p.cache_line_segment = deepcopy(self.cache_line_segment)
        return p

    def add_facts(self, facts: list[MathObject]) -> None:
        for fact in facts:
            self.add_fact(fact)

    def add_fact(self, fact: MathObject, append: bool = True) -> None:
        if _config.logging:
            log(f"added fact: {str(fact)}", seperate=True, dist=1)
        if isinstance(fact, LineSegment):
            key = tuple(sorted(fact.points, key=lambda p: p.name))
            print(key)
            self.cache_line_segment[key] = fact
        if append:
            self.facts.add(fact)

    ###
    ###
    ###

    def get_segment(self, p1: Point, p2: Point) -> LineSegment | None:
        key = tuple(sorted((p1, p2), key=lambda p: p.name))
        if key in self.cache_line_segment:
            return self.cache_line_segment[key]
        return None
