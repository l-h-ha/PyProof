from typing import TypeAlias, TYPE_CHECKING

if TYPE_CHECKING:
    from .math_objects import MathObject, Point, LineSegment, Angle
    from .problem_objects import Problem

MathObjectLike: TypeAlias = "MathObject"
PointLike: TypeAlias = "Point"
LineSegmentLike: TypeAlias = "LineSegment"
AngleLike: TypeAlias = "Angle"

ProblemLike: TypeAlias = "Problem"