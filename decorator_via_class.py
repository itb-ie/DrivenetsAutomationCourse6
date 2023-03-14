# for a decorator via class we need to define the __call__ (it makes it a callable)

import random


class Repeat:
    total_calls = 0  # this can only be done via class!!

    def __init__(self, num_times, do_debug=True):
        self.num_times = num_times
        self.do_debug = do_debug
        self.num_calls = 0

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(self.num_times):
                try:
                    self.num_calls += 1
                    Repeat.total_calls += 1
                    result = func(*args, **kwargs)
                except Exception as e:
                    print(f"I managed to reproduce the problem after {self.num_calls} tries!!")
                    if self.do_debug:
                        print(f"the problem values were: {e.__traceback__.tb_next.tb_frame.f_locals}")
                    # print(f"Total number of calls so far: {self.total_calls}")
                    break
            return result
        return wrapper




@Repeat(10**5)
def problem_code():
    a = random.randint(1, 10**6)
    b = random.randint(0, 10**4)
    return a/b

@Repeat(10**5)
def problem_code2():
    a = random.randint(1, 10**6)
    b = random.randint(0, 10**4)
    return a/b

@Repeat(10**5)
def problem_code3():
    a = random.randint(1, 10**6)
    b = 0
    return a/b



problem_code()
problem_code2()
problem_code3()

print(f"Total calls {Repeat.total_calls}")
