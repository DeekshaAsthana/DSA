from os import *
from sys import *
from collections import *
from math import *

class Deque:
    def __init__(self, size):
        self.size=size
        self.q=[0]*size
        self.Front=-1
        self.Rear=-1
    # Pushes 'X' in the front of the deque. Returns true if it gets pushed into the deque, and false otherwise.
    def pushFront(self, x):
        if (self.isFull()):
            return False
        if(self.Front==-1):
            self.Front=0
            self.Rear=0
        else:
            self.Front=(self.Front-1)%self.size 
        self.q[self.Front]=x
        return True
        # Write your code here
    

    # Pushes 'X' in the back of the deque. Returns true if it gets pushed into the deque, and false otherwise.
    def pushRear(self, x):
        if(self.isFull()):
            return False
        if(self.Front==-1):
            self.Front=0
        self.Rear=(self.Rear+1)%self.size 
        self.q[self.Rear]=x
        return True
        # Write your code here
        

    # Pops an element from the front of the deque. Returns -1 if the deque is empty, otherwise returns the popped element.
    def popFront(self):
        if(self.isEmpty()):
            return -1
        x=self.q[self.Front]
        if(self.Front==self.Rear):
            self.Front=-1
            self.Rear=-1
        else:
            self.Front=(self.Front+1)%self.size 
        # Write your code here
        return x

    # Pops an element from the back of the deque. Returns -1 if the deque is empty, otherwise returns the popped element.
    def popRear(self):
        if(self.isEmpty()):
            return -1
        x=self.q[self.Rear]
        if(self.Front==self.Rear):
            self.Front=-1
            self.Rear=-1
        else:
            self.Rear=(self.Rear-1)%self.size
        return x
        # Write your code here


    # Returns the first element of the deque. If the deque is empty, it returns -1.
    def getFront(self):
        if(self.isEmpty()):
            return -1
        return self.q[self.Front]
        # Write your code here
    

    # Returns the last element of the deque. If the deque is empty, it returns -1.
    def getRear(self):
        if(self.isEmpty()):
            return -1
        return self.q[self.Rear]
        # Write your code here

    # Returns true if the deque is empty. Otherwise returns false.
    def isEmpty(self):
        if(self.Front==-1):
            return True
        return False
        # Write your code here
    

    # Returns true if the deque is full. Otherwise returns false.
    def isFull(self):
        if((self.Rear + 1)%self.size==self.Front):
            return True
        return False
        
        # Write your code here
