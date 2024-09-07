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
print(bfs_connected_component(graph,"A"))                  

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
print(bfs_shortest_path(graph,"A","G"))         


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
print(list(all_paths(setGraph, "A","G")))
