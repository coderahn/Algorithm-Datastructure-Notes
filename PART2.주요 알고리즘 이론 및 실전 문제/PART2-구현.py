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


##3.왕실의 나이트(동빈북 115p)
#구현-시뮬레이션

#<내풀이1>
#바보같이 h8등 끝에 있는 반례에 대해 생각을 못했다.
#반복화 할 수 있는데 중복 고민을 덜 했다..반성..
val = str(input())
a,b = val[0], int(val[1])
arr = ['a','b','c','d','e','f','g','h']
a = int(arr.index(a)+1)

cnt = 0
if a + 2 > 0 and b + 1 > 0:
  cnt+=1
if a - 2 > 0 and b - 1 > 0:
  cnt+=1
if a + 2 > 0 and b - 1 > 0:
  cnt+=1
if a - 2 > 0 and b + 1 > 0:
  cnt+=1
if a + 1 > 0 and b + 2 > 0:
  cnt+=1
if a - 1 > 0 and b - 2 > 0:
  cnt+=1
if a + 1 > 0 and b - 2 > 0:
  cnt+=1
if a - 1 > 0 and b + 2 > 0:
  cnt+=1

print(cnt)


#<내풀이2 - 일부참고>
val = str(input())
a,b = val[0], int(val[1])
arr = ['a','b','c','d','e','f','g','h']
a = int(arr.index(a)+1)
cnt=0

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2, 1),(1, 2),(-1, 2),(-2, 1)]

for step in steps:
  a2 = a + step[0]
  b2 = b + step[1]

  #h8등의 반례 고려 못함
  # if a2 > 0 and b2 > 0:
  #   cnt+=1

  if a2 > 0 and a2 < 9 and b2 > 0 and b2 < 9:
    cnt+=1

print(cnt)

#<동빈북 풀이>
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2, 1),(1, 2),(-1, 2),(-2, 1)]

result = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]

  if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
    result+=1

print(result)

##4.게임 개발(동빈북 118p)

'''
-책에서는 n방향,m방향을 따로 배열로 선언했지만 나는 하나의 리스트로 선언하여 튜플로 저장하였다.
-책에서는 방향 함수를 따로 빼서 global 변수처리로 d를 조종하였다. 하나의 특성으로 묶을 수 있는건 함수로 처리하려고 하자.
'''
#<내풀이>
n,m = map(int, input().split())
x,y,d = map(int, input().split())
move_array = [(-1,0),(0,1),(1,0),(0,-1)]
map_array = []
for i in range(n):
  map_array.append(list(map(int, input().split())))
move_count = 0
result = 1

while True:
  d-=1
  if d == -1:
    d = 3
  
  dx = x + move_array[d][0]
  dy = y + move_array[d][1]

  if map_array[dx][dy] == 1:
    move_count+=1
  else:
    map_array[dx][dy] = 1
    x = dx
    y = dy
    result += 1
    move_count = 0

  if move_count == 4:
    dx = x - move_array[d][0]
    dy = y - move_array[d][1]

    if map_array[dx][dy] == 1:
      break
    else:
      move_count = 0

print(result)
