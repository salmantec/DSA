def reverseArr(Arr, start, end):
    if start >= end:
        return
    Arr[start], Arr[end] = Arr[end], Arr[start]
    reverseArr(Arr, start+1, end-1)

Arr = [1, 2, 3, 4, 5, 6]
print('Before reverse ', Arr)
reverseArr(Arr, 0, len(Arr)-1)
print('After reverse ', Arr)
