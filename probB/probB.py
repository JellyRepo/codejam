import sys, fileinput, math
numTries = int(raw_input())
sys.setrecursionlimit(4000)

def find_least(pancakesPlated, minutes):
    print pancakesPlated,minutes
    if (math.ceil(max(pancakesPlated)) <= 1):
        return minutes + 1
    newPancakesPlated = pancakesPlated[1:] + [int(math.floor(pancakesPlated[0]/2.0))] + [int(math.ceil(pancakesPlated[0]/2.0))]
    newPancakesPlated.sort(reverse=True)
    return min(find_least(map(lambda x:x-1, pancakesPlated), minutes + 1),
    find_least(newPancakesPlated, minutes + 1))

"""
def find_num(plates, pancakesPlated):
    if reserve >= len(arrNum):
        return required
    if reserve > 0:
        newReserve = sum(arrNum[0:reserve])
        return find_num(arrNum[reserve:], newReserve, required)
    if reserve == 0:
        if int(arrNum[0]) == 0:
            return find_num(arrNum[1:], reserve, required+1)
        else:
            return find_num(arrNum[1:], reserve + int(arrNum[0]) -1, required)
    return 1337
"""

for line in range(numTries):
    plates = int(raw_input())
    pancakesPlated = map(int, raw_input().split(" "))
    pancakesPlated.sort(reverse=True)
    print "Case #"+str(line+1)+": "+str(find_least(pancakesPlated, 0))
