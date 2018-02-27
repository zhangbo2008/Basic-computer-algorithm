# update the parent element,aLen for sorting
def downEle(aList, pos, aLen):
    # left child's and right child's key
    left = 2 * pos + 1
    right = 2 * pos + 2

    exchange = pos

    # parent's value should be larger than children's
    if left < aLen and aList[exchange] < aList[left]:
        exchange = left
    if right < aLen and aList[exchange] < aList[right]:
        exchange = right
    if exchange != pos:
        aList[pos], aList[exchange] = aList[exchange], aList[pos]
        # the same as the child heap
        downEle(aList, exchange, aLen)


def buildHeap(aList):
    aLen = len(aList)

    # building from the mini tree
    for i in range(aLen / 2, -1, -1):
        downEle(aList, i, aLen)


def sortHeap(aList):
    aLen = len(aList)

    for i in range(0, aLen):
        # put the max number to the end of list and find the max number of the
        # rest heap
        aList[0], aList[aLen - i - 1] = aList[aLen - i - 1], aList[0]
        downEle(aList, 0, aLen - i - 1)


def upEle(aList, pos):
    # parent's key
    parent = (pos - 1) / 2

    # keep the max heap,parent's value should be larger than children's
    while pos >= 0 and aList[parent] < aList[pos]:
        aList[pos], aList[parent] = aList[parent], aList[pos]
        # the same as the child heap
        pos = parent
        parent = pos / 2


def addEle(aList, ele):
    # add the new element and keep the max heap
    aList.append(ele)
    upEle(aList, len(aList) - 1)

aList =[8,3,2,78,99,7,9546,98]

sortHeap(aList)
print (aList)
