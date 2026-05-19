import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"\n[Timer] {func.__name__} executed in {elapsed:.4f} sec")
        return result
    return wrapper


def get_user_filter():
    print("\nFilter by status (or press Enter to skip):")
    print("  Options: DEBUG, INFO, WARNING, ERROR, CRITICAL")
    status = input("  Enter status: ").strip().upper()
    return status if status else None


def get_date_range():
    print("\nFilter by date (or press Enter to skip):")
    start = input("  Start (YYYY-MM-DD): ").strip()
    end = input("  End   (YYYY-MM-DD): ").strip()
    if start and end:
        return start, end
    return None, None