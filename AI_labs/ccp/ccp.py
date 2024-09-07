import cv2
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from google.colab.patches import cv2_imshow

class WildlifeMonitoringSystem:
    def __init__(self, area_map):
        self.area_map = area_map
        self.graph = self.create_graph(area_map)
        self.animal_positions = []

    def create_graph(self, area_map):
        G = nx.Graph()
        rows, cols = len(area_map), len(area_map[0])
        for r in range(rows):
            for c in range(cols):
                if area_map[r][c] == 1:
                    G.add_node((r, c))
                    if r > 0 and area_map[r-1][c] == 1:
                        G.add_edge((r, c), (r-1, c))
                    if c > 0 and area_map[r][c-1] == 1:
                        G.add_edge((r, c), (r, c-1))
        return G

    def update_animal_positions(self, position):
        self.animal_positions.append(position)

    def bfs(self, start, end):
        queue = deque([start])
        visited = {start: None}
        while queue:
            current = queue.popleft()
            if current == end:
                break
            for neighbor in self.graph.neighbors(current):
                if neighbor not in visited:
                    visited[neighbor] = current
                    queue.append(neighbor)
        path = []
        step = end
        while step is not None:
            path.append(step)
            step = visited[step]
        path.reverse()
        return path

    def dfs(self, start, end):
        stack = [start]
        visited = {start: None}
        while stack:
            current = stack.pop()
            if current == end:
                break
            for neighbor in self.graph.neighbors(current):
                if neighbor not in visited:
                    visited[neighbor] = current
                    stack.append(neighbor)
        path = []
        step = end
        while step is not None:
            path.append(step)
            step = visited[step]
        path.reverse()
        return path

    def plot_graph(self, path_bfs, path_dfs):
        pos = {node: node for node in self.graph.nodes()}
        nx.draw(self.graph, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_color="black", font_weight="bold")
        
        if path_bfs:
            nx.draw_networkx_nodes(self.graph, pos, nodelist=path_bfs, node_color="green")
            nx.draw_networkx_edges(self.graph, pos, edgelist=list(zip(path_bfs, path_bfs[1:])), edge_color="green", width=2)
        
        if path_dfs:
            nx.draw_networkx_nodes(self.graph, pos, nodelist=path_dfs, node_color="red")
            nx.draw_networkx_edges(self.graph, pos, edgelist=list(zip(path_dfs, path_dfs[1:])), edge_color="red", width=2)
        
        plt.show()

def track_animal_in_video(video_path, system):
    cap = cv2.VideoCapture(video_path)
    fgbg = cv2.createBackgroundSubtractorMOG2()
    positions = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        fgmask = fgbg.apply(frame)
        contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Filter small objects
                (x, y, w, h) = cv2.boundingRect(contour)
                cx, cy = x + w // 2, y + h // 2
                positions.append((cy, cx))
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

        cv2_imshow(frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return positions

# Example usage
if __name__ == "__main__":
    area_map = [
        [1, 1, 0, 1],
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 1, 1]
    ]
    
    system = WildlifeMonitoringSystem(area_map)
    
    # Track animal in video
    video_path = '/content/sample_video.mp4'
    positions = track_animal_in_video(video_path, system)
    
    for pos in positions:
        system.update_animal_positions(pos)

    if len(positions) > 1:
        start = positions[0]
        end = positions[-1]
        path_bfs = system.bfs(start, end)
        path_dfs = system.dfs(start, end)
        
        print("BFS Path:", path_bfs)
        print("DFS Path:", path_dfs)
        
        system.plot_graph(path_bfs, path_dfs)
