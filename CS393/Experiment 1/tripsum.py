N = int(input())
M = int(input())
a = []
for i in range(N):
    a.append(int(input()))
for i in range(0 , N-2):
    for j in range(i + 1 , N-1):
        for k in range(j + 1, N):
            if (a[i] + a[j] +a[k] == M):
                print(1)
