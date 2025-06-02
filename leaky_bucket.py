import time
import threading

class LeakyBucketRateLimiter:
    def __init__(self, capacity, leak_rate):
        """
        capacity: Max number of requests the bucket can hold.
        leak_rate: Number of requests processed per second.
        """
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.queue = 0
        self.last_checked = time.time()
        self.lock = threading.Lock()

    def allow_request(self):
        with self.lock:
            now = time.time()
            elapsed = now - self.last_checked

            # Leak requests based on elapsed time
            leaked = elapsed * self.leak_rate
            self.queue = max(0, self.queue - leaked)
            self.last_checked = now

            if self.queue < self.capacity:
                self.queue += 1
                return True
            else:
                return False