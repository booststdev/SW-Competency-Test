# T : 테스트케이스(물웅덩이 개수)
T = int(input())
 
for tc in range(1, T+1):
    # N : 물웅덩이 길이
    # K : 개구리가 한번에 점프할 수 있는 최대 거리
    N, K = map(int, input().split())
 
    # arr : 물웅덩이 정보 (1: 나뭇잎 있음, 0: 나뭇잎 없음)
    arr = list(map(int, input().split()))
     
    # pos : 개구리 현재 위치 (0번 인덱스 기준)
    pos = 0
    # count : 연속으로 나뭇잎이 없는 칸 수를 카운트
    count = 0
 
    # 1번 인덱스부터 N-1까지 반복
    for i in range(1, N):
        if arr[i] == 1:
            # 나뭇잎 있으면 점프 가능
            pos = i       # 현재 위치 갱신
            count = 0     # 나뭇잎 없던 칸 수 초기화
        else:
            # 나뭇잎 없으면 count 증가
            count += 1
 
        # 만약 K칸 동안 나뭇잎 없거나 마지막 칸이면
        # 개구리는 K칸 점프 후 물에 빠짐
        if count == K or i == N-1:
            pos += K
            break
 
    # pos가 웅덩이 범위를 넘어가면 최대 이동 거리 N-1로 제한
    if pos >= N:
        pos = N-1
 
    # 결과 출력 (#테스트케이스번호 최대 이동 거리)
    # pos+1 : 1번 위치 기준 출력
    print(f"#{tc} {pos+1}")