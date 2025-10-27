# utils.py
import tracemalloc

def measure_memory(func):
    """
    Измеряет пиковое использование памяти (в байтах) при выполнении func.
    Возвращает максимальный объём памяти, использованный во время func().
    """
    tracemalloc.start()
    func()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak

def to_human_readable(bytes_num):
    """
    Переводит значение байтов в МБ/ГБ с округлением.
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_num < 1024:
            return f"{bytes_num:.2f} {unit}"
        bytes_num /= 1024
    return f"{bytes_num:.2f} TB"

def mean_std(values):
    """
    Возвращает среднее и стандартное отклонение для списка чисел.
    """
    import numpy as np
    return float(np.mean(values)), float(np.std(values))
