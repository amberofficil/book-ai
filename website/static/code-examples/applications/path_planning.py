import numpy as np
import matplotlib.pyplot as plt

class GridPathPlanner:
    """A simple path planner using A* algorithm for grid-based environments."""
    
    def __init__(self, grid):
        self.grid = grid  # 2D array where 0 = free space, 1 = obstacle
        self.rows, self.cols = grid.shape
    
    def heuristic(self, a, b):
        """Manhattan distance heuristic."""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def get_neighbors(self, pos):
        """Get valid neighbors for a position."""
        r, c = pos
        neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1),  # up, down, right, left
                     (r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1)]  # diagonals
        
        valid_neighbors = []
        for nr, nc in neighbors:
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] == 0:
                valid_neighbors.append((nr, nc))
        
        return valid_neighbors
    
    def plan_path(self, start, goal):
        """Plan path from start to goal using A*."""
        open_set = {start}
        came_from = {}
        
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}
        
        while open_set:
            current = min(open_set, key=lambda x: f_score.get(x, float('inf')))
            
            if current == goal:
                # Reconstruct path
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]  # Return reversed path
            
            open_set.remove(current)
            
            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, goal)
                    
                    if neighbor not in open_set:
                        open_set.add(neighbor)
        
        return []  # No path found

# Example usage
if __name__ == "__main__":
    grid = np.array([
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ])

    planner = GridPathPlanner(grid)
    start = (0, 0)
    goal = (7, 7)
    path = planner.plan_path(start, goal)

    print(f"Path from {start} to {goal}: {path}")

    # Visualize the path
    viz_grid = grid.astype(float)
    for r, c in path:
        if (r, c) != start and (r, c) != goal:
            viz_grid[r, c] = 0.5  # Mark path cells

    viz_grid[start[0], start[1]] = 0.3  # Start in light green
    viz_grid[goal[0], goal[1]] = 0.7    # Goal in light purple

    plt.imshow(viz_grid, cmap='RdYlBu', interpolation='none')
    plt.colorbar()
    plt.title('Path Planning: Green=Start, Purple=Goal, Yellow=Path, Red=Obstacles')
    plt.show()