import sys
import os
import time

# Add the parent directory (project root) to sys.path so Python can find sliding_window
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sliding_window import SlidingWindowRateLimiter

limiter = SlidingWindowRateLimiter(rate=5, window_size=10)

print("Sending 10 requests in quick succession:")

for i in range(10):
    allowed = limiter.allow_request()
    print(f"Request {i + 1}: {'Allowed' if allowed else 'Blocked'}")
    time.sleep(1)  # You can modify this to 0.5 or 2 to test burst/spread behavior