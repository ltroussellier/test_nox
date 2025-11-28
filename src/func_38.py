# func_38.py
# --- 3.8 feature: Walrus operator
def func_38():
    # Works in 3.8+, fails in 3.7-
    if (n := len("hello")) > 3:
        return n
    return 0
