import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"\n[Timer] {func.__name__} выполнился за {elapsed:.4f} сек")
        return result
    return wrapper


def get_user_filter():
    print("\nФильтр по статусу (или Enter чтобы пропустить):")
    print("  Варианты: DEBUG, INFO, WARNING, ERROR, CRITICAL")
    status = input("  Введи статус: ").strip().upper()
    return status if status else None


def get_date_range():
    print("\nФильтр по дате (или Enter чтобы пропустить):")
    start = input("  Начало (YYYY-MM-DD): ").strip()
    end = input("  Конец  (YYYY-MM-DD): ").strip()

    if start and end:
        return start, end

    return None, None