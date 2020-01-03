#Exercise 8 kyu
#Convert boolean values to strings 'Yes' or 'No'.

#Description:
#Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'
#test cases    
print(bool_to_word(True)) #should print "Yes"
print(bool_to_word(False)) #should print "No"
