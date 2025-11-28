# func_39.py
# --- 3.9 feature: dict union operator


def func_39():
    # Works in 3.9+, fails in 3.8-
    d1 = {"a": 1}
    d2 = {"b": 2}
    d3 = d1 | d2  # dict union
    return d3
