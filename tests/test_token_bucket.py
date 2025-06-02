import time
import sys
import os

# Add the parent directory (project root) to sys.path so Python can find token_bucket
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from token_bucket import TokenBucketRateLimiter

# Initialize rate limiter: 5 tokens/sec, max 10 tokens stored
limiter = TokenBucketRateLimiter(rate=5, capacity=10)

print("Sending 15 requests with 0.1s interval:\n")
for i in range(15):
    allowed = limiter.allow_request()
    print(f"Request {i + 1}: {'✅ Allowed' if allowed else '❌ Blocked'}")
    time.sleep(0.1)

print("\nSleeping for 2 seconds to let tokens refill...\n")
time.sleep(2)

print("Sending 5 more requests:\n")
for i in range(5):
    allowed = limiter.allow_request()
    print(f"Request {i + 16}: {'✅ Allowed' if allowed else '❌ Blocked'}")