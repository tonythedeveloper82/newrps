#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random,time

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

moves = ['rock', 'paper', 'scissors']

class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class HumanPlayer(Player):
    def move(self):
        response = input("""Make your selection of either rock, paper, scissors: To exit type quit\n""")
        response = response.lower()
        while response not in moves and response != 'quit':
            response = input(""""Invalid move, try again\n""")
        if response == 'quit':
            exit()
        return response

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):
    def move(self):
        return (random.choice(moves))

    def learn(self, my_move, their_move):
        pass

class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return (random.choice(moves))
        else:
            return self.their_move  

    def learn(self, my_move, their_move):
        pass

class CyclePlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.last_move = None

    def move(self):
        move = None
        if self.last_move is None:
            move = Player.move(self)
        else:
            index = moves.index(self.last_move) + 1
            if index >= len(moves):
                index = 0
            move = moves[index]
        self.last_move = move
        return move

    def learn(self, my_move, their_move):
        pass

def beats(one, two):
        return((one == 'rock' and two == 'scissors') or
           (one == 'paper' and two == 'rock') or
           (one == 'scissors' and two == 'paper'))

class Game():
    def __init__(self, HumanPlayer, RandomPlayer):
        self.HumanPlayer = HumanPlayer
        self.RandomPlayer = RandomPlayer
        self.wins = 0
        self.losses = 0

    def play_round(self):
        move1 = self.HumanPlayer.move()
        move2 = self.RandomPlayer.move()
        if beats (move1, move2):
            self.wins += 1
            time.sleep(2) 
            print("Player 1 Wins Round!") 
            print(f"Player 1 score: {self.wins} and Player 2 score: {self.losses}") 
        elif beats(move2, move1):
            self.losses += 1
            time.sleep(2) 
            print("Player 2 Wins Round!")
            print(f"Player 1 score: {self.wins} and Player 2 score: {self.losses}")
        else:
            print("Invalid, try again")

    def play_game(self):
        print("Let's Play Rock, Paper, Scissors and may the best hand win!")
        for rnd in range(1, 6):
            print(f"Round {rnd}:")
            self.play_round()
        if self.wins > self.losses:
            print(f"Player 1 score: {self.wins} and Player 2 score: {self.losses}")
            time.sleep(1)
            print("You won! You are the rock, paper, scissors champion!")
        elif self.wins < self.losses:
            print(f"Player 1 score: {self.wins} and Player 2 score: {self.losses}")
            time.sleep(1)
            print("Your opponent won, better luck next time!")
        else:
            print(f"Player 1 score: {self.wins} and Player 2 score: {self.losses}")
            time.sleep(1)
            print("It's a draw, play again!")
        
    
if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
