import time
import random

def retry(max_attempts, delay=1):
    """Decorates a function to retry it on failure up to a specified number of attempts.

    The decorator retries the function if it raises an exception, waiting for a specified
    delay between attempts. If all attempts fail, the last exception is re-raised.

    Args:
        max_attempts (int): The maximum number of attempts to execute the function.
        delay (float, optional): The delay in seconds between retry attempts. Defaults to 1.

    Returns:
        callable: A decorator function that wraps the target function with retry logic.

    Example:
        @retry(max_attempts=3, delay=2)
        def flaky_function():
            # Some code that might fail
            pass
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            error_count = 0
            for attempt in range(max_attempts):
                try:
                    func_result = func(*args, **kwargs)
                    print(f"Total retry attempts triggered: {error_count}")
                    return func_result
                except Exception:
                    error_count += 1
                    if attempt == max_attempts - 1:
                        print(f"Total retry attempts triggered: {error_count}")
                        raise
                    time.sleep(delay)  # Backoff
        return wrapper
    return decorator

def simple_retry(func):
    """Less nested version of the retry decorator.
    
    Retries a function up to 3 times with a 1-second delay."""
    def wrapper(*args, **kwargs):
        delay = random.uniform(0.5, 1.5)  # Random delay between 0.5 and 1.5 seconds
        max_attempts = 4
        error_count = 0
        if 'max_attempts' in kwargs:
            max_attempts = kwargs.pop('max_attempts')
        for attempt in range(max_attempts):
            try:
                result = func(*args, **kwargs)
                print(f"Total retry attempts triggered: {error_count}")
                return result
            except Exception:
                error_count += 1
                if attempt == max_attempts - 1:
                    print(f"Total retry attempts triggered: {error_count}")
                    raise
                time.sleep(delay)
    return wrapper

if __name__ == "__main__":
    # Example usage of the retry decorator
    # Order of wrapping matters: retry should be applied before error_counter
    @retry(max_attempts=4, delay=2)
    def flaky_function():
        if random.choice([True, False]):
            raise ValueError("Random failure")
        return "Success"

    try:
        RESULT = flaky_function()
        print(RESULT)
    except Exception as e:
        print(f"Function failed after retries: {e}")
    
    # Example usage of simple_retry
    # Again, order of wrapping matters
    @simple_retry
    def another_flaky_function():
        if random.choice([True, False]):
            raise ValueError("Another random failure")
        return "Another Success"

    try:
        ANOTHER_RESULT = another_flaky_function()
        print(ANOTHER_RESULT)
    except Exception as e:
        print(f"Function failed after retries: {e}")