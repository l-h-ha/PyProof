from .typedef import ProblemLike
from .utils import log

import numpy as np


def apply_pythagorean(problem: ProblemLike) -> None:
    from .math_objects import Angle, LineSegment

    log("applying Pythagorean theorem.")

    for fact in problem.facts:
        if isinstance(fact, Angle) and fact.degrees == 90:
            p1, vertex, p3 = fact.points
            s1 = problem.get_segment(p1, vertex)
            s2 = problem.get_segment(vertex, p3)

            # deriving hyp
            hyp = problem.get_segment(p1, p3)
            if not hyp and s1 and s2:
                hyp_len = np.hypot(s1.length, s2.length)
                new_fact = LineSegment((p1, p3), length=hyp_len)
                problem.add_fact(new_fact)
                return

            # deriving s1
            elif not s1 and hyp and s2:
                if hyp.length > s2.length:
                    s2_len = np.sqrt(np.square(hyp.length) - np.square(s2.length))
                    problem.add_fact(LineSegment((p1, vertex), length=s2_len))
                    return

            # deriving s2
            elif not s2 and hyp and s1:
                if hyp.length > s1.length:
                    s1_len = np.sqrt(np.square(hyp.length) - np.square(s1.length))
                    problem.add_fact(LineSegment((p3, vertex), length=s1_len))
                    return


theorems_list = [apply_pythagorean]
