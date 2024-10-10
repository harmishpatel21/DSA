import random

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

if __name__ == "__main__":
    temp_list = [random.randint(0, 100) for _ in range(10)]
    print(temp_list)
    sorted_list = insertion_sort(temp_list)
    print(sorted_list)
