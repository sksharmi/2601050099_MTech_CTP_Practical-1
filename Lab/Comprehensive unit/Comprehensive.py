import pytest
from hypothesis import given, strategies as st

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Unit Test
def test_add():
    assert add(2, 3) == 5

# Unit Test
def test_multiply():
    assert multiply(2, 3) == 6

# Hypothesis Test
@given(st.integers(), st.integers())
def test_hypothesis(a, b):
    assert add(a, b) == a + b

# Run tests directly
if __name__ == "__main__":
    test_add()
    test_multiply()
    test_hypothesis()
    print("All tests passed!")