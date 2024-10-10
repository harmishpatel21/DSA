import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    lefthalf = arr[:mid]
    righthalf = arr[mid:]

    sorted_left = merge_sort(lefthalf)
    sorted_right = merge_sort(righthalf)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right [j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    temp_list = [random.randint(0, 100) for _ in range(10)]
    print(temp_list)
    sorted_list = merge_sort(temp_list)
    print(sorted_list)
