# test_func_310.py
import sys
import pytest
import importlib

# ----------------------------
# 3.10: structural pattern matching
# ----------------------------


@pytest.mark.parametrize(
    "value,expected", [(0, "zero"), (1, "one or two"), (2, "one or two"), (99, "other")]
)
def test_func_310(value, expected):
    func_310_module = importlib.import_module("src.func_310")
    func_310 = func_310_module.func_310
    assert func_310(value) == expected
