# test_func_313_plus.py
import sys
import pytest
import importlib

# ----------------------------
# 3.13+: future feature simulation
# ----------------------------


def test_func_313_plus():
    func_313_plus_module = importlib.import_module("src.func_313_plus")
    func_313_plus = func_313_plus_module.func_313_plus
    # Only succeed on Python 3.13+, fail on earlier versions
    result = func_313_plus()
    assert "Value: 42" in result
    assert "List: [1, 2, 3]" in result
