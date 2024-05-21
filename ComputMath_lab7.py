def counting_sort(alist, largest):
    c = [0] * (largest + 1)
    for i in range(len(alist)):
        c[alist[i]] = c[alist[i]] + 1

    c[0] = c[0] - 1
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]

    result = [None] * len(alist)

    for x in reversed(alist):
        result[c[x]] = x
        c[x] = c[x] - 1

    return result

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def merge_sort(alist, start, end):

    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge_list(alist, start, mid, end)

def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1


alist = [5, 6, 8, 1, 2, 3, 4, 5, 5]
alist2 = alist
alist3 = alist
alist = [int(x) for x in alist]


merge_sort(alist, 0, len(alist))
print('Сортировка слиянием: ', end='')
print(alist)


print('Сортировка пузырьком: ', end='')
print(bubble_sort(alist2))

alist3 = [int(x) for x in alist3]
k = max(alist3)

sorted_list = counting_sort(alist3, k)
print('Сортировка подсчётом: ', end='')
print(sorted_list)