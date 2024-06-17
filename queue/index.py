from collections import deque

def reverse(queue: deque) -> deque:
    new_queue = deque()
    new_queue.append(queue.pop())
    return new_queue
if __name__ == '__main__':
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.reverse()
    print(q)
