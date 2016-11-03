# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7

    i = 1

    max_sum = A[0]

    if len(A) < 2: return A[0]

    num_negs = 0
    least_negative = -10001

    while i < len(A) - 1:



    	if A[i] > 0:
    		max_sum += A[i]
    		num_negs = 0
    	else:
    		num_negs += 1
    		if A[i] > least_negative: least_negative = A[i]

    		if num_negs == 6:
    			#print "aqui", only_negs, max(only_negs)
    			max_sum += least_negative
    			num_negs = 0
    			least_negative = -10001


    	#print  i, A[i], max_sum
    	i += 1

    #if A[len(A) - 1] < 0:
    max_sum += A[len(A) - 1]

    return max_sum


    
print solution([1,1,1,1,2,1,1,1,1,2,1,1,1,1])
print solution([1, -2, 0, 9, -1, -2])
print solution([1, -2, -2, -9, -1, -2, -5, -3])
print solution([1])
print solution([1, 1])
lista = [-1] * 1000000
print solution(lista)
