# test_func_39.py
import sys
import pytest
import importlib

# ----------------------------
# 3.9: dict union operator
# ----------------------------


def test_func_39():
    func_39_module = importlib.import_module("src.func_39")
    func_39 = func_39_module.func_39
    assert func_39() == {"a": 1, "b": 2}
