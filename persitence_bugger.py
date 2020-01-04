#Exercise 6 kyu 
#Persistence bugger
#Write a function, persistence, that takes in a positive parameter num
#and returns its multiplicative persistence, which is the number of times
#you must multiply the digits in num until you reach a single digit.

#For example:
 #persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 #persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 #persistence(4) => 0   # Because 4 is already a one-digit number.

#For example:
#persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

#persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

#persistence(4) # returns 0, because 4 is already a one-digit number
 
 
import functools
def persistence(n):
    aux1 = str(n)
    if len(aux1) == 1:
        return 0
    else:
        cont= 0
        while (len(aux1) > 1):
            aux1 = str(functools.reduce(lambda x, y: int(x) * int(y), aux1)) 
            cont += 1
        return cont
#test cases
print(persistence(39)) #should equals 3
print(persistence(4)) #should equals 0
print(persistence(25)) #should equals 2
print(persistence(999)) #shoul equals 4