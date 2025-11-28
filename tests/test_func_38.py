# test_func_38.py
import sys
import pytest
import importlib

# ----------------------------
# 3.8: Walrus operator
# ----------------------------


def test_func_38():
    func_38_module = importlib.import_module("src.func_38")
    func_38 = func_38_module.func_38
    assert func_38() == 5
