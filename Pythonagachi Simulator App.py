#!/usr/bin/env python3

#Classes Challenge 36: Pythonagachi Simulator App

import random

class Tamagochi():
    """Class to create a Pythonagachi"""

    def __init__(self, name):
        """Initialize attributes"""
        # Name of the creature
        self.name = name

        # Stats
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0

        # Inventory of food and boolean for check if is awake and alive
        self.inventory = 2
        self.awake = True
        self.alive = True

    def increment_values(self):
        """Increment attributes based on the difficulty"""
        self.hunger += random.randint(0, difficult)
        self.dirtiness += random.randint(0, difficult)

        # Check if the creature is awake to increase the attributes
        if self.awake:
            self.boredom += random.randint(0, difficult)
            self.tiredness += random.randint(0, difficult)

    def display_info(self):
        """Display the information of the creature"""
        # Print the creature name and if it is awake or sleeping
        print(f"\nCreature Name:  {self.name}")
        if self.awake:
            awake = 'Awake'
        else:
            awake = 'Sleeping'
        print(f"Current Status: {awake}")

        # Print the stats and the inventory
        print("\nStats:")
        print(f"Hunger (0-10):     {self.hunger}")
        print(f"Boredom (0-10):    {self.boredom}")
        print(f"Tiredness (0-10):  {self.tiredness}")
        print(f"Dirtiness (0-10):  {self.dirtiness}")

        print(f"\nFood Inventory:    {self.inventory} pieces")
        

    def actions(self):
        """Display the possibles interactions with the creature"""
        # Variable for print options
        options = """
                ---------------------------------
                | Enter (1) to eat.             |
                | Enter (2) to play.            |
                | Enter (3) to sleep.           |
                | Enter (4) to take a bath.     |
                | Enter (5) to forage for food. |
                ---------------------------------
                """
        
        # Variable options but strike out
        options_strikeout = """"""
        cross = False

        # For loop to strike out the 5 initial options
        for letter in options:
            if letter.startswith('E'):
                cross = True
            elif letter == '.':
                cross = False
            if cross:
                options_strikeout += '\u0336' + letter
            else:
                options_strikeout += letter

        # Variables to add a 6th option
        options_strikeout += '| Enter (6) to try to wake up.  |\n'
        options_strikeout += '\t\t---------------------------------\n'

        # While loop for check if the input is right
        while True:
            # Check if the creature is awake
            if self.awake:
                # Print the possible actions and get the input
                print(options)
                choice = int(input("What is your choice?: "))
            else:
                # Print the possible actions and get the input
                print(options_strikeout)
                choice = int(input("Let's try to wake it up!: "))
            
            # List for check if the input is right
            choices = [1,2,3,4,5]

            # Check if is awake and the input is right
            if self.awake and choice in choices:
                return choice
            # Check if is sleeping and the input is 6 to wake up later
            elif not self.awake and choice == 6:
                return choice
            # Print a fancy wrong input and repeat the loop
            else:
                print("\n" + "X"*50)
                print("     Wrong input.  Please pick a right choice.")
                print("X"*50)

    def wake_up(self):
        """Function to try to wake up the creature"""
        # Variable to randomize the possibilities of wake up the creature
        wake_up = random.randint(0, difficult - 1)
        # Check if the variable is 0 to wake up the creature
        if wake_up == 0:
            print(f"\t{self.name} just woke up!")
            # Also wake up the creature, states tiredness to 0 and subtract 2 to boredom
            self.awake = True
            self.tiredness = 0
            self.boredom -= 2
        # If the variable isn't 0, the creature won't wake up
        else:
            print(f"\t{self.name} won't wake up...")
            print("\tZzzzzz....Zzzzzz....Zzzzzz....")
            # Also keeps subtracting 2 to boredom
            self.boredom -= 2

    def eat(self):
        """Function to give food to the creature"""
        # Check if the inventory has food
        if self.inventory > 0:
            print(f"\tYumm!  {self.name} ate a great meal!")
            # Randomize the subtract of hunger and subtracts 1 meal from inventory
            self.hunger -= random.randint(1,4)
            self.inventory -= 1
        # Check if the creature is hungry
        elif self.hunger == 0:
            print(f"\tSeems like {self.name} is not hungry...")
        # Print that the creature has not food in the inventory
        else:
            print(f"\tSeems like {self.name} doesn't have any food...")

        # Checks if the hunger value is negative and states to 0
        if self.hunger < 0:
                self.hunger = 0

    def play(self):
        """Function to play with the creature"""
        # Check if the creature is bored
        if self.boredom > 0:
            print(f"\t{self.name} wants to play a game.")
            print(f"\t{self.name} is thinking of a number 0, 1 or 2.")
            guess = int(input("\tWhat is your guess?: "))
            # Variable to randomize the choice of the creature
            number = random.randint(0,2)

            # Check if your number is the same of the creature
            if guess == number:
                # Prints a fancy response of win
                print("\n\t" + "*"*(28+int(len(name))))
                print(f"\t NICE! {self.name} was thinking of {number} too!")
                print("\t" + "*"*(28+int(len(name))))
                # Also substracts 3 from boredom
                self.boredom -= 3
            else:
                # Prints a fancy response of lose
                print("\n\t" + "x"*(28+int(len(name))))
                print(f"\t WRONG! {self.name} was thinking of {number}.")
                print("\t" + "x"*(28+int(len(name))))
                # Also substracts 1 from boredom
                self.boredom -= 1
        # Print that the creature is not bored
        else:
            print(f"\tSeems like {self.name} doesn't want to play...")

        # Checks if the boredom value is negative and states to 0
        if self.boredom < 0:
            self.boredom = 0

    def sleep(self):
        """Function to set the creature to sleep"""
        # Check if the creature is tired
        if self.tiredness > 0:
            print("\tZzzzzz....Zzzzzz....Zzzzzz....")
            print(f"\t{self.name} just took a nap!")
            # Also sets tiredness to 0, subtracts 2 from boredom and awake the creature
            self.tiredness = 0
            self.boredom -= 2
        else:
            print(f"\tSeems like {self.name} is not tired...")

        # Checks if the boredom value is negative and states to 0
        if self.boredom < 0:
            self.boredom = 0

    def take_bath(self):
        """Function to give a bath to the creature"""
        print(f"\t{self.name} has taken a bath.  All clean!")
        # States dirtiness to 0
        self.dirtiness = 0

    def forage_food(self):
        """Function to forage food"""
        # Variable to randomize the food found
        found = random.randint(1,4)
        print(f"\t{self.name} found {found} pieces of food!")
        # Sums the found food to the inventory and sums 2 to dirtiness
        self.inventory += found
        self.dirtiness += 2

    def death(self):
        """Function to check if the creature is death or sleeping"""
        # Check if the creature starved to death or if suffered an infection
        if self.hunger > 9:
            print(f"\n{self.name} has starved to death...")
            self.alive = False
        elif self.dirtiness > 9:
            print(f"\n{self.name} has suffered an infection and died...")
            self.alive = False
        # Check if the creature is bored or sleepy
        elif self.boredom > 9:
            (f"\n{self.name} is bored.  Falling asleep...")
            self.boredom = 10
            self.awake = False
        elif self.tiredness > 9:
            print(f"\n{self.name} is sleepy.  Falling asleep...")
            self.tiredness = 10
            self.awake = False

