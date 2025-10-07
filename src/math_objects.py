from dataclasses import dataclass
from typing import Tuple

class MathObject:
    pass

###
###
###

@dataclass(frozen=True)
class Point(MathObject):
    name: str
    def __repr__(self) -> str:
        return f"Point({self.name})"
    
@dataclass(frozen=True)
class LineSegment(MathObject):
    points: Tuple[Point, Point]
    length: float
    def __repr__(self) -> str:
        return f"LineSegment(p0={self.points[0]}, p1={self.points[1]}, length={self.length})"
    
@dataclass(frozen=True)
class Angle(MathObject):
    points: Tuple[Point, Point, Point]
    degrees: float

    @property
    def vertex(self) -> Point:
        return self.points[1]
    
    def __repr__(self) -> str:
        return f"Angle(p0={self.points[0]}, p1={self.points[1]}, p2={self.points[2]}, degrees={self.degrees})"