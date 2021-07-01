#exercise_2
#program with Decorator
def divid(func):
    def wrapper (a,b):
        if a > 0 and b > 0 :
            func(a,b)
        else:
            raise ValueError
    return wrapper


@divid
def div(a,b):
    print(f"{a}/{b} = {a/b}")

# Example
# div(10,2)