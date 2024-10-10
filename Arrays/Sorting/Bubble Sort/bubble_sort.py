import random

def bubble_sort(temp_list):
    n = len(temp_list)
    for i in range(n-1):
        for j in range(n-i-1):
            if temp_list[j] > temp_list[j+1]:
                temp_list[j], temp_list[j+1] = temp_list[j+1], temp_list[j]
    return temp_list

if __name__ == "__main__":
    temp_list = [random.randint(0, 100) for _ in range(10)]
    print(temp_list)
    sorted_list = bubble_sort(temp_list)
    print(sorted_list)
