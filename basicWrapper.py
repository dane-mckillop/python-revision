# Decorator: A function that takes another function, adds or changes its 
# behavior, and returns a new function. Applied using @decorator_name above 
# a function.
#
# Wrapper: The new function returned by a decorator. It runs extra code 
# before or after calling the original function, handling its arguments and 
# return value.
#
# Applied using @decorator above a function definition.
# 
# Decorators preserve the original function’s metadata (e.g., name, docstring) 
# using tools like functools.wraps.
#
# Variable-Length Arguments (*args, **kwargs):
# Use *args for variable positional arguments and **kwargs for variable 
# keyword arguments to support flexible argument counts.

import logging
import time

def my_decorator(func):
    def wrapper():
        print("Something before")
        func()
        print("Something after")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
    
# Common decorators for Python functions:
# Logging, admin checks, timing, and argument validation.

def log(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

def requires_admin(func):
    def wrapper(user, *args, **kwargs):
        if user.is_admin:
            return func(user, *args, **kwargs)
        raise PermissionError("Admin access required")
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.2f} seconds")
        return result
    return wrapper

def positive_args(func):
    def wrapper(*args):
        if any(x <= 0 for x in args):
            raise ValueError("All arguments must be positive")
        return func(*args)
    return wrapper

if __name__ == "__main__":
    # Example usage of the decorator
    say_hello()  # Output: Something before, Hello!, Something after

    # Example of logging decorator
    @log
    def add(a, b):
        return a + b

    add(2, 3)  # Logs the call and result

    # Example of requires_admin decorator
    class User:
        def __init__(self, is_admin):
            self.is_admin = is_admin

    @requires_admin
    def admin_task(user):
        return "Admin task completed"

    user = User(is_admin=True)
    print(admin_task(user))  # Output: Admin task completed