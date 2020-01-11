#Exercise 7 kyu
#Two to one

#Take 2 strings s1 and s2 including only letters
#from a to z. Return a new sorted string,
#the longest possible, containing distinct letters,
#each taken only once - coming from s1 or s2.

#Examples:
#a = "xyaabbbccccdefww"
#b = "xxxxyyyyabklmopq"
#longest(a, b) -> "abcdefklmopqwxy"

#a = "abcdefghijklmnopqrstuvwxyz"
#longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(s1, s2):
    ans = sorted(set(s1 + s2))
    return ''.join(ans)

#tests cases
print(longest("aretheyhere", "yestheyarehere")) 
#should return "aehrsty"
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))
#should return "abcdefghilnoprstu"
print(longest("inmanylanguages", "theresapairoffunctions"))
#should return "acefghilmnoprstuy"