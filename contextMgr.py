# A context manager is an object that defines the methods __enter__ and
# __exit__ to control what happens when entering and exiting a with block.
# The most common use case is file handling.
# Python’s built-in open() function returns a context manager

class MyContextMgr:
    def __enter__(self):
        print("Entering the context")
        return self  # The value returned is bound to the 'as' variable
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        # Handle exceptions if needed
        return False  # False propagates exceptions; True suppresses them

with MyContextMgr() as cm:
    print("Inside the context")