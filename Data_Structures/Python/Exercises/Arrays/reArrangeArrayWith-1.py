def fixArray(ar, n):
    print('ar', ar)
    print('n', n)
    for i in range(n):
        print('i ', i)
        for j in range(n):
            print('j ', j)
            print('condition arr[j] == i ', ar[j], i, ar[j] ==i)
            if (ar[j] == i):
                ar[j], ar[i] = ar[i], ar[j]

    for i in range(n):
            if (ar[i] != i):
                ar[i] = -1


    print('final array => ', ar)

    for i in range(n):
        print(ar[i], end = " ")

ar = [ -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 ]
n = len(ar)

fixArray(ar, n)
