###구현###

#완전탐색, 시뮬레이션을 포함
#-완전탐색 : 모든 경우의 수를 주저 없이 다 계산하는 해 결 방법
#-시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행

##1.상하좌우(동빈북 110p)
#구현중에서도 시뮬레이션 문제(개체를 차례대로 이동시키는 문제)
#<내풀이>
n = int(input())
a,b=0,0 #굳이 0으로 하고 마지막에 1을 합쳤다. 리스트 등을 사용하는게 아니면 문제 흐름에 맞춰야 한다.
arr = list(input().split()) #그냥 list() 안 해도 리스트로 변수에 대입

for val in arr:
  if val == 'R':
    b+=1
  elif val == 'L':
    b-=1
  elif val == 'U':
    a-=1
  else:
    a+=1
  
  if a<0:
    a+=1
  if b<0:
    b+=1

print(a+1,b+1)

#<동빈북 풀이>
n = int(input())
x,y = 1, 1
plans = input().split()

#L, R, U, D에 따른 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

#이동계획을 하나씩 확인
for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]

  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue

  #Q.nx, ny를 어떻게 사용하나요?
  x = nx 
  y = ny

print(x, y)


##2.시각(동빈북 114p)

#내풀이와 동빈북풀이 답이 다른 이유 잘 생각해보기
#<내풀이>
hour = int(input())
cnt=0
for h in range(hour+1):
  if '3' in str(h):
        cnt+=1
  for m in range(60):
    if '3' in str(m):
        cnt+=1
    for s in range(60):
      if '3' in str(s):
        cnt+=1

print(cnt)

#<동빈북풀이>
hour = int(input())
cnt=0
for h in range(hour+1):
  for m in range(60):
    for s in range(60):
      if '3' in str(h) + str(m) + str(s):
        cnt+=1

print(cnt)