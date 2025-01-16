# Rock Paper Scissors Game

A simple Python-based implementation of the classic **Rock Paper Scissors** game, where you can play against the computer.

## Features
- Interactive console-based gameplay.
- Validates player input to ensure correct choices.
- Randomized computer choices.
- Decides and announces the winner of each round.

## Getting Started

### Prerequisites
- Python 3.6 or higher

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/rock-paper-scissors.git
    ```
2. Navigate to the project directory:
    ```bash
    cd rock-paper-scissors
    ```

### Running the Game
To start the game, run the script:
    
```bash
python rock_paper_scissors.py
```

### How to Play
```bash
1. When prompted, enter your choice: `rock`, `paper`, or `scissors`.
2. The computer will make a random choice.
3. The result of the round (win, lose, or tie) will be displayed.
4. You can choose to play again or quit the game.
```
### Code Overview
The game is implemented in the `RockPaperScissors` class, which includes the following methods:

- **`get_player_choice()`**: Prompts the user for their choice and validates the input.
- **`get_computer_choice()`**: Randomly selects the computer's choice.
- **`decide_winner(user_choice, computer_choice)`**: Determines the outcome of the game.
- **`play()`**: Manages the gameplay loop.

### Example Output

```plaintext
Enter your choice (['rock', 'paper', 'scissors']): rock
Computer choice: scissors
Congratulations! You won!
Do you want to play again? (Enter any key to play again, enter q to exit!)
```
## Author
Soheila  
Date created: 20/12/2024

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

