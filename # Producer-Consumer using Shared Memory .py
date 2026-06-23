# Producer-Consumer using Shared Memory (Python - BSc CS level)

import multiprocessing
import time
import random

# Buffer size
BUFFER_SIZE = 5

def producer(buffer, in_index, empty, full, mutex):
    for i in range(10):  # produce 10 items
        item = random.randint(1, 100)
        
        empty.acquire()   # wait if buffer is full
        mutex.acquire()   # lock for mutual exclusion

        buffer[in_index.value] = item
        print(f"Producer produced: {item} at index {in_index.value}")
        in_index.value = (in_index.value + 1) % BUFFER_SIZE

        mutex.release()
        full.release()    # signal that buffer has new item
        time.sleep(random.random())

def consumer(buffer, out_index, empty, full, mutex):
    for i in range(10):  # consume 10 items
        full.acquire()   # wait if buffer is empty
        mutex.acquire()  # lock for mutual exclusion

        item = buffer[out_index.value]
        print(f"Consumer consumed: {item} from index {out_index.value}")
        out_index.value = (out_index.value + 1) % BUFFER_SIZE

        mutex.release()
        empty.release()  # signal that buffer has free space
        time.sleep(random.random())

if __name__ == "__main__":
    # Shared buffer and index pointers
    buffer = multiprocessing.Array('i', BUFFER_SIZE)  
    in_index = multiprocessing.Value('i', 0)
    out_index = multiprocessing.Value('i', 0)

    # Semaphores
    empty = multiprocessing.Semaphore(BUFFER_SIZE)  # initially all slots empty
    full = multiprocessing.Semaphore(0)             # initially no full slots
    mutex = multiprocessing.Lock()                  # for critical section

    # Create producer and consumer processes
    p = multiprocessing.Process(target=producer, args=(buffer, in_index, empty, full, mutex))
    c = multiprocessing.Process(target=consumer, args=(buffer, out_index, empty, full, mutex))

    # Start processes
    p.start()
    c.start()

    # Wait for processes to finish
    p.join()
    c.join()

    print("Producer-Consumer problem solved using shared memory!")
