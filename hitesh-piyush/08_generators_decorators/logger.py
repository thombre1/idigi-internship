# I still dont know why or where will I use decorators but i got a brief structural outline
# make a function , then write a wrapper after @wraps(func)
# the wrapper will execute the func() that is passed in the main decorator
# wherever it is called inside the wrapper
# write a decorator that will tell that the func argument you need
# take that from the line below me

# Yup thats what i got to know, till now

from functools import wraps
def my_logger(func):

    #preserve metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} is processing")
        result = func(*args, **kwargs)
        print(f"{func.__name__} is finished ✅")
        return result
    return wrapper

@my_logger
def chai_type(chai, milk="NO"):
    print(f"{chai} is brewing. Milk: {milk}")

chai_type("Ginger tea")
