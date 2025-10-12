from ..geometry.mathobjs import Problem
from ..geometry.theorems import theorems
from ..utils import GroupOfFacts, log
from .. import _config


def deduce(problem: Problem, extend: bool = False) -> GroupOfFacts:
    if _config.logging:
        log("deducing problem.", seperate=True, dist=2)

    new_facts = set()
    last_new_fact_count = 0

    while True:
        for theorem in theorems:
            theorem_new_facts = theorem(problem)
            new_facts.update(theorem_new_facts)

        nfl = len(new_facts)
        if nfl == last_new_fact_count:
            log("terminating deduction: cannot deduce anymore facts.")
            log(f"deduced {nfl} facts.")
            break

        last_new_fact_count = nfl

    if extend:
        log("appending facts to facts buffer.")
        for fact in new_facts:
            problem.add_fact(fact)
    return new_facts
