T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
 
 
    cnt = 0
    visited = [0] * N
    i = 0
    while i < N:
        if arr[i] == 0:
            visited[i] = 1
            i += 1
            cnt += 1
        elif visited[i] == 0 and arr[i] != 0:
            visited[i] =1
            i = arr[i] - 1
            cnt += 1
        elif visited[i] == 1 and arr[i] != 0:
            i += 1
            cnt += 1
        if i == N-1:
            print(f'#{tc} {cnt}')
            break