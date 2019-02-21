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

def insertion_sort(lst):
    for i in range(1, len(lst)):
        val, j = lst[i], i
        while j > 0 and lst[j - 1] > val:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = val

# =================== O(N log N) algorithms ===================


# lst = random_list(100, 1000)
# print(lst)
# insertion_sort(lst)
# print(lst)
