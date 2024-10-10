import random

def selection_sort(temp_list):
    n = len(temp_list)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if temp_list[j] < temp_list[min_idx]:
                min_idx = j
        temp_list[i], temp_list[min_idx] = temp_list[min_idx], temp_list[i]

    return temp_list

if __name__ == "__main__":
    temp_list = [random.randint(0, 100) for _ in range(10)]
    print(temp_list)
    sorted_list = selection_sort(temp_list)
    print(sorted_list)
