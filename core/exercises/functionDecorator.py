# write a program to demo function decorator

def decor(func):
    def wrapper():
        print
        a = 5
        b = func() + a
        return b

    return wrapper


@decor
def call_func():
    return 10


# without using @decor function
# return_val = decor(call_func)
# print(return_val())


# using @decor just printing call_function
print(call_func())
