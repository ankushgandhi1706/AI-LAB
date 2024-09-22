# Tic-Tac-Toe with Minimax Algorithm

## Problem Statement

Tic-Tac-Toe is a classic two-player game played on a 3x3 grid. Players alternate placing their symbols (X for the user and O for the computer) in empty squares. The objective is to align three of their symbols in a row, either horizontally, vertically, or diagonally. This implementation uses the Minimax algorithm to enable the computer to make optimal moves, ensuring it plays as strategically as possible.

### Example Diagram of Tic-Tac-Toe

```
     0   1   2
   +---+---+---+
 0 |   |   |   |
   +---+---+---+
 1 |   |   |   |
   +---+---+---+
 2 |   |   |   |
   +---+---+---+
```

## Approach

This implementation uses the Minimax algorithm to determine the best move for the computer player. The key components of the code are:

- **Game State Representation**: The board is represented as a 2D list, where each cell can be 'X', 'O', or '_'.

- **User Input**: The user is prompted to input their move, which updates the board.

- **Minimax Algorithm**: The `Best_Move` function recursively evaluates all possible moves to determine the optimal strategy for the computer. It maximizes the chance of winning while minimizing the user's chances.

- **Game Flow**: The game alternates turns between the user and the computer until a win, loss, or draw is achieved.

### Code Explanation

```python
from copy import deepcopy

class Tic_Tac_Toe:
    def __init__(self, size):  
        self.size = size
    
    def Display_Current_State(self, curr_state):
        # Display the current state of the board
        ...
    
    def Success(self, state):
        # Check if the user has won
        ...
    
    def Lose(self, state):
        # Check if the user has lost
        ...
    
    def Draw(self, state):
        # Check if the game is a draw
        ...
    
    def aimove(self, state):
        # Determine the best move for the computer
        ...
    
    def Best_Move(self, state, player):
        # Minimax algorithm implementation
        ...
    
    def Start_Game(self):
        # Start the game loop
        ...
```

## Time Complexity

- The time complexity of the Minimax algorithm can be expressed as O(b^d), where `b` is the branching factor (the average number of moves available to the players) and `d` is the depth of the game tree (the maximum number of moves).

## Space Complexity

- The space complexity is O(d), where `d` is the maximum depth of the game tree, due to the storage of states in the recursion stack.

## How to Run

1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using Python:

   ```bash
   python MinMax.py
   ```

4. Follow the prompts to play against the computer!

## Contributing

Feel free to fork this repository and submit pull requests with enhancements or bug fixes. Contributions are welcome!

## License

This project is licensed under the MIT License.
