from functools import wraps
from typing import Callable
from colorama import Fore


#######################################################################################################################


def set_range(lower_boundary: int, upper_boundary: int, field_name: str):
    """
    Decorator that sets range to a variable

    Args:
        lower_boundary (int): Lower boundary
        upper_boundary (int): Upper boundary
        field_name (str): Field name (to which the range is set)

    Returns:
        Callable
    """

    def decorator_range(func):
        @wraps(func)
        def wrapper_range(*args, **kwargs) -> int:
            while True:
                try:
                    user_time = func(*args, **kwargs)
                    if user_time not in range(int(lower_boundary), int(upper_boundary)):
                        raise ValueError
                except ValueError as ve:
                    print(Fore.RED + f'Error! {field_name} must be in range [{lower_boundary}, {upper_boundary}].')
                else:
                    return user_time
        return wrapper_range

    return decorator_range


