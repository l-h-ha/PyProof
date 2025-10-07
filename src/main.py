from .math_objects import *
from .problem_objects import *

pA = Point("A")
pB = Point("B")
pC = Point("C")

initial_facts = [
    LineSegment((pA, pB), 1),
    LineSegment((pB, pC), 2),
    Angle((pA, pB, pC), 90),
]

problem = Problem(initial_facts=initial_facts)
solver = Deducer(problem)
solver.deduce()
