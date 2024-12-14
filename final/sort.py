def selection_sort(array):
    for i in range(len(array)):
        minIndex = i
        for j in range(i + 1,len(array)):           # 비정렬 리스트에서 최소값 찾기
            if array[minIndex] > array[j]:          # 최소값과 비정렬 리스트의 첫번째 값을 바꿈
                minIndex = j
        tmp = array[i]
        array[i] = array[minIndex]
        array[minIndex] = tmp

def insertion_sort(array):
    for i in range(1, len(array)):
        key = v[i]
        j = i - 1
        while j >= 0 and array[j] < key:
            array[j + 1] = array[j]
            j -= 1
        v[j + 1] = key

v = [3, 5, 6, 9, 2, 4, 1, 8]
#v = [5, 4, 3, 2, 1]

selection_sort(v)
print(v)