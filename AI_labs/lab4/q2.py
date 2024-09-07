from collections import deque

graph = {
    "A" : ["B","C","D"],
    "B" : ["A","D","E"],
    "C" : ["A","F",],
    "D" : ["E","A","G"],
    "E" : ["B","D","G"],
    "F" : ["C","G"],
    "G" : ["D","E","F"]
}

setGraph = {
    "A" : set(["B","C","D"]),
    "B" : set(["A","D","E"]),
    "C" : set(["A","F",]),
    "D" : set(["E","A","G"]),
    "E" : set(["B","D","G"]),
    "F" : set(["C","G"]),
    "G" : set(["D","E","F"])
}

def dfs(graph, node ,visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs (graph,n,visited)
            return visited
visited = dfs(graph,'A',[])
print("\n DFS: ")                
print(visited)


def find_path(graph, start, end ,path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph,node, end ,path)
            if newpath:
                return newpath
    return None           
print("\n Find Path from A to E: ")                
print(find_path(graph,'A', 'E'))


def find_all_paths(graph, start, end ,path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph,node, end ,path)
            for newpath in newpaths:
                paths.append(newpath)    
    return paths           
print("\n All Paths of Graph from A to E: ")                
print(find_all_paths(graph,'A', 'E'))

def shortest_path(graph,start,end):
    queue = deque([(start,[start])])
    while queue:
        node,path = queue.popleft()
        if node == end:
            return path
        for neighour in graph[node]:
            if neighour not in path:
                queue.append((neighour,path+[neighour]))
    return None        
print("\n Shortest Path of Graph from A to E: ")                
print(shortest_path(graph,"A","E"))

