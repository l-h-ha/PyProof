from ..geometry.mathobjs import Problem, Angle, LineSegment
from ..utils import GroupOfFacts

import numpy as np


def pythagorean(problem: Problem) -> GroupOfFacts:
    new_facts = []

    for fact in problem.facts:
        if isinstance(fact, Angle) and fact.angle == 90:
            p1, p2, p3 = fact.points
            s21 = problem.get_segment(p2, p1)
            s23 = problem.get_segment(p2, p3)
            s13 = problem.get_segment(p1, p3)

            # * hypot
            if not s13 and s21 and s23:
                hypot_len = np.hypot(s21.length, s23.length)
                new_facts.append(LineSegment((p1, p3), length=hypot_len))
            # * s21
            elif not s21 and s13 and s23:
                s21_len = np.sqrt(np.square(s13.length) - np.square(s23.length))
                new_facts.append(LineSegment((p2, p1), length=s21_len))
            # * s23
            elif not s23 and s21 and s13:
                s23_len = np.sqrt(np.square(s13.length) - np.square(s21.length))
                new_facts.append(LineSegment((p2, p3), length=s23_len))

    return new_facts


theorems = [pythagorean]
