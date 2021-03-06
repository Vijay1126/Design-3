# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.cursor = None
        self.stack.append(iter(nestedList))
        #this adds an iterator pointing to the first integer/integer in list
    def next(self) -> int:
        outputVal = self.cursor
        self.cursor = None
        return outputVal
        
    
    def hasNext(self) -> bool:
         
        while len(self.stack)>0 and self.cursor==None:
            
            currentIterator = self.stack[-1]
            nextValue  = next(currentIterator, None)
            if nextValue == None:
                self.stack.pop()
                continue
            elif nextValue.isInteger():
                self.cursor = nextValue.getInteger()
                return True
            else:
                self.stack.append(iter(nextValue.getList()))
                
        return False
Time : O(Depth - Nested Lists)
Space: O(1)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())