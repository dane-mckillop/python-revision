import time
from functools import wraps

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # High-resolution timer
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.6f} seconds to execute")
        return result
    return wrapper

# Example usage:
@measure_time
def deep_loop(depth):
    """Creates nested loops to the specified depth, each iterating 1000 times."""
    def nested_loop(current_depth):
        if current_depth == 0:
            return 1
        total = 0
        for _ in range(10*current_depth):  
            total += nested_loop(current_depth - 1)
        return total
    return nested_loop(depth)

if __name__ == "__main__":
    # DO NOT LOOP DEEPER THAN 5 TIMES
    for d in range(1, 6): 
        print(f"\nTesting depth {d}:")
        result = deep_loop(d)
        print(f"Result: {result}")