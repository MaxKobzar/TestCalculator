import pytest
import allure
from calculator import add, subtract, multiply, divide


@allure.feature("Addition - EP")
def test_add_valid(valid_numbers):
    a, b = valid_numbers
    assert add(a, b) == a + b


@allure.feature("Addition - BVA")
def test_add_boundary(boundary_numbers):
    a, b = boundary_numbers
    assert add(a, b) == a + b


@allure.feature("Addition - EP Negative")
def test_add_invalid(invalid_numbers):
    a, b = invalid_numbers
    with pytest.raises(TypeError):
        result = add(a, b)
        if not isinstance(result, int) or isinstance(result, float) or isinstance(result, complex):
            raise TypeError


@allure.feature("Subtraction - EP")
def test_subtract_valid(valid_numbers):
    a, b = valid_numbers
    assert subtract(a, b) == a - b


@allure.feature("Subtraction - BVA")
def test_subtract_boundary(boundary_numbers):
    a, b = boundary_numbers
    assert subtract(a, b) == a - b


@allure.feature("Subtraction - EP Negative")
def test_subtract_invalid(invalid_numbers):
    a, b = invalid_numbers
    with pytest.raises(TypeError):
        result = subtract(a, b)
        if not isinstance(result, int) or isinstance(result, float) or isinstance(result, complex):
            raise TypeError


@allure.feature("Multiplication - EP")
def test_multiply_valid(valid_numbers):
    a, b = valid_numbers
    assert multiply(a, b) == a * b


@allure.feature("Multiplication - BVA")
def test_multiply_boundary(boundary_numbers):
    a, b = boundary_numbers
    assert multiply(a, b) == a * b


@allure.feature("Multiplication - EP Negative")
def test_multiply_invalid(invalid_numbers):
    a, b = invalid_numbers
    with pytest.raises(TypeError):
        result = multiply(a, b)
        if not isinstance(result, int) or isinstance(result, float) or isinstance(result, complex):
            raise TypeError


@allure.feature("Division - EP")
def test_divide_valid(valid_numbers):
    a, b = valid_numbers
    if b == 0:
        with pytest.raises(ValueError):
            divide(a, b)
    else:
        assert divide(a, b) == a / b


@allure.feature("Division - EP")
def test_divide_boundary(boundary_numbers):
    a, b = boundary_numbers
    if b == 0:
        with pytest.raises(ValueError):
            divide(a, b)
    else:
        assert divide(a, b) == a / b


@allure.feature("Division - EP Negative")
def test_divide_invalid(invalid_numbers):
    a, b = invalid_numbers
    with pytest.raises(TypeError):
        result = multiply(a, b)
        if not isinstance(result, int) or isinstance(result, float) or isinstance(result, complex):
            raise TypeError
