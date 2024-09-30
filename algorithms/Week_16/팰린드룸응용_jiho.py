"""
s<=팰린드룸 수 <=e (자리수 2개 이상 수(이 수들도 팰린드룸)들의 곱으로 만들 수 있는 팰린드룸 수 모두 구하기)
ex1. 54388345 => 999 * 55055
ex2.
s,e = 1,500
답: [121,242,363,484]
121 = 11*11
242 = 11*22
363 = 11*33
484 = 22*22
ex3.
s,e = 170000, 180000
답: [171171, 176671, 177771, 178871, 179971]
171*1001
11*16061
11*16161
161*1111
11*16361
"""
def is_palindrome(num): # 팰린드룸인지 확인
    return str(num)==str(num)[::-1] # 역순과 동일한지 확인

def find_palindrome(s,e):
    ans = []
    for num in range(s, e+1):
        if is_palindrome(num): # 해당 숫자가 팰린드룸이라면
            for i in range(10,num): # 두자리 이상 팰린드룸 수
                if num % i == 0: # 해당 숫자로 나누어 떨어지면
                    j = num//i # 나머지 한 숫자 받환
                    if is_palindrome(i) and is_palindrome(j):  # 두 숫자 모두 팰린드 룸이면
                        ans.append(num)
                        break
    ans.sort()
    return ans
s, e = 170000, 180000
print(find_palindrome(s,e))