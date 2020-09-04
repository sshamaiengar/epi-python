import threading

"""

Create synchronization mechanism for readers and writers of shared resource.

Any reader must wait for a writer to finish.
Any writer must wait for all readers to finish.
Readers may access at the same time.

Idea:
    track readers and writers
    if both are 0, get access and increment depending on type of accessor
    if reader and writers == 0:
        increment readers and get access
    if writer and readers == 0:
        increment writers and get access
    if writer and writers > 0:
        wait
    if reader and writers > 0:
        wait

Book Solution:
Read + write locks, with a read counter locked by read lock

Reader:
Lock read lock
Increment counter
release read lock
Do read
Lock read lock
Decrement counter
Release read lock

Writer:
Lock write lock
While True
    Lock read lock
    write if read counter is 0
    Release read lock
Release write lock

"""

class ReaderWriter:
    LR = threading.Lock()
    LW = threading.Lock()
    read_count = 0
    data = 0

class Reader(threading.Thread):
    def run(self):
        while True:
            with ReaderWriter.LR:
                ReaderWriter.read_count += 1

            print(ReaderWriter.data) # read

            with ReaderWriter.LR:
                ReaderWriter.read_count -= 1
                ReaderWriter.LR.notify()

class Writer(threading.Thread):
    def run(self):
        while True:
            with ReaderWriter.LW:
                done = False
                while not done:
                    with ReaderWriter.LR:
                        if ReaderWriter.read_count == 0:
                            ReaderWriter.data += 1 # write
                            done = True
                        else:
                            while ReaderWriter.read_count != 0:
                                ReaderWriter.LR.wait()



