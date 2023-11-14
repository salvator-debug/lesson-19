from random import *  # імпортую всі команди з random


def bubble_sort(arr):
    arr = [randint(0, 100) for i in range(1000)]
    n = len(arr)
    start = 0
    end = n - 1
    swapped = False

    while not swapped:
        swapped = True
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = False
        end -= 1

    return arr[:]
