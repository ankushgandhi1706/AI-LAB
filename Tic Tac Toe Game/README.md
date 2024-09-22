# Tic-Tac-Toe Game

## Problem Statement

Tic-Tac-Toe is a classic two-player game played on a 3x3 grid. Players take turns placing their symbols (X and O) in empty squares. The goal is to be the first to align three of your symbols horizontally, vertically, or diagonally. This project implements a console-based version of Tic-Tac-Toe, allowing two players to compete against each other.

## Approach

The game uses a 3x3 board represented as a list of lists in Python. The key functions in the code are:

- **Initialization**: The board starts empty, denoted by `"-"` for each cell.
  
- **Input Handling**: Players input their desired position using a coordinate format (row,column). The program checks for valid moves and updates the board accordingly.

- **Win Checking**: The `checkWin` function checks for winning conditions by evaluating rows, columns, and diagonals for three identical symbols. 

- **Game Flow**: The game alternates turns between the two players until a win or a tie occurs, using the `startGame` function to control the overall gameplay.

Here is a brief overview of some critical sections of the code:

```python
board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"],]

initBoard = [["0,0", "0,1", "0,2"],
             ["1,0", "1,1", "1,2"],
             ["2,0", "2,1", "2,2"],]

def isBoardFull():
    numDash = 9
    for i in board:
        for j in i:
            if j != "-":
                numDash -= 1
    return numDash

# Other functions (printBoard, checkWin, startGame) follow...
```

## Time Complexity

- **Game Initialization**: O(1) - Initializing the board and player names.
- **Win Checking**: O(1) - Always checks a fixed number of conditions (3 rows, 3 columns, 2 diagonals).
- **Game Turns**: Each turn involves a constant-time check and update, leading to an overall complexity of O(n) where n is the maximum number of turns (9).

## Space Complexity

The space complexity is O(1) since the board size is constant (3x3) regardless of the number of moves made.

## How to Run

1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using Python:

   ```bash
   python TicTac.py
   ```

4. Follow the on-screen prompts to play the game!

## Contributing

Feel free to fork this repository and submit pull requests with enhancements or bug fixes. Contributions are welcome!

## License

This project is licensed under the MIT License.
