import time
import redis

class DistributedTokenBucket:
    def __init__(self, redis_client, key, rate, capacity):
        """
        rate: tokens per second
        capacity: max number of tokens in the bucket
        key: unique identifier per client (user/ip/endpoint)
        """
        self.redis = redis_client
        self.key = key
        self.rate = rate
        self.capacity = capacity

    def allow_request(self):
        current_time = time.time()
        bucket = self.redis.hgetall(self.key)

        if not bucket:
            # First request — initialize bucket
            bucket = {
                "tokens": self.capacity,
                "timestamp": current_time
            }
        else:
            # Decode and convert types
            bucket["tokens"] = float(bucket[b"tokens"])
            bucket["timestamp"] = float(bucket[b"timestamp"])

            # Refill based on elapsed time
            elapsed = current_time - bucket["timestamp"]
            refill = elapsed * self.rate
            bucket["tokens"] = min(self.capacity, bucket["tokens"] + refill)
            bucket["timestamp"] = current_time

        if bucket["tokens"] >= 1:
            bucket["tokens"] -= 1
            self.redis.hmset(self.key, {"tokens": bucket["tokens"], "timestamp": bucket["timestamp"]})
            return True
        else:
            self.redis.hmset(self.key, {"tokens": bucket["tokens"], "timestamp": bucket["timestamp"]})
            return False