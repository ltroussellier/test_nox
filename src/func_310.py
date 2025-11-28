# func_310.py
# --- 3.10 feature: structural pattern matching


def func_310(value):
    # Works in 3.10+, fails in 3.9-
    match value:
        case 0:
            return "zero"
        case 1 | 2:
            return "one or two"
        case _:
            return "other"
