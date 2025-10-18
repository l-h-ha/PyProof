from . import GroupOfFacts


def tokenize_facts(facts: GroupOfFacts) -> set[tuple[str]]:
    tokens = set()
    for fact in facts:
        tokens.add(fact.tokenize())
    return tokens
