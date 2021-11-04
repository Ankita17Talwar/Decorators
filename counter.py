# how many times each of the functions in it gets called
from functools import wraps


def counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # Call the function being decorated and return the result
        return func

    wrapper.count = 0
    # Return the new decorated function
    return wrapper


# Decorate foo() with the counter() decorator
@counter
def foo():
    """
    Function Foo
    """
    print('calling foo()')


foo()
foo()

print('foo() was called {} times.'.format(foo.count))
print(foo.__doc__)
