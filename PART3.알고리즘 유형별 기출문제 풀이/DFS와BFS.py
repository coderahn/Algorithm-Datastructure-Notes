###DFS/BFS 문제###

##15.특정 거리의 도시 찾기(p339)

'''
-모든 간선의 비용이 동일할 때는 너비우선탐색(BFS) 이용하여 최단거리 찾을 수 있음(도시간 거리 1로 동일)
-문제조건 노드개수(N) 최대 300,000 / 간선개수(M) 최대 1,000,000 -> BFS 시간복잡도 O(N+M)으로 동작
'''

from collections import deque

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
visited = [False] * (n + 1)
distance = [-1] * (n + 1)
#출발도시는 0으로 설정
distance[x] = 0

#BFS
queue = deque([x])
while queue:
  now = queue.popleft()
  for i in graph[now]:
    #미방문 노드만 확인
    if distance[i] == -1:
      queue.append(i)
      distance[i] = (distance[now] + 1)
  
if k not in distance:
  print(-1)
else:
  for i in range(len(distance)):
    if distance[i] == k:
      print(i)

'''
입력
4 4 1 1
1 2
1 3
2 3
2 4
출력
2
3
'''
  
  