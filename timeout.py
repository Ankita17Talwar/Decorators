# Timeout decorator : for functions running longer

import signal
from functools import wraps
import time


def raise_timeout(*args, **kwargs):
    raise TimeoutError()


# when an "alarm" signal goes off , call raise_timeout()
signal.signal(__signalnum=signal.SIGALRM, __handler=raise_timeout())


def timeout_in_5s(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Set off an alarm in 5 seconds
        signal.alarm(5)
        try:
            # call decorated function
            return func(*args, **kwargs)
        finally:
            # cancel the alarm
            signal.alarm(0)

    return wrapper


@timeout_in_5s
def test():
    time.sleep(10)
    print('test')


def timeout(n_seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Set off an alarm in 5 seconds
            signal.alarm(n_seconds)
            try:
                # call decorated function
                return func(*args, **kwargs)
            finally:
                # cancel the alarm
                signal.alarm(0)

        return wrapper
    return decorator()


@timeout(5)
def test():
    time.sleep(10)
    print('test')