#this one is like yourt scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# ok, that is actually pointless, we can just do this

def print_two_again(arg1, arg2):
    print(f"arg1 {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1 : {arg1}")

# this just takes no arguments
def print_none():
    print("T got nothin'.")


print_two("tri","gunawan")
print_two_again("tri","gunawan")
print_one("tri")
print_none

