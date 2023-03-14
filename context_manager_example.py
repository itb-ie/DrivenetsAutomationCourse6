# a short example of a context manager

# working with files:

# f = open("text.txt", "a")  # function call
#
# text = input("What do you want to put in the file? ")
# f.write(f"{text}\n")
#
# f.close()


# the same code, can be written using an existing context manager

with open("text.txt", "a") as f:  # context manager
    # here is the code inside the context manager
    text = input("What do you want to put in the file? ")
    f.write(f"{text}\n")


