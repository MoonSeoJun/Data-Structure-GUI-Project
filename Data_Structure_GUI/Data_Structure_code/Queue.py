from collections import deque

class ListQueue(object):
    def __init__(self):
        self.queue = deque([''] * 7)

    def print_queue(self, num):
        return str(self.queue[num])

    def queue_put(self,item):
        global index_num
        self.queue[index_num] = item
        index_num += 1

    def queue_pop(self):
        self.queue.popleft()
        self.queue.append('')

    def reset_queue(self):
        while self.queue:
            print(self.queue)
            self.queue.pop()

queue_list = ListQueue()

index_num = 0

