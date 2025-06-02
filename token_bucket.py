import time
import threading

class TokenBucketRateLimiter:
    def __init__(self, rate, capacity):
        """
        rate: Number of tokens to add per second.
        capacity: Maximum number of tokens the bucket can hold.
        """
        self.capacity = capacity
        self.tokens = capacity
        self.rate = rate
        self.last_checked = time.time()
        self.lock = threading.Lock()

    def allow_request(self):
        with self.lock:
            now = time.time()
            # Add new tokens based on elapsed time
            elapsed = now - self.last_checked
            added_tokens = elapsed * self.rate
            self.tokens = min(self.capacity, self.tokens + added_tokens)
            self.last_checked = now

            if self.tokens >= 1:
                self.tokens -= 1
                return True
            else:
                return False