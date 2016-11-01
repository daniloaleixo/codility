import re

def solution(N):
    # write your code in Python 2.7
    N_bin = "{0:b}".format(N)
    # print N_bin

    regex = re.compile("1+")

    # gaps = N_bin.split(regex)
    gaps = re.split("1+", N_bin)

    get_length_gaps = []

    for i in range(0, len(gaps) - 1):
    	get_length_gaps.append(len(gaps[i]))

    # print N_bin, gaps, get_length_gaps, max(get_length_gaps)

    return max(get_length_gaps)




# solution(10)
# solution(8)
# solution(9)
# solution(15)
# solution(529)
# solution(20)
# solution(20)
# solution(1041)
