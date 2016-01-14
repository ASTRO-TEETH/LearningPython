#Password Checker
print("Welcome to PGO Security Systems")
print("*******************************")
password = input("Enter your password: ")

if password == "everything is awesome":
    print("You are awesome")
else:
    print("Stop getting it wrong!")

print("Press ENTER to exit the program")

#accept the driver's speed

print("What is the driver's speed?")
speed = int(input("Enter the driver's speed here"))

#if and else statement in use

if speed >= 75:
    print ("Issue ticket")
elif speed >=70:
    print ("Issue warning")
else:
    print ("Issue fine")
