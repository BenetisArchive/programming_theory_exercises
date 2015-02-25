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
    caseError = ''

    def isCaseCorrect(caseString):
        def isTagCorrect(tag):
            insideTag = re.search('\<\/?([a-zA-Z]{1,10}?)\>', tag)
            if insideTag:
                return True
            else:
                problemSolution.caseError = 'Tag ' + tag + ' is incorrect'
                return False

        def isTagsOrderValid(tagList):
            def isOpenTag(tag):
                if tag[1] == '/':
                    return False
                else:
                    return True
            def makeOpenTag(tag):
                return tag.replace('/', '')
            tagStack = []
            for itTag in tagList:
                if isOpenTag(itTag):
                    tagStack.append(itTag)
                else:
                    if not tagStack:
                        problemSolution.caseError = 'No opening tag of '+ itTag
                        return False
                    removedTag = tagStack.pop()
                    if removedTag != makeOpenTag(itTag):
                        problemSolution.caseError = 'Expected ending tag of '+removedTag
                        return False
            return True

        problemSolution.caseError = ''
        tagIterator = re.finditer('\<\/?.*?\>', caseString)
        tagList = list(map(lambda x: x.group(), tagIterator))
        areTagsValid = tagList == filter(isTagCorrect, tagList)
        return areTagsValid and isTagsOrderValid(tagList)

    def checkCases(casesToCheck):
        solution = map(lambda (i,x): "Case #{} : Correct".format(i+1) \
            if isCaseCorrect(x) else "Case #{} : Incorrect. Error: ".format(i+1)+problemSolution.caseError,\
            enumerate(casesToCheck))

        print('\n'.join(solution))

    checkCases(cases)

    
problemSolution(getInput())
