# My Attempt


#Initially, kettle will not be boiled
kettle_boiled = False
notification_sent = False

def check_and_notify_user(kettle_boiled):
    if(kettle_boiled == True):
        print("Kettle done! Time to make chai!")
        return True
    return False

while(notification_sent==False):
    notification_sent = check_and_notify_user(kettle_boiled)
    

