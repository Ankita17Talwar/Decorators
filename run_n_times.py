

def run_n_times(n):
    """Define and return a decorator"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


# Make print_sum() run 10 times with the run_n_times() decorator
@run_n_times(10)  # run_n_times = run_n_times(10) ; then calling with @run_n_times
def print_sum(a, b):
    print(a + b)

# call print_sum
print_sum(15, 20)


# output print 35 (i.e. 15+20) 10 times
