# Romania Graph Pathfinding

## Problem Statement

This project aims to solve the pathfinding problem in a graph representing cities in Romania. We utilize four different algorithms—Depth-First Search (DFS), Iterative Deepening Search (IDS), Depth-Limited Search (DLS), and A* Search—to find the shortest path from a source city to a target city. The cities and their connections are represented as nodes and edges, respectively, with weights indicating distances.

## Diagram of the Graph

The following diagram represents the cities as nodes and the connections between them as edges. The weights on the edges represent the distances in kilometers.

```
    [Arad]
     / | \
   75 118 140
   /   |    \
[Zerind]  [Sibiu]
   |         |
   71       99
   |         |
 [Oradea]--[Fagaras]
                |
               211
                |
            [Bucharest]
```

## Approaches

1. **Depth-First Search (DFS)**:
   - The DFS algorithm explores as far as possible along each branch before backtracking. It uses a stack to keep track of nodes to visit next, and it is efficient for exploring all possible paths in the graph.
   
2. **Iterative Deepening Search (IDS)**:
   - IDS combines the space efficiency of DFS with the completeness of Breadth-First Search (BFS). It performs depth-limited searches with increasing depth limits until the target node is found or the maximum depth is reached.

3. **Depth-Limited Search (DLS)**:
   - DLS is a variant of DFS that restricts the depth of the search to a predetermined limit. This approach is useful when the search space is large, and we want to limit the exploration depth to find a solution quickly.

4. **A* Search**:
   - The A* search algorithm uses heuristics to guide its search for the shortest path. It maintains a priority queue of nodes to explore, considering both the cost to reach the node and an estimated cost to reach the goal from that node. This allows A* to efficiently find the optimal path while minimizing the number of nodes explored.

## How to Run

1. Clone this repository to your local machine.
2. Navigate to the directory containing the scripts.
3. Ensure that the required data files (`Graph_romania.txt` and `romania_sld.txt`) are present in the same directory.
4. Run the desired algorithm script using Python:

   ```bash
   python <script_name>.py
   ```

   Replace `<script_name>` with the name of the script you wish to execute (e.g., `RomaniaUsingDFS.py`, `RomaniaUsingIDS.py`, `RomaniaUsingDLS.py`, `RomaniaUsingAstar.py`).

## Complexity Analysis

- **DFS**: 
  - Time Complexity: O(b^d), where `b` is the branching factor and `d` is the depth of the solution.
  - Space Complexity: O(d) for the recursion stack.

- **IDS**:
  - Time Complexity: O(b^d) for the worst case.
  - Space Complexity: O(d) for the recursion stack.

- **DLS**:
  - Time Complexity: O(b^l), where `l` is the depth limit.
  - Space Complexity: O(l) for the recursion stack.

- **A***:
  - Time Complexity: O(b^d) in the worst case, but generally faster with good heuristics.
  - Space Complexity: O(b^d) due to maintaining the priority queue.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests with enhancements or bug fixes.

## License

This project is licensed under the MIT License.
