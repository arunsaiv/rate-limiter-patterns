# rate_limiter/fixed_window.py

import time
from collections import defaultdict

class FixedWindowRateLimiter:
    def __init__(self, limit: int, window_size: int):
        """
        :param limit: Max number of requests allowed in the window.
        :param window_size: Window size in seconds.
        """
        self.limit = limit
        self.window_size = window_size
        self.request_counts = defaultdict(int)
        self.timestamps = {}

    def allow_request(self, user_id: str) -> bool:
        """
        Determines if a request from a user should be allowed.
        """
        current_time = int(time.time())
        window_start = current_time - (current_time % self.window_size)

        if self.timestamps.get(user_id) != window_start:
            self.timestamps[user_id] = window_start
            self.request_counts[user_id] = 0

        if self.request_counts[user_id] < self.limit:
            self.request_counts[user_id] += 1
            return True
        return False