# Leetcode 2259 Remove Digit From Number to Maximize Result
# Random practice problem

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        def findOccurrences(number, digit):
            occurrences = []
            for i in range(len(number)):
                if number[i] == digit:
                    occurrences.append(i)
            return occurrences
        print(findOccurrences(number, digit))
        occurrences = findOccurrences(number, digit)
        currNumber = 0
        for index in occurrences:
            currNumber = max(currNumber, int(number[:index] + number[index+1:]))
        return str(currNumber)
        