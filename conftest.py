import pytest
import sys

MAX_INT = sys.maxsize
MIN_INT = -sys.maxsize - 1


# --- Fixtures for Equivalence Partitioning ---
@pytest.fixture(params=[
    (5, 3),  # valid ints
    (2.5, 1.5),  # valid floats
    (-3, -7),  # valid negative numbers
    (0, 0),  # valid zero input
])
def valid_numbers(request):
    return request.param


@pytest.fixture(params=[
    ('a', 3),
    (None, 5),
    ([], {}),
    (3, "b"),
])
def invalid_numbers(request):
    return request.param


# --- Fixtures for Boundary Value Analysis ---
@pytest.fixture(params=[
    (0, 1),
    (1, 0),
    (-1, 1),
    (MAX_INT, 1),
    (MIN_INT, -1),
    (1e-10, 2e-10),
])
def boundary_numbers(request):
    return request.param
