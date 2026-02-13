def my_decorator(func):

    # we need to decorate the wrapper function with @wrap
    # that way fucntion what we passed 'func'
    # preserves its metadata
    @wrap(func)
    def my_wrapper():
        print("Before the func runs")
        func()
        print("After the func runs")
    
    # common practice to return a wrapper
    return my_wrapper


@my_decorator
def greeting():
    print("Hello World!")

# Right at the start because only the line bellow the decorator is considered for the decorator
# 😖
print("Where will this line print")
greeting()
