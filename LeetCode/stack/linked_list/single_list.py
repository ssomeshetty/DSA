class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None
    
    def push(self,val):
        node = Node(val)
        node.next = self.top
        self.top = node
        print("pushed the item" + str(val))

    def pop(self):
        if self.is_empty():
            print("The stack is Empty")
        else:
            value = self.top.val
            self.top = self.top.next
            print("popped item : " + str(value))

    def peek(self):
        value = self.top.val
        print("peek element :" + str(value))
    
    def display(self):
        curr = self.top
        while curr is not None:
            print("->" + str(curr.val))
            curr = curr.next
    
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.peek()
stack.push(40)
stack.display()
stack.pop()
stack.display()
stack.is_empty()
stack.pop()
stack.display()


