
def stoopidSearch(numList, num):
    for elem in numList:
        if elem == num:
            return True
    return False       

#print(stoopidSearch(numList, num))


def binarySearch(numList, num):
    halfList = numList
    while True:
        if num < halfList[int(len(halfList)/2)]:
            halfList = halfList[0:int(len(halfList)/2)]
        elif num > halfList[int(len(halfList)/2)]:
            halfList = halfList[int(len(halfList)/2)+1:len(halfList)]
        else:
            return True
        if len(halfList) == 1:
            if halfList[0] == num:
                return True
            return False


if __name__=="__main__":
    numList = [1, 3, 5, 30, 42, 43, 500]
    num = 3

    print(binarySearch(numList, numList[0]))
    print(binarySearch(numList, numList[1]))
    print(binarySearch(numList, numList[2]))
    print(binarySearch(numList, numList[3]))
    print(binarySearch(numList, numList[4]))
    print(binarySearch(numList, numList[5]))
    print(binarySearch(numList, numList[6]))
