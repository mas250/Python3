List = []
cList = []


def cumulative():
    lastI = 0
    for i in range (0, 21):         #with a list this line should read "for i range (lenList[i])):
        List.append(i)
        lastI = lastI + List[i]
        cList.append(lastI)
    print(cList)

cumulative()
