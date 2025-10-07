from typing import Sequence, Optional
from .typedef import *
from .utils import log
from .theorems import theorems_list

import numpy as np


class Problem:
    def __init__(self, initial_facts: Sequence[MathObjectLike]) -> None:
        self.facts = list(initial_facts)
        self.line_segment_cache = {}

        from .math_objects import LineSegment

        print("established a problem with facts:")
        for fact in self.facts:
            if isinstance(fact, LineSegment):
                key = tuple(sorted(fact.points, key=lambda p: p.name))
                self.line_segment_cache[key] = fact
            print(fact)
        print("\n")

    def add_fact(self, fact: MathObjectLike) -> None:
        from .math_objects import LineSegment

        if fact not in self.facts:
            self.facts.append(fact)
            log(f"added new fact: {fact}.")

            ###
            ### Cache for instant look-ups
            ###

            if isinstance(fact, LineSegment):
                key = tuple(sorted(fact.points, key=lambda p: p.name))
                self.line_segment_cache[key] = fact

    ###
    ### GET
    ###

    def get_segment(self, p1: PointLike, p2: PointLike) -> Optional[LineSegmentLike]:
        key = tuple(sorted((p1, p2), key=lambda p: p.name))
        return self.line_segment_cache[key] if key in self.line_segment_cache else None


class Deducer:
    def __init__(self, problem: ProblemLike) -> None:
        self.problem = problem

    def deduce(self):
        log("deducing facts.")
        problem = self.problem
        facts_count = len(self.problem.facts)

        while True:
            for theorem in theorems_list:
                theorem(problem)

            if len(self.problem.facts) == facts_count:
                log("deduction terminated: no new facts can be deduced.")
                break

            facts_count = len(self.problem.facts)
