###최단경로###

'''
-최단경로 알고리즘 : 특정 지점까지 가장 빠르게 도달하는 방법을 찾는 알고리즘
-보통 그래프 자료구조를 사용(노드, 간선)
-다익스트라 알고리즘(2가지 방법), 플로이드 워셜 알고리즘
1)다익스트라 알고리즘은 특정 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘. 
음의 간선 없을 때 정상 동작. GPS 소프트웨어 알고리즘. 매번 '가장 비용이 적은 노드'를 선택해서 반복하기에 그리디 알고리즘으로 분류.
2)플로이드 워셜 알고리즘(정리예정)
-다익스트라는 O(V^2)의 시간복잡도
'''

##예제 9-1. 간단한 다익스트라 알고리즘(동빈북 237p)

'''
-시간복잡도 O(V^2)
-그리디 알고리즘 분류(현재 앞의 최단거리만 고려)
'''

#입력되는 데이터 많을 시 sys.std.readline 사용
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
#시작 노드 번호 입력받기
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
#방문한 적 있는지 체크 리스트
visited = [False] * (n + 1)
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)


#모든 간선 정보를 입력받기
for _ in range(m):
  a, b, c = map(int, input().split())
  #a->b 비용 c
  graph[a].append((b, c))

#방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1, n + 1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i

  return index

def dijkstra(start):
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]

  #시작 노드를 제외한 전체 n-1개 노드에 대해 반복
  for i in range(n - 1):
    now = get_smallest_node()
    visited[now] = True
    #현재 노드와 연결된 다른 노드 확인
    for j in graph[now]:
      cost = distance[now] + j[1] #현재노드까지의 간선 비용 + 현재노드와 연결된 노드 사이 간선 비용
      if cost < distance[j[0]]:
        distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    print('INFINITY')
  else:
    print(distance[i])

'''
입력
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
출력
0
2
3
1
2
4
'''

##예제 9-2. 개선된 다익스트라 알고리즘(우선순위 큐 사용)

'''
-시간복잡도 O(ElogV)로 이전 버전보다 빠름
-힙정렬 자료구조를 이용한 우선순위 큐 자료구조를 사용
-우선순위 큐 : 우선순위에 따라 pop이 됨. 최단거리를 찾아야 하니 최소힙을 활용
'''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수 입력받기
n,m = map(int, input().split())
#시작 노드 번호를 입력받기
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

#모든 간선 정보 입력받기
for _ in range(m):
  a,b,c = map(int, input().split())
  #a->b 간선 c
  graph[a].append((b,c))

def dijkstra(start):
  q = []
  #시작 노드로 가기 위한 최단경로 0으로 설정하여 큐 삽업
  heapq.heappush(q, (0, start))
  distance[start] = 0
  #q가 빌 때까지 반복
  while q:
    #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist, now = heapq.heappop(q)

    #현재 노드가 처리된 적이 있는 노드면 무시
    if distance[now] < dist:
      continue
    #현재 노드와 연결된 다른 인접한 노드들 확인 
    for i in graph[now]:
      #now까지의 최단거리 비용 + x노드까지 비용
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

#다익스트라 알고리즘 수행
dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
  #도달할 수 없는 경우, 무한 출력
  if distance[i] == INF:
    print('INFINITY')
  else:
    print(distance[i])

'''
입력
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
출력
0
2
3
1
2
4
'''



