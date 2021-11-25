###그리디 문제###

##01.모험가 길드

'''
-굳이 deque를 썼는데 쉽게 푸는 연습을 하자
'''

#내풀이
from collections import deque

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

q = deque(arr)

result = 0
while q:
  tempCnt = 0 #그룹원 수
  last = 0 #마지막 그룹원
  now = q[0]
  for _ in range(now):
    last = q.popleft()
    tempCnt += 1

  if tempCnt < last: #마지막 그룹원 n보다 그룹원수가 적다면 그룹핑 불가하므로 break 
    break

  result += 1

print(result)

'''
입력
5
2 3 1 2 2 
출력
2
'''

##02.곱하기 혹은 더하기

'''
-주어진 입력 값 숫자 사이사이 + 또는 *을 이용해 가장 큰 수 만들기
-0인 경우에만 더하고 계속 곱하면 됨
'''

#내풀이
arr = list(map(int, input()))
arr.sort(reverse=True)
result = arr[0]

for i in range(1, len(arr)):
  if result * arr[i] == 0:
    result += arr[i]
  else:
    result *= arr[i]

print(result)

'''
입력
02984
출력
567
'''