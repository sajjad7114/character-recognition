def read(filename, p, n):
    arr = []
    with open(filename, 'r') as f:
        s = f.read().split()
        for line in s:
            for point in line:
                if point == '*':
                    arr.append(p)
                else:
                    arr.append(n)
    return arr


w = []
alph = ['a', 'b', 'c', 'd', 'e', 'j', 'k']

for a in alph:
    l_w = [0]*64
    for i in range(1, 4):
        filename = 'data/' + a + str(i) + '.txt'
        arr = read(filename, 1, 0)
        l_w[0] += 1
        for j in range(63):
            l_w[j+1] += arr[j]
    w.append(l_w)

for a in alph:
    print('testing ' + a + ' with real data:')
    for al in alph:
        print(al, end='  ')
    print()
    for i in range(1, 4):
        filename = 'data/' + a + str(i) + '.txt'
        arr = read(filename, 1, 0)
        y_in = [0]*7
        y_out = []
        for j in range(7):
            y_in[j] -= w[j][0]
            for k in range(63):
                y_in[j] += arr[k] * w[j][k+1]
            y_out.append(y_in[j] >= 0)
        for y in y_in:
            if y < 10:
                print(' ', end='')
            print(y, end=' ')
        print()
    print()

for a in alph:
    print('testing ' + a + ' with noisy data:')
    for al in alph:
        print(al, end='  ')
    print()
    for i in range(1, 4):
        filename = 'test/' + str(i) + a + '.txt'
        arr = read(filename, 1, 0)
        y_in = [0]*7
        y_out = []
        for j in range(7):
            y_in[j] -= w[j][0]
            for k in range(63):
                y_in[j] += arr[k] * w[j][k+1]
            y_out.append(y_in[j] >= 0)
        for y in y_in:
            if 0 <= y < 10:
                print(' ', end='')
            print(y, end=' ')
        print()
    print()
