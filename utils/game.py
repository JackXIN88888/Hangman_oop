
import random

class Hangman:
    """_summary_ this is a class for the game "Hangman", it has all the methods and attributes to run the game.
    :param possible_words: this gives a pool of words the computer will select "word to find" from
    :param lives: this gives how many guesses you have before you begin the game, each wrong guess, you loss 1 life.
    """
    def __init__(self, possible_words=['becode', 'learning', 'mathematics', 'sessions'], lives=5):
        self.possible_words = possible_words
        word_to_find_init = list(random.choice(possible_words))
        self.word_to_find = word_to_find_init 
        self.lives = lives
        correctly_guessed_letters_init =[]
        for length in range(len(word_to_find_init )):
            correctly_guessed_letters_init.append('_')
            
        
        self.correctly_guessed_letters = correctly_guessed_letters_init
        wrongly_guessed_letters_init = []
        self.wrongly_guessed_letters = wrongly_guessed_letters_init
        self.turn_count = 0
        self.error_count = 0
        
                
    def play(self):
        """_summary_this gives the main part of the game itself, you have to pick a letter and find if the letter is or not in the "word to find"
        """
        print('Please enter a letter:')
        guessed_letter = input()
        input_status = False
        for one_letter in range(97,123):
            if guessed_letter == chr(one_letter):
                input_status = True

        if input_status:
            guessed_status = False
            position_of_letter = 0
            for letter in self.word_to_find:
                if letter == guessed_letter:
                    guessed_status = True
                    self.correctly_guessed_letters[position_of_letter] = guessed_letter
                position_of_letter +=1

            if not guessed_status:
                self.wrongly_guessed_letters.append(guessed_letter)
                self.error_count +=1
                self.lives -=1

        else:
            print("input is not a letter, please enter again!")
            self.play()

        print(f"the letter is: {self.correctly_guessed_letters}")
        print(f"the wrongly guessed letters are:. {self.wrongly_guessed_letters}")
        
    def start_game(self):
        """_summary_this is the function to start the game and make the counts, and linked to other methods inside the class
        """

        while self.lives > 0 and self.word_to_find != self.correctly_guessed_letters:
            self.play()
            self.turn_count+=1
            
            if self.word_to_find == self.correctly_guessed_letters:
                self.well_played()
                break

        if self.lives == 0:
            self.game_over()

    def game_over(self):
        """_summary_tell you that game is over, you lost
        """
        print('Game Over')

    def well_played(self):
        """_summary_give a result of the performance of you on the game when it is over and when you won
        """
        print(f"You found the word:{self.word_to_find},in {self.turn_count} turns with {self.error_count} errors")
