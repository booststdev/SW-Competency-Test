# 테스트 케이스 개수를 입력받음
T = int(input())

# 1부터 T까지 반복 (각 테스트 케이스 처리)
for tc in range(1, T+1):
    # N: 주어진 숫자열 n의 길이 입력
    N = int(input())
    # n: 숫자열 n 입력 (문자열로 받아서 각 자리 숫자를 리스트로 변환)
    # 예: "1234567890" -> [1,2,3,4,5,6,7,8,9,0]
    n = list(map(int, input().strip()))   

    # M: 맞춰야 하는 암호코드 m의 길이 입력
    M = int(input())
    # m: 암호코드 m 입력 (마찬가지로 문자열 -> 숫자 리스트)
    # 예: "2467" -> [2,4,6,7]
    m = list(map(int, input().strip()))   

    # idx: m에서 현재 확인 중인 위치 (0부터 시작)
    idx = 0
    # answer: 암호코드가 n 안에서 부분수열로 존재하는지
    # 표시 (0=불가, 1=가능)
    # 일단 안된다고 가정
    answer = 0

    # n 안의 숫자를 순서대로 확인
    for num in n:
        # 현재 m[idx]와 일치하면 idx 증가
        # idx < M 조건: m 범위 초과 방지
        if idx < M and num == m[idx]:
            idx += 1

    # 반복이 끝난 후, idx가 M과 같으면
    # m의 모든 숫자를 순서대로 찾았다는 뜻 -> 부분수열 존재
    if idx == M:
        answer = 1

    # 결과 출력 (예: #1 0, #2 0)
    print(f"#{tc} {answer}")
