from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    from ..geometry.mathobjs import MathObject

GroupOfFacts: TypeAlias = list["MathObject"] | set["MathObject"]

__all__ = ["GroupOfFacts"]
