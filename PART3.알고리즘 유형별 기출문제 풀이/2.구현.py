###구현 문제###

##07.럭키 스트레이트

#내풀이
n = input()

a = n[0:(len(n)//2)]
b = n[(len(n)//2):]

resultA = 0
resultB = 0
for i in range(len(n)//2):
  resultA += int(a[i])
  resultB += int(b[i])

if resultA == resultB:
  print('LUCKY')
else:
  print('READY')
  
#책풀이
'''
-result변수를 1개로 활용
'''
n = input()
length = len(n)
summary = 0

for i in range(length // 2):
  summary += int(n[i])
for i in range(length // 2):
  summary -= int(n[i])
  
if summary == 0:
  print('LUCKY')
else:
  print('READY')
  
'''
입력
123402
출력
LUCKY
'''

##08.문자열 재정렬

#내풀이
n = input()
alphabet = []
number = 0
for i in n:
  if ord(i) >= 65 and ord(i) <=90:
    alphabet.append(i)
  else:
    number+=int(i)
    
alphabet.sort()

result = ''
for i in alphabet:
  result += i
  
result += str(number)

print(result)

#책풀이

'''
-알파벳 여부는 간단하게 isAlpha()함수 사용
-리스트를 문자열로 변환시 join()함수 사용
'''
data = input()
result = []
value = 0

for x in data:
  #알파벳인 경우
  if x.isAlpha():
    result.append(x)
  #숫자인 경우
  else:
    value += int(x)

#알파벳을 오름차순으로 정렬
result.sort()

#숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
  result.append(str(value))
  
#최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))

'''
입력1
K1KA5CB7
출력1
ABCKK13
입력2
AJKDLSI412K4JSJ9D
출력2
ADDIJJJKKLSS20
'''

##09.문자열 압축(2020카카오코테)

def solutions(s):
  answer = len(s)
  #1개 단위(step)부터 압축 단위를 늘려가면서 확인
  for step in range(1, len(s) // 2 + 1):
    compressed = ''
    prev = s[0:step]
    cnt = 1
    #단위(step) 크기만큼 증가시키며 이전 문자열과 비교
    for j in range(step, len(s), step):
      #이전 상태와 동일하다면 압축 횟수(cnt) 증가
      if prev == s[j : j + step]:
        cnt += 1
      #이전 상태와 다르다면
      else:
        compressed += str(cnt) + prev if cnt >= 2 else prev
        prev = s[j : j + step]
        cnt = 1
    
    #남아있는 문자열 처리
    compressed += str(cnt) + prev if cnt >= 2 else prev
    #압축문자열 짧은 것으로 갱신
    answer = min(answer, len(compressed))
  return answer

print(solutions(input()))

'''
입력
aabbaccc
출력
7
'''

##11.뱀

'''
-꼬리정보에 대해 스택자료구조로 하는 것에 대해 생각 못함..3개중 2개만 통과
-책처럼 로직이 많거나 반복되면 함수로 빼자
'''

#책풀이(문제 327p)
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] #맵정보
info = [] #방향 회전 정보

#맵정보(사과있는곳 1로 표시)
for _ in range(k):
  a,b = map(int, input().split())
  data[a][b] = 1
  
#방향 회전 정보 입력
l = int(input())
for _ in range(l):
  x,c = input().split()
  info.append((int(x),c))
  
#처음에는 오른쪽을 보고있으므로(동남서북)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction, c):
  if c == 'L':
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4
  return direction

def simulate():
  x,y = 1,1 #뱀의 머리 위치
  data[x][y] = 2 #뱀이 존재하는 위치는 2로 표시
  direction = 0
  time = 0 #시작한뒤에 지난 '초'
  index = 0 #다음 회전 정보
  q = [(x,y)] #뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    #맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
    if 1 <= nx and 1 <= ny and nx <= n and ny <= n and data[nx][ny] != 2:
      #사과 없으면 이동 후 꼬리 제거
      if data[nx][ny] == 0:
        data[nx][ny] = 2
        q.append((nx,ny))
        px,py = q.pop(0)
        data[px][py] = 0
      #사과가 있다면 이동 후에 꼬리 유지
      if data[nx][ny] == 1:
        data[nx][ny] = 2
        q.append((nx,ny))
    #벽이나 뱀의 몸통과 부딪혔다면    
    else:        
      time += 1
      break
    x,y = nx, ny #다음 위치로 머리를 이동
    time += 1
    if index < l and time == info[index][0]:
      direction = turn(direction, info[index][1])
      index += 1
  return time

print(simulate())