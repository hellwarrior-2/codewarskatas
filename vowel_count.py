#Exercise 7 kyu
#Vowel count
#Return the number (count) of vowels in the given string.

#We will consider a, e, i, o, and u as vowels for this Kata.

#The input string will only consist of lower case letters and/or spaces.

def getCount(inputStr):
    return sum(1 for i in inputStr.lower() if i in "aeiou")    
#test cases
print (getCount("abracadabra")) #should print 5
print (getCount ("murcielago volador")) #should print 8