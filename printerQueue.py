from linkedqueue import Queue
from random import randint


def printerQueue():
    random = randint(10, 100)
    q = Queue()
    task_received = 0
    task = 0
    tick = 0
    left = 0
    free = True
    while tick < random:
        r = randint(1, 40)
        if r % 5 == 0 or r % 13 == 0 or r % 67 == 0:
            pages = r % 61
            q.Enqueue(pages)
            task_received += 1
            print(f"At tick {tick}, task {task_received} of {pages} pages received for printing.")
        elif free and not q.isEmpty():
            pages = q.Dequeue()
            left = pages
            free = False
            task += 1
            print(f"At tick {tick}, task {task} starts printing.")
        elif not free:
            tick += 1
            left -= 1
            if left == 0:
                free = True
                print(f"At tick {tick}, task {task} completed.")


printerQueue()
