from queue import LifoQueue

stack = LifoQueue()

print(stack.qsize())

stack.put(1)
stack.put(2)
stack.put(3)

print(list(stack.queue)) #its cannot write like list and deque because it is thread safe .

print(stack.get())
print(stack.get())

print(stack.qsize())

print(list(stack.queue)) # Lock system works, not concurrently we cannot able to perform push and pop operations . like in ATM

print(stack.empty())