

def solution(A):
    # write your code in Python 2.7
    
    dictionary = {}
    for number in A:
    	if dictionary.get(number) == None:
    		dictionary[number] = 1
    	else:
    		dictionary[number] = dictionary[number] + 1


    
    for key in dictionary.keys():
    	if dictionary.get(key) == 1:
    		return key



  #  dictionary[1] = 1
 #   dictionary[2] = 1

#    print dictionary, dictionary.get(1), dictionary.get(3)






print solution([1,2,1,2,3])
print solution([1,2,3])
print solution([9,3,9,3,9,7,9])
my_list = [i for i in  range(0,999999)]
my_list2 = [i for i in  range(0,1000000)]
my_list.extend(my_list2)
print solution(my_list)
#solution([1])