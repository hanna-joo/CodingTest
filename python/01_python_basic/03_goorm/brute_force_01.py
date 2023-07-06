# 제곱암호
# keyword : 문자열, 아스키 코드, ord(), chr()
# return : 소문자+숫자 번갈아 나타나는 문자열에서 소문자의 다음 문자로 이동을 숫자의 제곱 번만큼 수행하는 복호화

"""
1. 인코딩
- 정해진 정보를 비트의 조합으로 표현하는 것

2. ASCII
- 문자를 인코딩하는 방식 중 하나
- 문자를 특정 비트의 집합으로 표현하는 것
- ord() : 특정 문자 > ASCII 값 (정수)
- chr() : ASCII 값 > 해당 문자
"""


def decryption_1(password):
    decryption = ''
    for i in range(0, len(password)-1, 2):
        char, num = password[i], int(password[i+1])
        new_ascii = (ord(char) + (num**2))
        while new_ascii > 122:
            new_ascii = (new_ascii % 123) + 97
        char = chr(new_ascii)
        decryption += char

    return decryption


def decryption_2(password):
    decryption = ''
    for i in range(0, len(password), 2):
        char, num = password[i], int(password[i+1])
        new_ascii = (ord(char) - ord('a') + (num**2)) % 26 + ord('a')
        char = chr(new_ascii)
        decryption += char

    return decryption


if __name__ == '__main__':

    import sys
    input = sys.stdin.readline

    test_cases = ['a1b2c3e4', 'z2y2z1'] # bflu, dca
    test_cases.append(input().rstrip())

    for case in test_cases:
        print(decryption_1(case))
        print(decryption_2(case))