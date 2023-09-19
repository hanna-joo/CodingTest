# 나는야 포켓몬 마스터 이다솜 (s4, 34.027%)
# source : https://www.acmicpc.net/problem/1620
# keyword : 딕셔너리, 해시를 사용한 집합과 맵
# return : 포켓몬 번호에 맞는 이름 또는 이름에 맞는 번호 맞추기

"""
1. 문제
- 포켓몬 번호가 물어보면 이름을 답하고 포켓몬 이름을 물어보면 번호를 답하라

2. 입력 및 제한
- 포켓몬 개수 N, 맞춰야 하는 문제 개수 M (1<=N,M<=100,000)
- 1번부터 N번까지 포켓몬 이름 (2<=이름길이<=20)
    - 첫 글자만 대문자, 나머지는 소문자 / 마지막 문자만 대문자
- M개의 줄에 문제

3. 로직
- 딕셔너리 2개 활용 -> 208ms
- 이름 찾는 것은 입력 값 자체를 활용해도 좋음 -> 188ms
"""


N, M, *inputs = open(0).read().split()
#find_name = dict(), 
find_num = dict()

for i in range(int(N)):
    #find_name[i+1] = inputs[i]
    find_num[inputs[i]] = i+1
    
for q in inputs[int(N):]:
    if q.isdecimal():
        print(inputs[int(q)-1])
        #print(find_name[int(q)])
    else:
        print(find_num[q])


"""
테스트케이스

26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna
---
Pikachu
26
Venusaur
16
14
"""