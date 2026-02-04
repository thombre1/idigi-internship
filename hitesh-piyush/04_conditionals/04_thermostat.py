device_status = input("Enter device status(Active/Inactive): ")

if(device_status.lower() == "active"):
    device_status = True
    tempreature = int(input("What's the temp: "))
    if(tempreature>35):
        print("High Tempreature Alert!")
    else:
        print("Temp Normal")
else:
    device_status = False
    print("Device is Offline...")


