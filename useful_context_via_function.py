from contextlib import contextmanager

# i want to create a context manager that gets the content of a file. but with added protection

@contextmanager
def get_contents_of_file(filename):
    # lets make it better
    f = None
    try:
        f = open(filename, 'r')
        yield f.read()
    except FileNotFoundError:
        print("Hello: please give me a file that exists!!")
        try:
            yield None
        except Exception as e:
            print(f"Something bad happened! {e}")
    except UnicodeDecodeError:
        print("please make sure to give me a text file!")
        yield ""

    finally:
        if f:
            f.close()


with get_contents_of_file("useful_context_via_function.py") as content:
    for idx, line in enumerate(content.splitlines()):  # enumerate returns (idx, content) as a tuple that I unpack
        print(f"{idx+1}: {line}")

