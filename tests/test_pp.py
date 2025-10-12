from src.pyproof.geometry.mathobjs import Problem, Angle, LineSegment, Point
from src.pyproof.dde import deduce

from src import pyproof


pyproof.set_logging_state(True)

pA, pB, pC = Point("A"), Point("B"), Point("C")
initial_facts = [
    pA,
    pB,
    pC,
    Angle((pA, pB, pC), angle=90),
    LineSegment((pB, pA), 1),
    LineSegment((pB, pC), 1),
]
problem = Problem(initial_facts)
deduce(problem)
