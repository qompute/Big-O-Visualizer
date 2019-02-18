import random

def random_list(n, max_int=1000000):
    return [random.randrange(max_int) for _ in range(n)]

# ===================== O(n^2) algorithms =====================
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if(lst[j] > lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]

def selection_sort(lst):
    for i in range(len(lst)):
        min_j = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_j]:
                min_j = j
        lst[i], lst[min_j] = lst[min_j], lst[i]

# lst = random_list(100)
# print(lst)
# selection_sort(lst)
# print(lst)
