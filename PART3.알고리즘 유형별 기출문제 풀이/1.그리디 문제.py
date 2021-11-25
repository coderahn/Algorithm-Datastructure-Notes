###그리디 문제###

##01.모험가 길드

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