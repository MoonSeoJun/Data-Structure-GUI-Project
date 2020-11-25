stack = []

def stack_push(item):
    stack.append(item)

def print_stack(num):
    return stack[num]
    
def stack_pop():
    return stack.pop()

def reset_stack():
    while stack:
        stack_pop()
        print(stack)
