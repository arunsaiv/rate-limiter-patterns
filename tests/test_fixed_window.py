import sys
import os

# Add the parent directory (project root) to sys.path so Python can find fixed_window
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fixed_window import FixedWindowRateLimiter
import time

# Function to test the Fixed Window Rate Limiting strategy
def test_fixed_window():
    # Initialize the rate limiter with a limit of 5 requests per 10 seconds
    limiter = FixedWindowRateLimiter(limit=5, window_size=10)

    # Simulate a unique user (this could be a user ID or IP in a real application)
    user = "user123"

    print("Testing Fixed Window Rate Limiter:")

    # Send 10 requests, 1 second apart
    for i in range(10):
        # Check if the request is allowed under the current rate limit
        allowed = limiter.allow_request(user)

        # Print the result of the request attempt
        print(f"Request {i+1}: {'✅ Allowed' if allowed else '❌ Blocked'}")

        # Wait for 1 second before sending the next request
        time.sleep(1)

# Only run the test if this file is executed directly
if __name__ == "__main__":
    test_fixed_window()