
#a)	Find isolated nodes.
graph = {
    "Mayor's House": ["Bakery","Brewery"],
    "Bakery": ["Mayor's House", "Mc Fane's Farm"],
    "Brewery": ["Mayor's House", "Mc Fane's Farm","Inn"],
    "Mc Fane's Farm": ["Bakery", "Brewery","Thomas Farm"],
    "Thomas Farm": ["Mc Fane's Farm"],
    "Dry Cleaner": ["Inn","City Hall"],
    "City Hall": ["Dry Cleaner", "Library"],
    "Inn":["Brewery","Dry Cleaner","Library"],
    "Library":["Inn","City Hall"],
}
def find_isolated(graph):
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated +=node
    return isolated

print("\nthe isolated node is ", find_isolated(graph))

 

#b)	Find path between two vertex/node Thomas’ Farm and Library.


def find_path(graph,start,end,path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    
    for node in graph[start]:
        if node not in path :
            newpath = find_path(graph,node,end,path)
            
            if newpath:
                return newpath
    return None

print("\nthe path between two nodes is :" , find_path(graph ,'Thomas Farm','Library'))

 
#c)	Find all paths in graph.


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
 

print("\nthe path between two nodes is :" , find_all_path(graph ,'Thomas Farm','Library'))

 
#d)	Finding shortest path between nodes Thomas’ Farm and Library.


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
path=find_shortest_path(graph,'Thomas Farm','Library')
if path:
    print("\npath between",'Thomas Farm',"and",'Library',":",path)
else:
    print("\nno path found between",'Thomas farm',"and",'Library')

 
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

 
#f)	Add an edge named John’s House.

def add_edge(graph, edge):
    edge = set(edge)
    n1, n2 = tuple(edge)
    if n1 in graph:
        graph[n1].append(n2)
    return graph

print("\nadd an edge : ", add_edge(graph, {"Thomas Farm","John's House"}))
print("\nNew graph: ",graph)

 
#g)	Find degree of vertex Bakery.


def find_degree(graph,node):
    degree=0
    t=[]
    for neighbour in graph[node]:
        t.append(neighbour)
        degree=degree+1
    return degree

Degree=find_degree(graph,"Bakery")
print("\ndegree of the vertex : ",Degree)

 
#h)	Find if the graph is connected.

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
