#Exercise 7 kyu
#Regex validate pin code

#ATM machines allow 4 or 6 digit PIN codes
#and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

#If the function is passed a valid PIN string, return true, else return false.

#eg:

#validate_pin("1234") == True
#validate_pin("12345") == False
#validate_pin("a234") == False

def validate_pin(pin):
    if len (pin) ==4 or len(pin) ==6:
        for i in pin:
            if i not in "1234567890":
                return False
        return True
    return False
    #return len(pin) in (4, 6) and pin.isdigit()
#test cases
print (validate_pin("1")) #should return False
print(validate_pin("12")) #should return False
print(validate_pin("123")) #should return False
print(validate_pin("1234")) #should return True
print(validate_pin("12345")) #should return False
print(validate_pin("1234567")) #should return False
print(validate_pin("123456")) #should return True
print(validate_pin("-1234")) #should return False
print(validate_pin("1.234")) #should return False
print(validate_pin("-1.234")) #should return False
print(validate_pin("00000000")) #should return False
print(validate_pin("a234")) #should return False
print(validate_pin(".234")) #should return False
print(validate_pin("-123")) #should return False
print(validate_pin("-1.234")) #should return False