import time
from collections import deque

class SlidingWindowRateLimiter:
    """
    Rate limiter using the sliding window log algorithm.

    Attributes:
        rate (int): Maximum number of requests allowed in the time window.
        window_size (int): The size of the time window in seconds.
        requests (deque): Timestamps of allowed requests.
    """

    def __init__(self, rate: int, window_size: int):
        self.rate = rate
        self.window_size = window_size
        self.requests = deque()

    def allow_request(self) -> bool:
        """
        Determines whether a request is allowed based on the current request timestamps.

        Returns:
            bool: True if the request is allowed, False otherwise.
        """
        current_time = time.time()

        # Remove timestamps that are older than the window
        while self.requests and self.requests[0] <= current_time - self.window_size:
            self.requests.popleft()

        if len(self.requests) < self.rate:
            self.requests.append(current_time)
            return True
        return False