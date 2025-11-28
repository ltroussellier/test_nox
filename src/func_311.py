# func_311.py
# --- 3.11 feature: Exception groups


def func_311():
    # Works in 3.11+, fails in 3.10-
    result = "No match"
    try:
        raise ExceptionGroup("Multiple errors", [ValueError("v"), TypeError("t")])
    except* ValueError as e:
        result = "Caught ValueError"
    except* TypeError as e:
        result = "Caught TypeError"

    return result
