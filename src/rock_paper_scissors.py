"""Author: Soheila
    Date created: 20/12/2024
    Description: Rock Paper Scissors game
"""

import random


class RockPaperScissors:
    """Main class for rock paper scissors game."""
    # get_player_choice
    # get_computer_choice
    # decide_winner
    # play()
    def __init__(self, name: str):
        self.choices = ["rock", "paper", "scissors"]
        self.player_name = name
    
    def get_player_choice(self):
        user_choice = input(f"Enter your choice ({self.choices}): ")
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        
        print(f"Invalid choice, you must select from {self.choices}")
        return self.get_player_choice()
        
    def get_computer_choice(self):
        """Get computer choice randomly from choices: rock, paper, scissors."""
        return random.choice(self.choices)
    
    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        """Decide the winner of the game based on user and computer choice.

        :param user_choice: the choice of the user
        :param computer_choice: the choice of the computer
        :return: the result of the game. (who won!)
        """
        if user_choice == computer_choice:
            return "It's a Tie!"
        
        win_combination = [("rock", "scissors"),("paper", "rock"),("scissors", "paper")]
        for win_comb in win_combination:
            if (user_choice == win_comb[0]) & (computer_choice == win_comb[1]):
                return "Congratulationa! You won!"
            
        return "Oh no! The computer won!"
    
    def play(self):
        """play the game.
        - Get your choice.
        - Get computer choice.
        - Decide the winner.
        - Print the result.
        """
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        winner_msg = self.decide_winner(user_choice, computer_choice)
        print(f"computer choice: {computer_choice}")
        print(winner_msg)

if __name__ == "__main__":
    game = RockPaperScissors("Ali")
    while True:
        game.play()
        continue_game = input("Do you want to play again? (Enter any key to play again, enter q to exit!)")
        if continue_game.lower() == "q":
            break