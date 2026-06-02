import time

def retry(max_attempts=3, delay=1):

    def decorator(func):

        def wrapper(*args, **kwargs):

            last_error = None

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)

                except Exception as e:
                    last_error = e
                    time.sleep(delay)

            raise last_error

        return wrapper

    return decorator