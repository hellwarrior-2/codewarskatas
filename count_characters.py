#Exercise 6kyu
#Count characters in your string
#The main idea is to count all the occurring 
#characters(UTF-8) in string. If you have string
#like this aba then the result should be { 'a': 2, 'b': 1 }

#What if the string is empty ? Then the result should be
#empty object literal { }

def count(string):    
    #from collections import Counter
    #return Counter(string)    
    return {i : string.count(i) for i in string}

#Test cases
print(count('aba')) #should return {'a': 2, 'b': 1})
print(count('')) #should return {}