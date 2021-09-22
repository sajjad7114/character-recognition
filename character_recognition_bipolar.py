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


w = {'a': [0]*64, 'b': [0]*64, 'c': [0]*64, 'd': [0]*64, 'e': [0]*64, 'j': [0]*64, 'k': [0]*64}

alph = ['a', 'b', 'c', 'd', 'e', 'j', 'k']

c = 0
for a in alph:
    l_arr = [-1] * 7
    l_arr[c] *= -1
    for i in range(1, 4):
        filename = 'data/' + a + str(i) + '.txt'
        arr = read(filename, 1, -1)
        d = 0
        for b in alph:
            w[b][0] += l_arr[d]
            for j in range(63):
                w[b][j+1] += arr[j] * l_arr[d]
            d += 1
    c += 1

for a in alph:
    print('testing ' + a + ' with real data:')
    for al in alph:
        print(al, end='\t\t')
    print()
    for i in range(1, 4):
        filename = 'data/' + a + str(i) + '.txt'
        arr = read(filename, 1, -1)
        y_in = [0]*7
        y_out = []
        j = 0
        for b in alph:
            y_in[j] -= w[b][0]
            for k in range(63):
                y_in[j] += arr[k] * w[b][k+1]
            y_out.append(y_in[j] >= 0)
            j += 1
        for y in y_in:
            print(y, end='\t')
            if -99 <= y < 100:
                print(' ', end='\t')
        print()
    print()

for a in alph:
    print('testing ' + a + ' with noisy data:')
    for al in alph:
        print(al, end='\t\t')
    print()
    for i in range(1, 4):
        filename = 'test/' + str(i) + a + '.txt'
        arr = read(filename, 1, -1)
        y_in = [0]*7
        y_out = []
        j = 0
        for b in alph:
            y_in[j] -= w[b][0]
            for k in range(63):
                y_in[j] += arr[k] * w[b][k+1]
            y_out.append(y_in[j] >= 0)
            j += 1
        for y in y_in:
            print(y, end='\t')
            if -99 <= y < 100:
                print(' ', end='\t')
        print()
    print()