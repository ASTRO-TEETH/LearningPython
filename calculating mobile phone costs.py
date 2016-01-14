#*mobile phone costs*

#accept user name and mobile phone network
print ("What is your name?")
name = input()
print ("What is your mobile phone network?")
network = input()

#number of minutes they have used the phone *0.10 per minute

minutes = int(input("How many minutes have you used this month?"))
totalminutes = minutes *0.10
print (totalminutes)

#number of texts they have sent *0.05 pence per text

texts = int(input("How many texts have you sent this month?"))
totaltexts = texts *0.05
print (totaltexts)

#displays the whole bill without VAT

bill = totalminutes+totaltexts
print ("You have to pay",totalminutes+totaltexts ,"without the 20% added VAT")

#displays the whole bill with VAT of 20%

vat_bill = bill /100 *20 +bill

print ("You have to pay" , vat_bill, "which includes the overall VAT amount")




