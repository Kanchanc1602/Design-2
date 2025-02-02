# Time Complexity : O(1)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this :


# Your code here along with comments explaining your approach
class MyQueue:

    def __init__(self):

        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
     
        while self.s1:
             self.s2.append(self.s1.pop())
        self.s1.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())

        

    def pop(self) -> int:
        return self.s1.pop()
        

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1