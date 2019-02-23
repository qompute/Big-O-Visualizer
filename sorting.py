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
def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left, right = lst[:mid], lst[mid:]
        merge_sort(left)
        merge_sort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

def quicksort(lst, begin=0, end=None):
    def partition(lst, begin, end):
        pivot = begin
        for i in range(begin + 1, end + 1):
            if lst[i] <= lst[begin]:
                pivot += 1
                lst[i], lst[pivot] = lst[pivot], lst[i]
        lst[pivot], lst[begin] = lst[begin], lst[pivot]
        return pivot
    if end is None:
        end = len(lst) - 1
    if begin >= end:
        return
    pivot = partition(lst, begin, end)
    quicksort(lst, begin, pivot - 1)
    quicksort(lst, pivot + 1, end)

# lst = random_list(100, 1000)
# print(lst)
# quicksort(lst)
# print(lst)
