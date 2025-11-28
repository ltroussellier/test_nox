# test_func_311.py
import sys
import pytest
import importlib

# ----------------------------
# 3.11: Exception groups
# ----------------------------


def test_func_311():
    func_311_module = importlib.import_module("src.func_311")
    func_311 = func_311_module.func_311
    # With except*, both handlers execute, last one wins
    assert func_311() == "Caught TypeError"
