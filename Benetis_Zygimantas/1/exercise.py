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

def problemSolution(cases):
    import re

    def isCaseCorrect(caseString):
        def isTagCorrect(tag):
            insideTag = re.search('\<\/?([a-zA-Z]{1,10}?)\>', tag)
            if insideTag:
                return True
            else:
                return False

        def isTagsOrderValid(tagList):
            def isOpenTag(tag):
                if tag[1] == '/':
                    return False
                else:
                    return True
            def makeOpenTag(tag):
                return tag.replace('/', '')
            #imperative solution
            tagStack = []
            for itTag in tagList:
                if isOpenTag(itTag):
                    tagStack.append(itTag)
                else:
                    if not tagStack:
                        return False
                    removedTag = tagStack.pop()
                    if removedTag != makeOpenTag(itTag):
                        return False
            return True

        tagIterator = re.finditer('\<\/?.*?\>', caseString)
        tagList = list(map(lambda x: x.group(), tagIterator))
        areTagsValid = tagList == filter(isTagCorrect, tagList)
        return areTagsValid and isTagsOrderValid(tagList)

    def checkCases(casesToCheck):
        solution = map(lambda (i,x): "Case #{} : Correct".format(i+1) \
            if isCaseCorrect(x) else "Case #{} : Incorrect".format(i+1),\
            enumerate(casesToCheck))

        print(solution)

    checkCases(cases)

problemSolution(getInput())
