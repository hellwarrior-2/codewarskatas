#Exercise 6kyu
#Format a string of names like 'Bart, Lisa & Maggie'.

#Given: an array containing hashes of names

#Return: a string formatted as a list of names
#separated by commas except for the last two names,
#which should be separated by an ampersand.

#Example:

#namelist([ {'name': 'Bart'}, {'name': 'Lisa'},
#{'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

#namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

#namelist([ {'name': 'Bart'} ])
# returns 'Bart'

#namelist([])
# returns ''

def namelist(names):
    ans = ''.join(i['name'] + ', ' for i in names)
    ans = ans[::-1]
    ans = ans.replace(",", "", 1)
    ans = ans.replace(" ", "", 1)
    ans = ans.replace(',', '& ', 1)
    return ans[::-1]

#test cases
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))
#should return 'Bart, Lisa, Maggie, Homer & Marge',

print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]))
#should return 'Bart, Lisa & Maggie'

print(namelist([{'name': 'Bart'},{'name': 'Lisa'}]))
#should return 'Bart & Lisa'

print(namelist([{'name': 'Bart'}]))
#should return 'Bart'
print(namelist([])) #should return ''




