from src.pyproof.geometry.mathobjs import Problem
from src.pyproof.geometry.theorems import theorems
from src.pyproof.utils import log, tokenize_facts

MAX_DEPTH = 10


def datagen_helper(
    problem: Problem,
    tokenize: bool,
    logging: bool,
    generated_data: set,
    total_facts: set,
    visited_states: set,
    depth: int,
) -> None:
    if depth > MAX_DEPTH:
        if logging:
            log(f"generation termination: max depth reached: {MAX_DEPTH}")
        return

    if logging:
        log(
            f"generating synthetic data: MAX_DEPTH={MAX_DEPTH}, DEPTH={depth}",
            seperate=True,
            dist=2,
        )

    if tokenize:
        premise = tuple(tokenize_facts(problem.facts))
    else:
        premise = tuple(problem.facts)

    for i, theorem in enumerate(theorems):
        deduced_facts = theorem(problem)
        deduced_facts.difference_update(total_facts)

        if deduced_facts:
            sample = (premise, i)

            generated_data.add(sample)
            total_facts.update(deduced_facts)

            next_problem = Problem(problem.facts.union(deduced_facts))
            datagen_helper(
                next_problem,
                tokenize=tokenize,
                logging=logging,
                generated_data=generated_data,
                total_facts=total_facts,
                visited_states=visited_states,
                depth=depth + 1,
            )


def generate_data_from_problem(
    problem: Problem,
    tokenize: bool = True,
    logging: bool = False,
) -> set:
    generated_data = set()
    total_facts = set(problem.facts)
    visited_states = set()

    datagen_helper(
        problem,
        tokenize=tokenize,
        logging=logging,
        generated_data=generated_data,
        total_facts=total_facts,
        visited_states=visited_states,
        depth=0,
    )

    if logging:
        log(
            "synthetic data generation end: exhausted maximum depth search or unable to derive anymore states."
        )
    return generated_data
