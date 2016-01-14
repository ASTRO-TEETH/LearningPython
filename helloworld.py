#imports the time to use as a timer below in executable script
import time

#print example, print is a function

print ("My name is Dhiresh and everything is awesome")

#firstname is a variable

time.sleep(1)
print ("What is your name?")
firstname = input()
print ("Hello", firstname)

#surname is a variable

time.sleep(1)
print ("What is your surname?")
surname = input()
print("Hello",firstname ,surname)

#Initials

time.sleep(1)
print ("Your initials are:", firstname[0], surname[0])

#firstname+surname

time.sleep(1)
fullname = firstname +" "+ surname
print (fullname.upper())


#.upper() intergrated with fullname output

time.sleep(1)
print("Hello",firstname.upper() ,surname.upper())

#Amount of characters in fullname

time.sleep(1)
print (len(fullname))

#Length of a list

time.sleep(1)
colours = ("red", "yellow", "orange", "green", "blue", "purple")
print (len(colours))

#Adding numbers from input of the user

a = input('Enter A Number')
b = input('Now Enter Another Number')
sum = a+b
print(sum)
sum = int(a) + int(b)


