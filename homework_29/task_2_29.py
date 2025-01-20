graph = {
    'S': ['A', 'B'],
    'A': ['B','C', 'D'],
    'B': ['C'],
    'C': ['D'],
    'D': []
}

visited_paths = {}
queue = []
goal = 'D'
def bfs(visited, graph, node):
  visited[node] = node
  queue.append(node)
  while queue:
    s = queue.pop(0)
    if(s == goal):
        break

    for n in graph[s]:
        if n not in visited:
            queue.append(n)
            visited[n] = s

  if goal in visited:
    path = [goal]
    curr = goal
    while curr != node:
       curr = visited[curr]
       path.append(curr)
    path.reverse()
    print(path)
  else:
    print("No path")

bfs(visited_paths,graph,'S')
