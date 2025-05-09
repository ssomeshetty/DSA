# | Feature           | `list`   | `deque`   | `LifoQueue`         |
# | ----------------- | -------- | --------- | ------------------- |
# | Syntax Simplicity | ✅ Yes    | ✅ Yes     | 🚫 Slightly verbose |
# | Thread-safe       | ❌ No     | ❌ No      | ✅ Yes               |
# | Performance       | ✅ Fast   | ✅ Fastest | ⚠️ Slower (locking) |
# | Use in Threads    | ❌ Unsafe | ❌ Unsafe  | ✅ Safe              |
# | Blocking Ops      | ❌ No     | ❌ No      | ✅ Yes               |

# 🔹 Analogy
# Imagine multiple people trying to withdraw money from the same ATM at the same time:

# A non-thread-safe ATM lets them access it simultaneously → potential errors or fraud.

# A thread-safe ATM locks itself when one person is using it → others wait → ensures correctness

from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

print(stack.pop())

print(stack)

print(stack.pop())

print(stack)

stack.append(4)
print(stack)

