def log(msg: str, seperate: bool = False, dist: int = 1) -> None:
    print(f"{"\n"*dist if seperate else ""}[LOG]: {msg}")
