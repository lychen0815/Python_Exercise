class Stack:
    def __init__(self):
        self.the_stack = []
        self.count = 0
    def __len__(self):
        return self.count
    def is_empty(self):
        return self.count == 0
    def push(self,item):
        self.the_stack.append(item)
        self.count += 1
    def pop(self):
        assert not self.is_empty()
        self.count -= 1
        return self.the_stack.pop()

    def peek(self):
        assert not self.is_empty()
        return self.the_stack[-1]

def my_reverse(li):
    rev_stack = Stack()
    while len(li) > 0:
        rev_stack.push(li.pop(0))
    while len(rev_stack) > 0:
        li.append(rev_stack.pop())

li = [1,2,3,4]
print(li)

my_reverse(li)
print(li)