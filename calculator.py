import functools


class Calculator:

    def check_output_type(func):
        @functools.wraps(func)
        def wrap(self, *args, **kwargs):
            ret = func(self, *args, **kwargs)
            if not (isinstance(ret, int) or isinstance(ret, float) or isinstance(ret, complex)):
                raise TypeError
            return ret

        return wrap

    @check_output_type
    def add(self, a, b):
        ret = a + b
        return ret

    @check_output_type
    def subtract(self, a, b):
        ret = a - b
        return ret

    @check_output_type
    def multiply(self, a, b):
        ret = a * b
        return ret

    @check_output_type
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        ret = a / b
        return ret
