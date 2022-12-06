def arrReverse(Arr, start, end):
    while start < end:
        Arr[start], Arr[end] = Arr[end], Arr[start]
        start += 1
        end -= 1

Arr = [1, 2, 3, 4, 5, 6]
print('Before reverse ', Arr)
arrReverse(Arr, 0, len(Arr)-1)
print('After reverse ', Arr)

