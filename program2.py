class Solution:
    listOfNums = [1, 3, 2, 5]
    outputNum = 0
    powerOf10 = len(listOfNums) #help to deside how many zeros do we need to put after the nubber in position [i] ## 1*10^3 + 3*10^2 + 2*10^1 + 5*10^0 = 1000+300+20+5 = 1325
    def plusOne(self):
        for i in range(len(self.listOfNums)): #for each number i list
            self.outputNum += self.listOfNums[i] * 10 ** (self.powerOf10 - i - 1)  #self.listOfNums[i] -- current number from list; *10 -- we need to put zeros after the nubber in position [i]; **(...) -- deside how many: (self.powerOf10 - 1 -- we have one zero less: 1000 for 4 elements in list; -i -- we must take into account that the positions of elements in the list changes)
        return self.outputNum

##     ##     ##     ##     ##     ##     ##     ##     ##     ##     
myNumber = Solution()
print(myNumber.plusOne())
