import threading

"""

Print numbers 1 to 100 in order using two threads, one for even and one for odd nums

"""

# Condition variable for taking turns
# Odd thread should wait until notified by even thread, and vice versa
class OddEvenCondition(threading.Condition):
    ODD = True
    EVEN = False

    def __init__(self):
        super().__init__()
        self.turn = self.ODD # start with 1

    def wait_turn(self, old_turn):
        with self: # context manager to acquire lock on CV
            while self.turn != old_turn:
                self.wait()


    def toggle_turn(self):
        with self:
            self.turn ^= True
            self.notify()

# Odd thread
# Should run and print, waiting on CV for odd turn

class OddThread(threading.Thread):
    def __init__(self, monitor):
        super().__init__()
        self.monitor = monitor

    def run(self):
        for i in range(1, 101, 2):
            self.monitor.wait_turn(OddEvenCondition.ODD)
            print("OddThread: ", i)
            self.monitor.toggle_turn()

# Even thread
# Should run and print, waiting on CV for even turn
class EvenThread(threading.Thread):
    def __init__(self, monitor):
        super().__init__()
        self.monitor = monitor
    
    def run(self):
        for i in range(2, 101, 2):
            self.monitor.wait_turn(OddEvenCondition.EVEN)
            print("EvenThread: ", i)
            self.monitor.toggle_turn()

turn = OddEvenCondition()
even = EvenThread(turn)
odd = OddThread(turn)
even.start()
odd.start()
even.join()
odd.join()
