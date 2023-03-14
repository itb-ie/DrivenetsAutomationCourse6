#  suppose there is a bug in some code that is intermittent

import random


def repeat(num_times, do_debug=False):  # notice that there is an extra level
    def repeat_decorator(func):
        def wrapper(*args, **kwargs):
            result = 0
            for _ in range(num_times):
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    print("I managed to reproduce the problem!!")
                    if do_debug:
                        print(f"the problem values were: {e.__traceback__.tb_next.tb_frame.f_locals}")
                    break
            return result
        return wrapper
    return repeat_decorator


@repeat(10**5, do_debug=True)
def problem_code():
    a = random.randint(1, 10**6)
    b = random.randint(0, 10**4)
    return a/b


problem_code()
