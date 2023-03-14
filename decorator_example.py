def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("I am adding the chocolate on top")
        func(*args, **kwargs)
        print("I am cleaning the plate")

    return wrapper  # not!! wrapper()


@my_decorator
def cake(name="Bogdan", surname="Ratiu"):
    print(f"I am eating the cake for {name} {surname}")


# cake = my_decorator(cake)
# cake(surname="Obama")

cake()




