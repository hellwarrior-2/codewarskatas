#Exercise 7kyu
#Sum of a sequence
#Your task is to make function, which returns the sum of
#a sequence of integers.

#The sequence is defined by 3 non-negative values: begin, end, step.

#If begin value is greater than the end, function should returns 0
#Examples

#sequenceSum(2,2,2) === 2
#sequenceSum(2,6,2) === 12 // 2 + 4 + 6
#sequenceSum(1,5,1) === 15 // 1 + 2 + 3 + 4 + 5
#sequenceSum(1,5,3) === 5 // 1 + 4

def sequence_sum(begin_number, end_number, step):
    return 0 if begin_number > end_number else sum(range(begin_number, end_number + 1, step))

#test cases
print (sequence_sum(2, 6, 2)) #should return 12
print (sequence_sum(1, 5, 1)) #should return 15
print (sequence_sum(1, 5, 3)) #should return 5
print(sequence_sum(0, 15, 3)) #should return 45
print(sequence_sum(16, 15, 3)) #should return 0
print(sequence_sum(2, 24, 22)) #should return 26
print(sequence_sum(2, 2, 2)) #should return 2
print(sequence_sum(2, 2, 1)) #should return 2
print(sequence_sum(1, 15, 3)) #should return 35
print(sequence_sum(15, 1, 3)) #should return 0