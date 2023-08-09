from threading import Semaphore
from asyncio import Queue

finish_lst = Queue()
tasks_lst = Queue()

# semaph_worker = Semaphore(0)
semaph_boss = Semaphore(0)
