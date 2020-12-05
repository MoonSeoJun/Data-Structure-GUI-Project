class ListStack(object):
    def __init__(self):
        self.stack = []

    def stack_push(self,item):
        self.stack.append(item)

    def print_stack(self,num):
        return self.stack[num]
    
    def stack_pop(self):
        return self.stack.pop()

    def reset_stack(self):
        while self.stack:
            print(self.stack)
            self.stack_pop()
            
stack_list = ListStack()

