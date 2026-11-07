"""Program 52: Decorators"""

from functools import wraps

def show_message(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Function is starting...")
        result = function(*args, **kwargs)
        print("Function has finished.")
        return result
    return wrapper

@show_message
def greet(name):
    print(f"Hello, {name}!")

greet("Python Learner")
