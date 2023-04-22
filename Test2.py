########################################################################
# Date : '23.4/20
# Source : 백준 2941
# Difficulty : D(발상 떠올리기 쉽고,특별한 알고리즘 없이 기본 문법 지식만으로 구현 가능)
# Lesson & Learn :
# 1) 스트링 인덱스 함수 이용하여 찾은 값에 해당하는 인덱스 리턴 받기
# 2)
########################################################################

import sys

a = sys.stdin.readline().strip()

#print(a)

#b = a.index('a')

#print(b)

'''''
c = [i.index for i in a if (i =='a')]
print(c)
'''

cnt = 0

for i in range(len(a)) :
    if(a[i] == 'c') :
      if(a[i+1] == '=' or a[i+1] == '-') : cnt += 1
    elif(a[i] == 'd') :
      if(a[i+1] == '-') : cnt += 1
      elif(a[i+1] == 'z'): 
        if(a[i+2] == '=') : cnt += 1  
    elif(a[i] == 'l') :
      if(a[i+1] == 'j') : cnt += 1
    elif(a[i] == 'n') :
      if(a[i+1] == 'j') : cnt += 1
    elif(a[i] == 's') :
      if(a[i+1] == '=') : cnt += 1
    elif(a[i] == 'z') :
      if(a[i+1] == '=') : cnt += 1

print(len(a)-cnt)