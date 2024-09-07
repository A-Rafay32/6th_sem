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

def bfs_connected_component(graph,start):
    explored = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in explored :
                explored.append(node)
                neighbours = graph[node]

                for neighbour in neighbours:
                     queue.append(neighbour)
    return explored
print("\nBFS Traversal: ")
print(bfs_connected_component(graph,"1"))                  

def bfs_shortest_path(graph,start,goal):
   explored = []
   queue = [[start]]

   while queue:
      path = queue.pop()
      node=  path[-1]
      if node not in explored :
         neighbours = graph[node]
         for neighbour in neighbours:
            new_path = list(path)
            new_path.append(neighbour)
            queue.append(new_path)
            if neighbour == goal:
               return new_path
            explored.append(node)
   return "connected path doesn't exist"
print("\nBFS Shortest Path: ")
print(bfs_shortest_path(graph,"1","6"))         


def all_paths(graph,start,goal):
    queue = [(start ,[start])]
    while queue:
        (vertex,path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next,path+[next])) 

print("\n All Paths of Graph: ")                
print(list(all_paths(setGraph, "1","6")))
s