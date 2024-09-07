#finding a path between 2 nodes
graph = {"1": ["4","2","3"],
         "2": ["1","4","3"],
         "3": ["2","1","4"],
         "4": ["1","2","3","5"],
         "5": ["4","6","7","8"],
         "6":["5","7","8"],
         "7":["5","6","8"]
         }
def find_all_path(graph,start,end,path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return []
    paths =[]
    for node in graph[start]:
        if node not in path :
            newpaths = find_all_path(graph,node,end,path)
            for newpath in newpaths:
                paths.append(newpath)
            
    return paths
 
print("\n\nfinding a path between 2 nodes")
print("\n\nthe path between two nodes is :" , find_all_path(graph ,'1','7'))

 
#Find shortest path between nodes 1 and 7.

def find_shortest_path(graph,start,end,path=[]):
    path=path+[start]
    if start==end:
        return path
    if start not in graph:
        return []
    shortest=[]
    for node in graph[start]:
        if node not in path:
            newpath=find_shortest_path(graph,node,end,path)
            if newpath:
                if not shortest or len(newpath)<len(shortest):
                    shortest=newpath
    return shortest
path=find_shortest_path(graph,'1','7')
if path:
    print("\npath between",'1',"and",'7',":",path)
else:
    print("\nno path found between",'1',"and",'7')
print("\nFind shortest path between nodes 1 and 7." , find_shortest_path(graph, 1,7))


#e)	Determine cycles in graphs.

def has_cycle(graph):
    visited = set()

    def dfs(node, visited, path):
        if node in visited:
            return True  # Cycle detected
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor in path:
                return True  # Cycle detected
            if dfs(neighbor, visited, path + [node]):
                return True
        path.remove(node)
        return False

    for node in graph:
        if dfs(node, visited, []):
            return True
    return False

print("\nCycle exists:", has_cycle(graph))

 
#f)	Add an edge named 9.
graph = {
    "1": ["4", "2", "3"],
    "2": ["1", "4", "3"],
    "3": ["2", "1", "4"],
    "4": ["1", "2", "3", "5"],
    "5": ["4", "6", "7", "8"],
    "6": ["5", "7", "8"],
    "7": ["5", "6", "8"]
}

def add_edge(graph, edge):
    edge = set(edge)
    n1, n2 = tuple(edge)
    if n1 in graph:
        graph[n1].append(n2)
    return graph

print("\nadd an edge : ", add_edge(graph, {"9", "6"}))
print("\nNew graph: ",graph)

 
#g)	Find degree of vertex 4.
graph = {
    "1": ["4", "2", "3"],
    "2": ["1", "4", "3"],
    "3": ["2", "1", "4"],
    "4": ["1", "2", "3", "5"],
    "5": ["4", "6", "7", "8"],
    "6": ["5", "7", "8"],
    "7": ["5", "6", "8"]
}
def find_degree(graph,node):
    degree=0
    t=[]
    for neighbour in graph[node]:
        t.append(neighbour)
        degree=degree+1
    return degree

Degree=find_degree(graph,"4")
print("\ndegree of the vertex : ",Degree)

 
#h)	Find if the graph is connected.

graph = {
    "1": ["4", "2", "3"],
    "2": ["1", "4", "3"],
    "3": ["2", "1", "4"],
    "4": ["1", "2", "3", "5"],
    "5": ["4", "6", "7", "8"],
    "6": ["5", "7", "8"],
    "7": ["5", "6", "8"]
}
def graph_connected(graph, seen_node=None, start=None):
    if seen_node is None:
        seen_node = set()
    nodes = list(graph.keys())
    if not start:
        start = nodes[0]
    if len(seen_node) < len(nodes):
        for othernodes in graph[start]:
            if othernodes not in seen_node:
                seen_node.add(othernodes)
                if graph_connected(graph, seen_node, othernodes):
                    return True
    else:
        return True
    return False

conn = graph_connected(graph)
if conn:
    print("\nThe graph is connected")
else:
    print("\nThe graph is not connected")
