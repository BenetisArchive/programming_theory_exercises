def list_append(lst, item):
    lst.append(item)
    return lst

def input(): 
    fileContent = readFile()
    def groupLinesIntoCases(currentArrayIndex, caseList):
        caseSize = int(fileContent[currentArrayIndex])
        if caseSize == -1:
            return caseList
        caseStartingIndex = currentArrayIndex + 1
        caseEndingIndex = caseStartingIndex + caseSize
        caseString = fileContent[caseStartingIndex:caseEndingIndex]
        return groupLinesIntoCases(caseEndingIndex, list_append(caseList, '\n'.join([str(x) for x in caseString])))
    def readFile():
        f = open('input_data', 'r')
        return f.read().split('\n')

    return groupLinesIntoCases(0, [])


cases = input()
print(cases)
