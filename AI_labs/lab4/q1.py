from collections import deque

graph = {
    "1": ["2", "4" ,"3"],
    "2": ["1", "4" ,"3"],
    "3": ["1", "2" ,"4"],
    "4": ["1", "2" ,"3","5"],
    "5": ["4", "6" ,"7","8"],
    "6": ["5", "8" ,"7"],
    "7": ["5", "8" ,"6"],
    "8": ["5", "6" ,"7"],    
}

setGraph = {
    "1": set(["2", "4" ,"3"]),
    "2": set(["1", "4" ,"3"]),
    "3": set(["1", "2" ,"4"]),
    "4": set(["1", "2" ,"3","5"]),
    "5": set(["4", "6" ,"7","8"]),
    "6": set(["5", "8" ,"7"]),
    "7": set(["5", "8" ,"6"]),
    "8": set(["5", "6" ,"7"]),    
}


def dfs(graph, node ,visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs (graph,n,visited)
            return visited
visited = dfs(graph,'1',[])
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
print("\n Find Path from 1 to 6: ")                
print(find_path(graph,'1', '6'))


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
print("\n All Paths of Graph: ")                
print(find_all_paths(graph,'1', '6'))

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
print("\n Shortest Path From 1 to 6: ")                
print(shortest_path(graph,"1","6"))


