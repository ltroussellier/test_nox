# test_func_312.py
import sys
import pytest
import importlib

# ----------------------------
# 3.12: PEP 692 – Using TypedDict for **kwargs typing
# ----------------------------


def test_func_312():
    func_312_module = importlib.import_module("src.func_312")
    func_312 = func_312_module.func_312
    result = func_312()
    assert result["name"] == "Alice"
    assert result["age"] == 30
