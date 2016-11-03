# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7

    i = 1

    max_sum = A[0]

    if len(A) < 2: return A[0]

    only_negs = []
    num_negs = 0

    while i < len(A) - 1:



    	if A[i] > 0:
    		max_sum += A[i]
    		only_negs = []
    		num_negs = 0
    	else:
    		only_negs.append(A[i])
    		num_negs += 1

    		if num_negs == 6:
    			#print "aqui", only_negs, max(only_negs)
    			max_sum += max(only_negs)
    			num_negs = 0


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
