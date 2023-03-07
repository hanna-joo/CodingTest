# 백준 온라인 저지 12891, 시간 제한 2초
# DNA 문자열은 모든 문자열에 등장하는 문자가 {'A', 'C', 'G', 'T'}인 문자열을 말한다.
# DNA 문자열의 부분 문자열을 비밀번호로 사용하고자 하는데 보안을 위해 {'A', 'C', 'G', 'T'} 각각 최소 몇 번 들어가야 하는지 조건을 부여할 것이다.
# 임의의 DNA 문자열과 길이, 비밀번호 길이, 최소 조건이 주어졌을 때 만들 수 있는 비밀 번호의 종류의 수를 구하라.
# 문자열 길이 |S|와 비밀번호 길이 |P|(1<=|P|<=|S|<=1,000,000)

# 필요 변수 선언 및 초기화
dna_len, pwd_len = map(int, input().split())
dna_str = list(input())
chk_acgt = list(map(int, input().split()))
answer = 0

# 슬라이딩 윈도우 활용 X
for i in range(dna_len - pwd_len):
    now_pwd = dna_str[i:i+pwd_len-1]
    now_acgt = [now_pwd.count('A'), now_pwd.count('C'), now_pwd.count('G'), now_pwd.count('T')]
    for j in range(4):
        if now_acgt[j] < chk_acgt[j]:
            break
        answer += 1

# 슬라이딩 윈도우 활용 O

# 정답 출력
print(answer)