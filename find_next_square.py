#Exercise 7 kyu
#Find the next square

#You might know some pretty large perfect
#squares. But what about the NEXT one?

#Complete the findNextSquare method that 
#finds the next integral perfect square after
#the one passed as a parameter. Recall that
#an integral perfect square is an integer n 
#such that sqrt(n) is also an integer.

#If the parameter is itself not a perfect
#square, than -1 should be returned. 
#You may assume the parameter is positive.

#Examples:

#findNextSquare(121) --> returns 144
#findNextSquare(625) --> returns 676
#findNextSquare(114) --> returns -1 
#since 114 is not a perfect

def find_next_square(sq):
    aux = sq ** 0.5
    return int((aux + 1) ** 2) if aux.is_integer() else -1



#tests cases

print(find_next_square(121)) #should return 144
print(find_next_square(625)) #should return 676
print(find_next_square(319225)) #should return 320356
print(find_next_square(15241383936)) #should return 15241630849
print(find_next_square(155)) #should return -1
print(find_next_square(342786627)) #should return -1
