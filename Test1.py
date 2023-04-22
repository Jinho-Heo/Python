########################################################################
# Date : '23.4/19
# Source : 백준 10988
# Difficulty : D(발상 떠올리기 쉽고,특별한 알고리즘 없이 기본 문법 지식만으로 구현 가능)
# Lesson & Learn :
# 1) input() 함수 사용하여 문자열 입력 받기
# 2) 반복문에서 break문 과 continue문 이용해서 탈출 및 반복 지속
########################################################################

word = input()
#print(word)

n = len(word)
#print(n)

a = 1

for i in range(n) :
    if(word[i] == word[n-i-1]) : continue
    else :
        a = 0
        break

print(a)





