import time
from functools import wraps

def rate_limiter(calls_per_second):
    interval = 1 / calls_per_second

    def decorator(func):
        last_called = [0]

        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < interval:
                time.sleep(interval - elapsed)
            last_called[0] = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limiter(2)  # max 2 calls per second
def ping(msg):
    print(f"[{time.time():.2f}] {msg}")

for i in range(5):
    ping(f"Ping {i}")
