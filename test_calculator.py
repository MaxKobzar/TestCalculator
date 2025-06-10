import pytest
import allure
from calculator import Calculator


@allure.feature("Addition - EP")
def test_add_valid(valid_numbers):
    a, b = valid_numbers
    assert Calculator().add(a, b) == a + b


@allure.feature("Addition - BVA")
def test_add_boundary(boundary_numbers):
    a, b = boundary_numbers
    assert Calculator().add(a, b) == a + b


@allure.feature("Addition - Negative")
def test_add_invalid(invalid_numbers):
    a, b = invalid_numbers
    with pytest.raises(TypeError):
        Calculator().add(a, b)


@allure.feature("Subtraction - EP")
def test_subtract_valid(valid_numbers):
    a, b = valid_numbers
    assert Calculator().subtract(a, b) == a - b


@allure.feature("Subtraction - BVA")
def test_subtract_boundary(boundary_numbers):
    a, b = boundary_numbers
    assert Calculator().subtract(a, b) == a - b


@allure.feature("Subtraction - Negative")
def test_subtract_invalid(invalid_numbers):
    a, b = invalid_numbers
    with pytest.raises(TypeError):
        Calculator().subtract(a, b)


@allure.feature("Multiplication - EP")
def test_multiply_valid(valid_numbers):
    a, b = valid_numbers
    assert Calculator().multiply(a, b) == a * b


@allure.feature("Multiplication - BVA")
def test_multiply_boundary(boundary_numbers):
    a, b = boundary_numbers
    assert Calculator().multiply(a, b) == a * b


@allure.feature("Multiplication - Negative")
def test_multiply_invalid(invalid_numbers):
    a, b = invalid_numbers
    with pytest.raises(TypeError):
        Calculator().multiply(a, b)


@allure.feature("Division - EP")
def test_divide_valid(valid_numbers):
    a, b = valid_numbers
    if b == 0:
        with pytest.raises(ValueError):
            Calculator().divide(a, b)
    else:
        assert Calculator().divide(a, b) == a / b


@allure.feature("Division - EP")
def test_divide_boundary(boundary_numbers):
    a, b = boundary_numbers
    if b == 0:
        with pytest.raises(ValueError):
            Calculator().divide(a, b)
    else:
        assert Calculator().divide(a, b) == a / b


@allure.feature("Division - Negative")
def test_divide_invalid(invalid_numbers):
    a, b = invalid_numbers
    with pytest.raises(TypeError):
        Calculator().divide(a, b)
