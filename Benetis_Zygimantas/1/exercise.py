def list_append(lst, item):
    lst.append(item)
    return lst

def getInput():
    def readFile():
        f = open('input_data', 'r')
        return f.read().split('\n')
    fileContent = readFile()
    def groupLinesIntoCases(currentArrayIndex, caseList):
        caseSize = int(fileContent[currentArrayIndex])
        if caseSize == 0:
            return caseList
        caseStartingIndex = currentArrayIndex + 1
        caseEndingIndex = caseStartingIndex + caseSize
        caseString = fileContent[caseStartingIndex:caseEndingIndex]
        return groupLinesIntoCases(caseEndingIndex, list_append(caseList, '\n'.join([str(x) for x in caseString])))

    return groupLinesIntoCases(0, [])

cases = getInput()
import re

def isCaseCorrect(caseString):
    def isTagCorrect(tag):
        insideTag = re.search('\<\/?([a-zA-Z]{1,10}?)\>', tag)
        if insideTag:
            return True
        else:
            return False

    def isTagsOrderValid(tagList):
        print(tagList)
        isTagOpen = lambda x: False if (x[1] == '/') else True
                
        return True

    tagIterator = re.finditer('\<\/?.*?\>', caseString)
    tagList = list(map(lambda x: x.group(), tagIterator))
    areTagsValid = tagList == filter(isTagCorrect, tagList)
    # todo: We can cut here if tags are not valid
    # return areTagsValid and isTagsOrderValid(tagList)
    return isTagsOrderValid(tagList)

print(isCaseCorrect('<html>testas</html><>'))
