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

##03.문자열 뒤집기

#내풀이(잘못품 다시 풀자)
n=input()
checker = False
result = 0
now = '0'
if n.count('0') > n.count('1'):
  now = '1'
else:
  now = '0'

for i in range(len(n)):
  if n[i] == now:
    checker = True

  if checker == True:
    if n[i] != now:
      checker = False
      result += 1
    if i == len(n) - 1:
      result += 1

print(result)

#책풀이
data = input()
count0 = 0 #전부 0으로 바꾸는 경우
count1 = 0 #전부 1로 바꾸는 경우

#첫번째 원소 처리
if data[0] == '1':
  count0 += 1
else:
  count1 += 1

#두번째 원소부터 모든 원소 확인  
for i in range(len(data) - 1):
  #앞과 다른 숫자인 경우
  if data[i] != data[i + 1]:
    #다음 숫자가 1로 바뀌는 경우
    if data[i + 1] == '1':
      count0 += 1
    #다움 숫자가 0으로 바뀌는 경우
    else:
      count1 += 1
      
#0으로바꾸기, 1로바꾸기 횟수 중 더 작은 것을 print
print(min(count0,count1))

'''
입력
0001100
출력
1
'''

##04.볼링공 고르기

#내풀이
#->답만 나오고 조합의 경우만 생각해서 풀어서 제대로 된 풀이가 아닐듯
n,m = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
for i in range(len(arr)):
  for j in range(i + 1, len(arr)):
    if arr[i] != arr[j]:
      result += 1
      
print(result)


#책풀이
n,m = map(int, input().split())
data = list(map(int, input().split()))

#1부터 10까지 무게를 담을 리스트
array = [0] * 11

#각 무개에 해당하는 볼링공 개수 카운트
for i in data:
  array[i] += 1
  
result = 0
#1부터 m까지 각 무게에 대한 처리
for i in range(1, m + 1):
  n -= array[i] #A가 선택할 볼링공 개수 제외
  result += array[i] * n #B가 선택하는 경우와 곱하기
  
print(result)

'''
입력
5 3
1 3 2 3 2
출력
8
'''