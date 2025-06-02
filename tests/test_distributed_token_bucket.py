import time
import redis
import sys
import os

# Add the parent directory (project root) to sys.path so Python can find distributed_token_bucket
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from distributed_token_bucket import DistributedTokenBucket

r = redis.Redis(host='localhost', port=6379, db=0)

def test_distributed_rate_limit():
    limiter = DistributedTokenBucket(redis_client=r, key="client:123", rate=1, capacity=5)

    print("Sending 7 requests with 1-second interval (Rate: 1/s, Capacity: 5):")
    for i in range(7):
        allowed = limiter.allow_request()
        print(f"Request {i+1}: {'✅ Allowed' if allowed else '❌ Rate Limited'}")
        time.sleep(1)

if __name__ == "__main__":
    test_distributed_rate_limit()