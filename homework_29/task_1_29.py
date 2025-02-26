from collections import defaultdict

graph = {
        "A": ["A", "B", "C", "D", "E", "F"],
        "B": ["B", "C", "D", "E", "F"],
        "C": ["C", "D"],
        "D": ["D"],
        "E": ["E", "F"],
        "F": ["F"]
}

connected_components = defaultdict(set)


def dfs(node):
    global connected_components, graph
    if node not in connected_components:
        connected_components[node] = set()
        for next_ in graph[node]:
            dfs(next_)
            connected_components[node] = connected_components[next_]
        connected_components[node].add(node)

for node_ in graph:
    dfs(node_)


connected_comp_as_tuples = map(tuple, connected_components.values())
unique_components = set(connected_comp_as_tuples)
print(unique_components)

