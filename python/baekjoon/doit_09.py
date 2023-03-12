# 백준 온라인 저지 12891, 시간 제한 2초
# DNA 문자열은 모든 문자열에 등장하는 문자가 {'A', 'C', 'G', 'T'}인 문자열을 말한다.
# DNA 문자열의 부분 문자열을 비밀번호로 사용하고자 하는데 보안을 위해 {'A', 'C', 'G', 'T'} 각각 최소 몇 번 들어가야 하는지 조건을 부여할 것이다.
# 임의의 DNA 문자열과 길이, 비밀번호 길이, 최소 조건이 주어졌을 때 만들 수 있는 비밀 번호의 종류의 수를 구하라.
# 문자열 길이 |S|와 비밀번호 길이 |P|(1<=|P|<=|S|<=1,000,000)

# 슬라이딩 윈도우 활용 X
'''
dna_len, pwd_len = map(int, input().split())
dna_str = list(input())
chk_acgt = list(map(int, input().split()))
answer = 0

for i in range(dna_len - pwd_len):
    now_str = dna_str[i:i+pwd_len-1]
    now_acgt = [now_str.count('A'), now_str.count('C'), now_str.count('G'), now_str.count('T')]
    for j in range(4):
        if now_acgt[j] < chk_acgt[j]:
            break
        answer += 1
'''

# 슬라이딩 윈도우 활용 O
# 전역 변수 선언
chk_acgt = [0] * 4 # 비밀번호 되기 위한 최소 a,c,g,t 개수
now_acgt = [0] * 4 # 현재 문자열의 a,c,g,t 개수
pass_cnt = 0       # 최소 조건 충족 여부 수

# 함수 선언
def add_char(c): # 슬라이딩 윈도우에 추가된 문자 처리
    global chk_acgt, now_acgt, pass_cnt
    if c == 'A':
        now_acgt[0] += 1
        if now_acgt[0] == chk_acgt[0]:
            pass_cnt += 1
    elif c == 'C':
        now_acgt[1] += 1
        if now_acgt[1] == chk_acgt[1]:
            pass_cnt += 1
    elif c == 'G':
        now_acgt[2] += 1
        if now_acgt[2] == chk_acgt[2]:
            pass_cnt += 1
    elif c == 'T':
        now_acgt[2] += 1
        if now_acgt[2] == chk_acgt[2]:
            pass_cnt += 1

def remove_char(c): # 슬라이딩 윈도우에서 제거된 문자 처리
    global chk_acgt, now_acgt, pass_cnt
    if c == 'A':
        if now_acgt[0] == chk_acgt[0]:
            pass_cnt -= 1
        now_actg -= 1
    elif c == 'C':
        if now_acgt[1] == chk_acgt[1]:
            pass_cnt -= 1
        now_acgt -= 1        
    elif c == 'G':
        if now_acgt[2] == chk_acgt[2]:
            pass_cnt -= 1
        now_acgt -= 1
    elif c == 'T':
        if now_acgt[3] == chk_acgt[3]:
            pass_cnt -= 1
        now_acgt -= 1

# 필요 변수 선언
dna_len, pwd_len = map(int, input().split())
dna_str = list(input())
chk_acgt = list(map(int, input().split()))
answer = 0

# 최소 개수가 0인 문자열은 조건 충족
for i in range(4):
    if chk_acgt[i] == 0:
        pass_cnt += 1

# 첫번째 문자열 처리
for i in range(pwd_len):
    add_char(dna_len[i])
if pass_cnt == 4:
    answer += 1

# 슬라이딩 윈도우로 한 글자씩 뒤로 가기
for i in range(pwd_len, dna_len):
    add_char(dna_str(i))
    remove_char(dna_str(i-pwd_len))
    if pass_cnt == 4:
        answer += 1

# 정답 출력
print(answer)