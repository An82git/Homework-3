from multiprocessing import cpu_count
import concurrent.futures
from time import time


def worker(number: int) -> list:
    rezult = []
    for num in range(1, number + 1):
        if number % num == 0:
            rezult.append(num) 
    return rezult


def factorize(*number) -> list:
    cores = cpu_count() // 2 if cpu_count() >= 2 else 1
    with concurrent.futures.ProcessPoolExecutor(cores) as executor:
        return [el for el in executor.map(worker, number)]


if __name__ == "__main__":

    t = time()
    a, b, c, d  = factorize(128, 255, 99999, 10651060)
    print(f"Time - {time() - t}s")

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 
                304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 
                2662765, 5325530, 10651060]