def call_actions(Creature, choice):
    """Function to call the actions from the Creature class"""
    # Check if the creature is awake to proceed with actions from 1 to 5
    if my_tamagochi.awake:
        if choice == 1:
            my_tamagochi.eat()
        elif choice == 2:
            my_tamagochi.play()
        elif choice == 3:
            my_tamagochi.sleep()
        elif choice == 4:
            my_tamagochi.take_bath()
        elif choice == 5:
            my_tamagochi.forage_food()
    # Check if choice is 6 to try to wake up the creature
    else:
        if choice == 6:
            my_tamagochi.wake_up()
        else:
            print(f"{my_tamagochi.name} is sleeping! Try to wake it up!")

print("Welcome to the Pythonagachi Simulator App")

running = True # Variable flag
while running:
    # Sets the difficulty of the game
    difficult = int(input("\nPlease choose a difficulty level (1-5): "))
    if difficult > 5:
        print(f"You entered {difficult}, and the max value is 5.  Difficulty set to 5.")
        difficult = 5
    elif difficult < 1:
        print(f"You entered {difficult}, and the min value is 1.  Difficulty set to 1.")
        difficult = 1
    # Sets the name of the creature
    name = input("What name would you like to give your pet Pythonogachi?: ").title().strip()

    # Creates the creature
    my_tamagochi = Tamagochi(name)

    round_num = 0 # Variable flag for count rounds
    while my_tamagochi.alive:
        round_num += 1 # Variable flag for count rounds

        # Prints a fancy rounds counter
        print("\n" + "-"*50)
        print(f"\t\t    Round #{round_num}")

        # Displays the creature information and sets the action choice
        my_tamagochi.display_info()
        choice = my_tamagochi.actions()

        # Prints a fancy action information
        print("\n" + "-"*50)
        call_actions(my_tamagochi, choice)
        print("-"*50)

        # Print summary information
        print(f"\nRound #{round_num} Summary:")

        # Displays the creature information
        my_tamagochi.display_info()
        
        # Waits for the input to proceed with the next round
        input("\nPress 'Enter' to continue...")

        # Increment the stats values from the difficulty and checks if the creature is death or sleeping
        my_tamagochi.increment_values()
        my_tamagochi.death()

    # Prints a R.I.P. and a summary of the rounds survived
    print("R.I.P.")

    print(f"\n{my_tamagochi.name} survived a total of {round_num} rounds.")
    # Also asks if the player wants to play again
    again = input("Would you like to play again? (y/n): ").lower().strip()
    if again != 'y':
        print("Thank you for playing Pythonagachi!")
        running = False