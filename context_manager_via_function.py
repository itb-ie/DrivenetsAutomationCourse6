from contextlib import contextmanager


# 1st case, simplest way
@contextmanager
def my_context():
    # all the code above yield is called the setup phase and is called when entering the context!!
    print("Entering my context code")
    yield  # this is a fancier way of saying return

    # all the code below the yield is called the teardown phase and will be called when exiting the context!!
    print("Exiting my context code")


# we work with context managers via the keyword: with <name_of_context_manager>
with my_context():
    print("     Now I am inside the context manager")
    print("     It is quite cozy in here")


def hello_world():
    import random
    print("hello world function")
    return random.randint(1, 10)

# 2nd case, yield with a value
@contextmanager
def my_context2():
    # all the code above yield is called the setup phase and is called when entering the context!!
    print("Entering my context2 code")
    yield hello_world()  # yield can also return(yield) a value!

    # all the code below the yield is called the teardown phase and will be called when exiting the context!!
    print("Exiting my context2 code")


# we work with context managers via the keyword: with <name_of_context_manager>
with my_context2() as value:
    print("     Now I am inside the context manager")
    print(f"     It is quite cozy in here, about a {value} level of coziness")
