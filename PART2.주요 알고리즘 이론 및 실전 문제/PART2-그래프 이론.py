###그래프 이론###

'''
[INTRO]
-코테에서 출제 비중은 낮지만 알아둬야할 그래프 관련 이론
-서로소 집합 자료구조, 신장트리 알고리즘(크루스칼 알고리즘),위상정렬
[앞내용 복습]
-다익스트라 최단 경로 알고리즘은 우선순위 큐 자료구조 사용 / 그래프 구현 방법 중 '인접 리스트' 방식 사용
-플로이드 워셜 알고리즘은 다이나믹 프로그래밍 점화식 방식 사용 / 그래프 구현 방법 중 '인접 행렬' 방식 사용
-노드의 개수가 적은 경우 -> 플로이드 워셜 / 노드와 간선 개수가 많은 경우 -> 다익스트라
[서로소 집합]
-서로소 집합 : 공통 원소 없는 집합 ex) {1,2},{3,4}
-서로소 집합 자료구조 : 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
-union, find 연산으로 조작 가능
-union : 2개 원소가 포함된 집합을 하나의 집합으로 합치는 연산
-find : 특정 원소가 속한 집합이 어떤 집합인지 알려주는 연산
-트리 자료구조 이용
'''

##[서로소 집합]

##10-1 예제.기본적인 서로소 집합 알고리즘

#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  #루트 노드가 아니라면 루트노드를 찾을 때까지 재귀적 호출
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

#노드의 개수, 간선(union 연산)의 개수
v, e = map(int, input().split())
parent = [0] * (v + 1) #부모테이블 초기화

#부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
  parent[i] = i
  
#union 연산을 각각 수행
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

#각 원소가 속한 집합을 출력
print('각 원소가 속한 집합: ', end ='')
for i in range(1, v + 1):
  print(find_parent(parent, i), end=' ')

print()

#부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
  print(parent[i], end=' ')

'''
입력
6 4
1 4
2 3
2 4
5 6
출력
각 원소가 속한 집합: 1 1 1 1 5 5 
부모 테이블: 1 1 2 1 5 5
'''

##10-3 예제.개선된 서로소 집합 알고리즘(경로압축기법으로 find 함수 변경)

#특정 원소가 속한 집합을 찾기(경로압축기법)
def find_parent(parent, x):
  #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
  

#노드의 개수와 간선(union 연산) 개수 입력받기
v,e = map(int, input().split())
parent = [0] * (v + 1) 

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
  parent[i] = i

#union 연산 수행
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)  

#각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
  print(find_parent(parent, i), end=' ')

print()

#부모 테이블 내용 출력
for i in range(1, v + 1):
  print(parent[i], end=' ')
  
'''
입력
6 4
1 4
2 3
2 4
5 6
출력
각 원소가 속한 집합: 1 1 1 1 5 5 
부모 테이블: 1 1 1 1 5 5
'''

'''
-서로소 집합을 활용하면 무방향 그래프 내에서의 사이클 판별 가능
-방향 그래프에서의 사이클 여부는 DFS 사용(책에서 안 다룸)
'''

#예제 10-4.서로소 집합을 활용한 사이클 판별

#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

#노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
  parent[i] = i
  
cycle = False #사이클 발생 여부

for i in range(e):
  a, b = map(int, input().split())
  #사이클 발생시 종료
  if find_parent(parent, a) == find_parent(parent, b):
    cycle = True
    break
  #사이클 미발생시 합집합(union)
  else:
    union_parent(parent, a, b)
    
if cycle:
  print('사이클이 발생했습니다.')
else:
  print('사이클이 발생하지 않았습니다.')

'''
입력
3 3
1 2
1 3
2 3
출력
사이클이 발생했습니다.
'''

##[신장트리]

'''
-신장트리 : 하나의 그래프가 있을 때 모든 노드를 포함시키면서 사이클이 존재하지 않는 부분 그래프
-n개의 모든 도시를 연결할 때 최소비용으로 연결하기 -> 최소신장트리 알고리즘(크루스칼 알고리즘)
-크루스칼 알고리즘을 사용하면 가장 적은 비용으로 모든 노드 연결(그리디 알고리즘으로 분류)
1)모든 간선에 대하여 정렬 수행
2)가장 거리 짧은 간선부터 집합에 포함시키기(a,b의 루트노드가 같지 않을 때 union_parent)
'''

##예제10-5. 크루스칼 알고리즘 

#특정 원소가 속한 집합 찾기
def find_parent(parent, x):
  #루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
  parent[i] = i

#모든 간선 정보 입력
for i in range(e):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))
  
#간선을 비용순으로 정렬
edges.sort()

#간선을 하나씩 확인하기
for edge in edges:
  cost, a, b = edge
  #사이클 발생하지 않는 경우에만 집합에 포함(두 노드가 같은 루트 노드를 공유하지 않을 때)
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
    
print(result)

'''
입력
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
출력
159
'''

##[위상정렬]

'''
-방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'
-ex)선수과목을 고려한 학습 순서 설정(자료구조->알고리즘->고급알고리즘)
-진입차수(indegree) : 특정한 노드에 들어오는 간선의 개수
-시간복잡도 O(V+E) : 차례대로 모든 노드(V) 확인을 하면서 해당 노드에서 출발하는 간선(E)을 차례대로 제거해야 함
-진입차수가 0인 노드를 먼저 큐에 삽입 -> 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거 -> 새롭게 진입차수 0된 노드 큐에 넣음 -> 반복..
-모든 원소를 방문하기 전 큐가 빈다면 사이클 존재(위상정렬문제는 사이클이 없다고 명시하는 경우가 많음)
-큐에서 빠져나간 노드를 순서대로 출력하면 위상정렬 수행결과
'''

#예제10-6.위상정렬

from collections import deque

#노드의 개수, 간선의 개수 입력받기
v, e = map(int, input().split())
#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
#각 노드에 연결된 간선 정보를 담기위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(v + 1)]

#방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  #진입차수를 1 증가
  indegree[b] += 1
  
#위상 정렬 함수
def topology_sort():
  result = []
  q = deque()
  
  #처음 시작하는 진입차수가 0인 노드 큐에 삽입
  for i in range(1, v + 1):
    if indegree[i] == 0:
      q.append(i)
  
  #큐가 빌 때까지 반복
  while q:
    #큐에서 원소 꺼내기
    now = q.popleft()
    result.append(now)
    
    #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    for i in graph[now]:
      indegree[i] -= 1
      #새롭게 진입차수가 0이 되는 노드 큐 삽입
      if indegree[i] == 0:
        q.append(i)
        
  #위상정렬 수행결과 출력
  for i in result:
    print(i, end=' ')
    
topology_sort()