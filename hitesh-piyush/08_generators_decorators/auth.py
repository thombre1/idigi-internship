from functools import wraps
def my_auth(func):
    @wraps(func)
    def wrapper(user):
        
        if(user!="admin"):
            print("Access denied")
            return None
        else:
            print("Access Granted")
            return func(user)
    return wrapper


@my_auth
def auth(role):
    print(f"{role} can access inventory")

auth("user")
auth("admin")
