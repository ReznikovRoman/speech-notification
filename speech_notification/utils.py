from colorama import Fore


def handle_user_input_int(input_field: str, input_msg: str = None) -> int:
    """
    Handles user input (which should be converted to int)

    Args:
        input_field (str): Name of the input field
        input_msg (str): Help message

    Returns:
        int: User input (converted to int)
    """
    while True:
        try:
            user_input = int(input(input_msg))
        except ValueError as ve:
            print(Fore.RED + f'Error! {input_field} must be int.')
        else:
            return user_input


def handle_user_input_bool(input_field: str, input_msg: str):
    user_input = input(input_msg)
    if user_input not in ('0', 'n', 'N'):
        return True
    else:
        return False


def convert_minutes_to_seconds(time_in_minutes: int) -> int:
    """
    Converts time in minutes to time in seconds

    Args:
        time_in_minutes (int): Time in minutes (that must be converted to seconds)

    Returns:
        int: Time in seconds
    """
    if isinstance(time_in_minutes, int):
        return time_in_minutes * 60
    else:
        print(Fore.RED + "Error! Time must be int.")












