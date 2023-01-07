
class Queue:
    def __init__(self):
        self._enqueue_stack = list()
        self._dequeue_stack = list()

    def _fill_dequeue_stack(self):
        while len(self._enqueue_stack) > 0:
            value = self._enqueue_stack.pop()
            self._dequeue_stack.append(value)

    def enqueue(self, value:int):
        self._enqueue_stack.append(value)

    def dequeue(self):
        if not self._dequeue_stack:
            self._fill_dequeue_stack()

        return self._dequeue_stack.pop()

    def print_first(self):
        if not self._dequeue_stack:
            self._fill_dequeue_stack()

        print(self._dequeue_stack[-1])


# input: 5 7 8
# s1:    <-
# s2: 8 7 5

if __name__ == '__main__':
    t = int(input())
    queue = Queue()
    for i in range(t):
        query = input().split()

        if query[0] == '1':
            value = int(query[1])
            queue.enqueue(value)
        elif query[0] == '2':
            queue.dequeue()
        else:
            queue.print_first()

