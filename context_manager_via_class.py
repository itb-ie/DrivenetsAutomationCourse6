import traceback
import io


class MyContext:
    def __init__(self, filename):
        self.context = filename
        self.fp = None

    def __enter__(self):
        # this includes only the setup code!
        # instead of yield like function, we use return!!
        try:
            self.fp = open(self.context, 'r')
            return self.fp.read()
        except UnicodeDecodeError:
            print("Please make sure to give me a text file!")
            return ""
        except FileNotFoundError:
            print("Please make sure that the file exists!")
            return ""

    def __exit__(self, exc_type, exc_val, exc_tb):
        # this is how to check for an exception inside the body of the context manager!
        print("we are running the __exit__")
        if exc_type:
            print(f"During the body the following exception occurred: {exc_type}")
            print(f"The value is {exc_val}")
            print(f"The traceback is:")
            output = io.StringIO()  # create a in-memory buffer to write to
            traceback.print_tb(exc_tb, file=output)
            traceback_text_no_red = output.getvalue()
            print(traceback_text_no_red)
        if self.fp:
            self.fp.close()
        return True  # True masks the exceptions from the body, False will raise them!!


c = MyContext("context_manager_example.py")
with c as content:
    for idx, line in enumerate(content.splitlines()):  # enumerate returns (idx, content) as a tuple that I unpack
        print(f"{idx+1}: {line}")
        # import jamesjames
