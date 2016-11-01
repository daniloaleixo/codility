
def solution(A, K):
    # write your code in Python 2.7
    
    new_array = [None] * len(A) 
    

    for i in range(0, len(A)):
    	#print i, (i + K) % len(A), A[i], len(new_array)
    	new_array[ (i + K) % len(A)] = A[i]

    return new_array


print solution([3, 8, 9, 7, 6], 3)

print solution([3, 8, 9, 7, 6], 15)

print solution([-3, 8, 9, 7, 6], 15)