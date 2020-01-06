#Exercise 6 kyu 
#String to camel case

#Complete the method/function so that it converts 
#dash/underscore delimited words into camel casing. 
#The first word within the output should be capitalized 
#only if the original word was capitalized 
#(known as Upper Camel Case, also often referred to as Pascal case).

#Examples
#to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

#to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

import re
def to_camel_case(text):
    aux = re.sub("-|_", " ", text).split()
    return ''.join([i.capitalize() if aux.index(i)!= 0 else i for i in aux ])
#test cases
print(to_camel_case('')) #should return ''
print(to_camel_case("the_stealth_warrior")) #should return "theStealthWarrior"
print(to_camel_case("The-Stealth-Warrior")) #should return "TheStealthWarrior"
print(to_camel_case("A-B-C")) #should return "ABC"