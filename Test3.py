########################################################################
# Date : '23.4/22
# Source : 백준 2941
# Difficulty : D(발상 떠올리기 쉽고,특별한 알고리즘 없이 기본 문법 지식만으로 구현 가능)
# Lesson & Learn :
# 1) 출력되는 값에 제한값 있을 경우 조건문 연습
# 2) 2개의 정수값 두 개의 변수에 각각 입력 받기 연습
# 3) 2개의 변수값 스페이스로 띄워서 한줄에 출력하기
########################################################################

import sys

a , b = map(int,sys.stdin.readline().split())

if(b-45 < 0) : 
  b = 60-abs(b-45)
  a -= 1
  if(a<0) : a+=24
else :
  b -= 45

print('{} {}'.format(a,b))

