# explicitly check the return types in all of your functions
# and make sure they're returning what you expect. To do that,
# you are going to create a decorator that checks
# if the return type of the decorated function is correct


def returns_dict(func):
    # Complete the returns_dict() decorator
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        assert type(result) == dict
        return result

    return wrapper


@returns_dict
def test_func(value):
    return value


try:
    print(test_func([1, 2, 3]))
except AssertionError:
    print('test_func() did not return a dict!')

# decorator that take expected return type as argument


def returns(return_type):
    # Complete the returns() decorator
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            assert type(result) == return_type
            return result

        return wrapper

    return decorator


@returns(dict)
def test_func(value):
    return value


try:
    print(test_func([1, 2, 3]))
except AssertionError:
    print('test_func() did not return a dict!')
