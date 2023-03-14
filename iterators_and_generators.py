class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.x = 0

    def __iter__(self):
        return self

    def __next__(self):
        x = self.x
        if x > self.limit:
            raise StopIteration  # raise StopIteration exception when need to stop the iterator!
        self.x = x + 2
        return x


iter10 = MyIterator(10)
print(f"First I took this value: {next(iter10)}")
print(f"Second I took this value: {next(iter10)}")
for i in iter10:
    print(f"value generated: {i}")

# print(f"I am greedy and I want another value. {next(iter10)}")


def my_generator(limit):
    x = 0
    while x <= limit:
        yield x
        x += 10


generate100 = my_generator(100)
print(f"sneaking out an element: {next(generate100)}")
print(f"sneaking out another element: {next(generate100)}")
for i in generate100:
    print(i)

# print(f"I am greedy again: {next(generate100)}")

fruits = ["apple", "banana", "kiwi", "mango", "coconut", "durian", "cherry", "strawberry", "pear"]
import random

# let's create an infinite generator
def random_fruit():
    yield random.choice(fruits)


def infinite_fruits():
    while True:
        yield random.choice(fruits)


fruit_list = infinite_fruits()
for i in range(10):
    print(next(fruit_list))

