from functools import wraps
from inspect import signature

def strict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        

        func_sig = signature(func)

        bound_args = func_sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        

        for param, value in bound_args.arguments.items():
            expected_type = annotations.get(param)
            if expected_type and not isinstance(value, expected_type):
                raise TypeError(
                    f"Argument '{param}' must be of type {expected_type.__name__}, "
                    f"but got {type(value).__name__} instead."
                )

        return func(*args, **kwargs)
    
    return wrapper


@strict
def example_function(a: int, b: float, c: str):
    print(f"a: {a}, b: {b}, c: {c}")








