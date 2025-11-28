# func_312.py
# --- 3.12 feature: PEP 695 – Type Parameter Syntax

# type statement is new in Python 3.12
type Point = tuple[float, float]


def func_312() -> dict[str, str | int]:
    # Works in 3.12+, fails in 3.11-
    # Using the new type alias syntax
    p: Point = (1.5, 2.5)

    return {"name": "Alice", "age": 30, "point": p}
