from multiprocessing import Process, Queue

queue = Queue()

# Every process has its own memory space/ name space
# to be able to share the variable we use the queue

def prep_chai(queue):
    queue.put("Masala Chai is Ready...")


if __name__ == "__main__":
    p = Process(target=(prep_chai), args=(queue,))
    p.start()
    p.join()

    print(queue.get())
