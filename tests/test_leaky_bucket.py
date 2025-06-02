import time
import sys
import os 

# Add the parent directory (project root) to sys.path so Python can find leaky_bucket
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from leaky_bucket import LeakyBucketRateLimiter

# Allow max 10 requests in bucket, leak 2 per second
limiter = LeakyBucketRateLimiter(capacity=10, leak_rate=2)

print("Sending 15 requests with 0.1s interval:\n")
for i in range(15):
    allowed = limiter.allow_request()
    print(f"Request {i + 1}: {'✅ Allowed' if allowed else '❌ Blocked'}")
    time.sleep(0.1)

print("\nSleeping for 3 seconds to let bucket drain...\n")
time.sleep(3)

print("Sending 5 more requests:\n")
for i in range(5):
    allowed = limiter.allow_request()
    print(f"Request {i + 16}: {'✅ Allowed' if allowed else '❌ Blocked'}")