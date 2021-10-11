###DFS/BFS###

'''
그래프를 탐색하기 위한 두 가지 알고리즘.
'''

##1.스택
#선입후출, 기본 리스트에 구현되어 있음(append(), pop())

##2.큐
#선입선출, Collections 모듈사용 

#예제
from collections import deque

#큐 구현을 위해 deque 라이브러리 사용
#deque : 스택, 큐의 장점을 모두 채택한 것. 리스트에 비해 데이터 삽입,삭제가 효율적 / 
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #deque([3,7,1,4])
queue.reverse()
print(queue) #deque([4,1,7,3])

##3.재귀함수


##4.DFS
#그래프 2가지 방식 표현법 1)인접행렬 2)인접리스트

#인접행렬방식 예제
INF = 999999999

graph = [
  [0,7,5],
  [7,0,INF],
  [5,INF,0]
]

print(graph)

#인접리스트방식 예제
graph = [[] for _ in range(3)]

#노드0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

#노드1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0,7))

#노드2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0,5))

print(graph)

#DFS 예제
def dfs(graph, v, visited):
  #현재 노드 방문처리
  visited[v] = True
  print(v, end=' ')
  #현재 노드부터 방문시작
  for i in graph[v]:
    if not visited[i]: #방문 안 한 노드만 방문
      dfs(graph, i, visited)


graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9

dfs(graph, 1, visited)

##5.BFS
#BFS 예제
from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited):
  #큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  #현재 노드를 방문 처리
  visited[start] = True

  #큐가 빌 때까지 반복
  while True:
    #큐에서 하나씩 원소 뽑아 출력
    v = queue.popleft()
    print(v, end= ' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)

##6.음료수 얼려 먹기(동빈북 150p)

#<동빈북풀이>

#N,M을 공백으로 구분하여 입력받기
n,m = map(int, input().split())

#2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
  graph.append(map(int,input()))

#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
  #주어진 범위를 벗어나면 즉시 종료
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  
  if graph[x][y] == 0:
    graph[x][y] = 1

    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False

#모든 노드(위치)에 대하여 음료수 채우기(0,0부터 시작)
result = 0
for i in range(n):
  for j in range(m):
    #현재 위치에서 DFS 수행
    if dfs(i,j) == True:
      result += 1

print(result) #정답 출력

##7.미로 탈출(동빈북 152p)

#<동빈북풀이>
from collections import deque

#N,M을 공백으로 구분하여 입력받기
n,m = map(int, input().split())
#2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

#이동할 네 방향 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#BFS 소스코드 구현
def bfs(x,y):
  #큐 구현을 위해 deque사용
  queue = deque()
  queue.append((x,y))

  while queue:
    x,y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      #미로 찾기 공간 벗어난 경우 무시
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

      #벽인 경우 무시
      if graph[nx][ny] == 0:
        continue
        
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))
  return graph[n-1][m-1]

print(bfs(0,0)) 