# 테스트케이스 개수 입력
T = int(input())

# 각 테스트케이스 처리
for tc in range(1, T+1):
    # 방의 개수 N 입력
    N = int(input())

    # 각 방의 포탈 이동 번호 입력 (0-indexed)
    # 예: P_input = [0, 1, 1, 2, 0]
    P_input = list(map(int, input().split()))

    # P 배열 생성: 1번부터 N번 방까지 맞추기 위해 앞에 0 추가
    # P[1] = 1번 방 포탈 번호, P[N] = N번 방 포탈 번호
    P = [0] + P_input

    # dp 배열 준비 (사실 여기서는 시뮬레이션만 사용)
    # dp[i][0] = i번 방 처음 방문했을 때, 최소 포탈 횟수 저장 (사용하지는 않음)
    # dp[i][1] = i번 방 이미 방문했을 때, 최소 포탈 횟수 저장 (사용하지는 않음)
    dp = [[0]*2 for _ in range(N+2)]  # N+2로 N+1 방도 안전하게 처리

    # visited 배열: 각 방 방문 여부 체크
    # visited[i] = False -> 아직 i번 방 방문 안 함
    # visited[i] = True -> 이미 i번 방 방문
    visited = [False]*(N+1)

    # 시작 방 번호는 1번
    room = 1

    # 포탈 사용 횟수 카운트
    cnt = 0

    # 마지막 방(N번 방)에 도착할 때까지 반복
    while room != N:
        if not visited[room]:
            # 처음 방문한 방이면
            visited[room] = True  # 방문 체크
            next_room = P[room]   # 포탈 번호에 적힌 방으로 이동
        else:
            # 이미 방문한 방이면
            next_room = room + 1  # 다음 방으로 이동

        cnt += 1      # 포탈 사용 횟수 증가
        room = next_room  # 이동한 방 번호로 갱신

    # 결과 출력 (테스트케이스 번호와 포탈 사용 횟수)
    print(f"#{tc} {cnt}")
