#!/usr/bin/env python3

#Classes Challenge 37: Casino Blackjack App

import random, time

class Casino():
    """Class to create a casino"""

    def __init__(self, wallet):
        """Initialize attributes"""
        # Wallet to change "money for chips"
        self.wallet = wallet

        # Bet to play
        self.bet = 0

        # Variable to store the hands of player and dealer in every round
        self.player_hand = []
        self.dealer_hand = []

        # Variable to store the values of player and dealer in every round
        self.player_value = 0
        self.dealer_value = 0

    def display_info(self):
        """Function to display the information"""
        # Print the current money, gets the bet input and assigns to the class variable
        print(f"\nCurrent Money: ${self.wallet}")
        self.bet = int(input("What would you like to bet? (minimum bet of 20): ") or "0")
        # Checks if the input is 0. If it's closes the program
        if self.bet == 0:
            print("\nNo bet no play. Hope you enjoyed. See you next time!")
            return running == False
        # Checks if the input is at least 20. If not, prints a warning and set to 20 the variable
        if self.bet < 20:
            print("Told you that the minimum bet is $20.  Bet set to $20.")
            self.bet = 20

        # Takes out the bet from the current money
        self.wallet -= self.bet

        # Print the current money and the current bet for the round
        print(f"\nCurrent Money: ${self.wallet}\tCurrent Bet: ${self.bet}")
        return running == True

    def cards(self):
        """Function to create cards"""        
        while True:
            symbols = ["♠","♥","♦","♣"]
            # Random choose a card suit
            symbol = random.choice(symbols)

            # List with the 13 possibilities of cards
            cards = [['0'],
            ['╔═══════════╗',
            '║ A         ║',
            '║           ║',
            '║           ║',
            f'║     {symbol}     ║',
            '║           ║',
            '║           ║',
            '║         A ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            '║ 2         ║',
            f'║     {symbol}     ║',
            '║           ║',
            '║           ║',
            '║           ║',
            f'║     {symbol}     ║',
            '║         2 ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            '║ 3         ║',
            f'║     {symbol}     ║',
            '║           ║',
            f'║     {symbol}     ║',
            '║           ║',
            f'║     {symbol}     ║',
            '║         3 ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            '║ 4         ║',
            f'║   {symbol}   {symbol}   ║',
            '║           ║',
            '║           ║',
            '║           ║',
            f'║   {symbol}   {symbol}   ║',
            '║         4 ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            '║ 5         ║',
            f'║   {symbol}   {symbol}   ║',
            '║           ║',
            f'║     {symbol}     ║',
            '║           ║',
            f'║   {symbol}   {symbol}   ║',
            '║         5 ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            '║ 6         ║',
            f'║   {symbol}   {symbol}   ║',
            '║           ║',
            f'║   {symbol}   {symbol}   ║',
            '║           ║',
            f'║   {symbol}   {symbol}   ║',
            '║         6 ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            '║ 7         ║',
            f'║   {symbol}   {symbol}   ║',
            f'║     {symbol}     ║',
            f'║   {symbol}   {symbol}   ║',
            '║           ║',
            f'║   {symbol}   {symbol}   ║',
            '║         7 ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            '║ 8         ║',
            f'║   {symbol}   {symbol}   ║',
            f'║     {symbol}     ║',
            f'║   {symbol}   {symbol}   ║',
            f'║     {symbol}     ║',
            f'║   {symbol}   {symbol}   ║',
            '║         8 ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            '║ 9         ║',
            f'║   {symbol}   {symbol}   ║',
            f'║   {symbol}   {symbol}   ║',
            f'║     {symbol}     ║',
            f'║   {symbol}   {symbol}   ║',
            f'║   {symbol}   {symbol}   ║',
            '║         9 ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            '║ 10        ║',
            f'║   {symbol}   {symbol}   ║',
            f'║   {symbol}   {symbol}   ║',
            f'║   {symbol}   {symbol}   ║',
            f'║   {symbol}   {symbol}   ║',
            f'║   {symbol}   {symbol}   ║',
            '║        10 ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            f'║ J {symbol}       ║',
            '║           ║',
            '║     .     ║',
            '║   qoOop   ║',
            '║  (=====)  ║',
            '║           ║',
            f'║       {symbol} J ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            f'║ Q {symbol}       ║',
            '║           ║',
            '║     +     ║',
            '║   qoOop   ║',
            '║  (*-*-*)  ║',
            '║           ║',
            f'║       {symbol} Q ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            f'║ K {symbol}       ║',
            '║           ║',
            '║     *     ║',
            '║   qoOop   ║',
            '║  (*-*-*)  ║',
            '║           ║',
            f'║       {symbol} K ║',
            '╚═══════════╝']]

            # Choose a random card from A to K
            random_card = random.randint(1,13)
            # Stores the card chosen in the 'card' variable
            card = cards[random_card]

            # Checks if the card created was already created to not create duplicated cards.
            if card not in cards_created:
                cards_created.append(card)
            else:
                continue
            
            # Sets the value of cards according to
            # If the card is J, Q or K, sets to 10
            if random_card == 11 or random_card == 12 or random_card == 13:
                value = 10
            # If the card is an Ace, sets to 11
            elif random_card == 1:
                value = 11
            # Else, sets to their same value
            else:
                value = random_card

            return card, value
    
    def player_cards(self):
        """Function to create and display the player hand"""
        # Creates 2 cards for the starter player hand
        for i in range(2):
            # Gets the card created and its value from self.cards()
            card, value = self.cards()
            # Then adds the card to the player hand
            self.player_hand.append(card)
            # And adds its value to the 'player hand value'
            self.player_value += value

        only_once = True # Variable flag
        one_ace = False # Variable flag
        while True:
            # Prints a fancy 'Player's Hand' according to the number of cards in the hand
            if len(self.player_hand) == 2:
                print("""
            ---------------------
            |   Player's Hand   |
            ---------------------\n""")
            elif len(self.player_hand) == 3:
                print("""
          ---------------------
          |   Player's Hand   |
          ---------------------\n""")
            elif len(self.player_hand) == 4:
                print("""
                 ---------------------
                 |   Player's Hand   |
                 ---------------------\n""")
            elif len(self.player_hand) == 5:
                print("""
                        ---------------------
                        |   Player's Hand   |
                        ---------------------\n""")
            else:
                print("""
                               ---------------------
                               |   Player's Hand   |
                               ---------------------\n""")

            count = 0 # Variable flag
            # Loop to print the cards one beside the other
            while count < 9:
                for card in self.player_hand:
                    if len(self.player_hand) == 2:
                        print("\t" + card[count], end=" ")
                    else:
                        print(card[count], end=" ")
                print()
                count += 1

                # Checks if an Ace was created and sets is value to 1 if needed
                if only_once and 'A' in self.player_hand[0][1] or 'A' in self.player_hand[1][1]:
                    only_once = False
                    one_ace = True
                elif only_once and 'A' in self.player_hand[-1][1] and self.player_value > 21:
                    self.player_value -= 10
                    only_once = False
                
                if one_ace and self.player_value > 21:
                    self.player_value -= 10
                    one_ace = False
            
            # Creates spaces according to the value, if its one digit or two
            if self.player_value < 10:
                spaces = '    '
            else:
                spaces = '   '

            # Prints a fancy 'Player's Hand Value' according to the number of cards in the hand
            if len(self.player_hand) == 2:
                print(f"""
            ---------------------
            | Total value: {self.player_value}{spaces}|
            ---------------------""")
            elif len(self.player_hand) == 3:
                print(f"""
          ---------------------
          | Total value: {self.player_value}{spaces}|
          ---------------------""")
            elif len(self.player_hand) == 4:
                print(f"""
                 ---------------------
                 | Total value: {self.player_value}{spaces}|
                 ---------------------""")
            elif len(self.player_hand) == 5:
                print(f"""
                        ---------------------
                        | Total value: {self.player_value}{spaces}|
                        ---------------------""")
            else:
                print(f"""
                               ---------------------
                               | Total value: {self.player_value}{spaces}|
                               ---------------------""")

            # Checks if the value is below 21
            if self.player_value < 21:
                # If its, checks if the player wants one more card
                one_more = input("\nWould you like to hit? (y/n): ").lower().strip()
            # Else, the value is already over 21
            elif self.player_value == 21 and len(self.player_hand) == 2:
                print("\nYou got a Blackjack!!")
                break
            elif self.player_value == 21:
                print("\nYou got 21!!")
                break
            else:
                print("\nSorry, you already went over 21.")
                break

            # checks if the player wants one more card, then creates it
            if one_more == 'y':
                card, value = self.cards()
                self.player_hand.append(card)
                self.player_value += value
                continue
            else:
                break
    
    def dealer_card(self):
        """Function to create the dealer hand and display the first card"""
        only_once = True # Variable flag
        one_ace = False # Variable flag
        # Loops while the 'Dealer's Hand Value' is below 17 and create cards
        while self.dealer_value < 17:
            card, value = self.cards()
            self.dealer_hand.append(card)
            self.dealer_value += value

            # Checks if an Ace was created and sets is value to 1 if needed
            if only_once and 'A' in self.dealer_hand[-1][1] and self.dealer_value > 21:
                self.dealer_value -= 10
                only_once = False
            elif only_once and 'A' in self.dealer_hand[-1][1] and self.dealer_value < 21:
                one_ace = True
                only_once = False
            
            if one_ace and self.dealer_value > 21:
                self.dealer_value -= 10
                one_ace = False

        # Prints the first card of the dealer hand
        print(f"""
            The dealer is showing: 
        \t{self.dealer_hand[0][0]}
        \t{self.dealer_hand[0][1]}
        \t{self.dealer_hand[0][2]}
        \t{self.dealer_hand[0][3]}
        \t{self.dealer_hand[0][4]}
        \t{self.dealer_hand[0][5]}
        \t{self.dealer_hand[0][6]}
        \t{self.dealer_hand[0][7]}
        \t{self.dealer_hand[0][8]}""")

    def dealer_cards(self):
        """Function to display the entire dealer hand"""
        # Prints a fancy information of how much cards has draw the dealer
        print("\n--------------------------------------")
        print(f"Dealer is set with a total of {len(self.dealer_hand)} cards.")
        print("--------------------------------------")

        # Waits for the player to reveal the dealer hand
        input("\nPress 'Enter' to reveal the dealer's hand.")

        # Prints a fancy 'Dealer's Hand' according to the number of cards in the hand
        if len(self.dealer_hand) == 2:
            print("""
            ---------------------
            |   Dealer's Hand   |
            ---------------------\n""")
        elif len(self.dealer_hand) == 3:
            print("""
          ---------------------
          |   Dealer's Hand   |
          ---------------------\n""")
        elif len(self.dealer_hand) == 4:
            print("""
                 ---------------------
                 |   Dealer's Hand   |
                 ---------------------\n""")
        elif len(self.dealer_hand) == 5:
            print("""
                        ---------------------
                        |   Dealer's Hand   |
                        ---------------------\n""")
        else:
            print("""
                               ---------------------
                               |   Dealer's Hand   |
                               ---------------------\n""")
        
        count = 0
        while count < 9:
            for card in self.dealer_hand:
                if len(self.dealer_hand) == 2:
                    print("\t" + card[count], end=" ")
                else:
                    print(card[count], end=" ")
            print()
            count += 1

        # Prints a fancy 'Dealer's Hand Value' according to the number of cards in the hand
        if len(self.dealer_hand) == 2:
            print(f"""
            ---------------------
            | Total value: {self.dealer_value}   |
            ---------------------""")
        elif len(self.dealer_hand) == 3:
            print(f"""
          ---------------------
          | Total value: {self.dealer_value}   |
          ---------------------""")
        elif len(self.dealer_hand) == 4:
            print(f"""
                 ---------------------
                 | Total value: {self.dealer_value}   |
                 ---------------------""")
        elif len(self.dealer_hand) == 5:
            print(f"""
                        ---------------------
                        | Total value: {self.dealer_value}   |
                        ---------------------""")
        else:
            print(f"""
                               ---------------------
                               | Total value: {self.dealer_value}   |
                               ---------------------""")

    def who_wins(self):
        """Function to check the values of the player and the dealer and set who wins"""
        # Check if the player has a blackjack but not the dealer too
        if ((len(self.player_hand) == 2 and self.player_value == 21 and ('A' in self.player_hand[0][1] or 'A' in self.player_hand[1][1])) and not
        (len(self.dealer_hand) == 2 and self.dealer_value == 21 and ('A' in self.dealer_hand[0][1] or 'A' in self.dealer_hand[1][1]))):
            print(f"\nIt's a BLACKJACK!! You win ${self.bet*2}!!")
            self.wallet += self.bet * 3
        # Check if the player is not over 21
        elif self.player_value > 21:
            print("\nYou went over 21.  You lose...")
        # Check if the dealer is not over 21
        elif self.dealer_value > 21:
            print("\nDealer went over 21.  You win!")
            self.wallet += self.bet * 2
        # Check if the player value is the same as dealer
        elif self.player_value == self.dealer_value:
            print(f"\nYou and dealer both got {self.player_value}. It's a push!")
            self.wallet += self.bet
        # Check if the player value is over the dealer value (but not over 21)
        elif self.player_value > self.dealer_value:
            print(f"\nDealer gets {self.dealer_value} over {self.player_value}.  You win!")
            self.wallet += self.bet * 2
        # Check if the player value is below the dealer value (but not over 21)
        elif self.player_value < self.dealer_value:
            print(f"\nDealer gets {self.dealer_value} over {self.player_value}.  You lose...")

print("Welcome to the Blackjack App.")

# Print the minimum bet info and get the input of how much are gonna willing to play
print("\nThe minimum bet at this table is $20.")
wallet = int(input("How much money are you willing to play with today?: ") or "0")
# Sets wallet to 100 if no input given
if wallet == 0:
    input("\nNo money no play.  See you next time!")
    quit()
# Checks if the wallet value is over 20
elif wallet < 20:
    # If not, prints a warning and closes the program
    print(f"\nTold you that the minimum bet is $20. You can't play with {wallet}.")
    input("See you next time.  Bye!")
    quit()

# Creates the wallet with money to bet
my_bets = Casino(wallet)

# Variable to store the cards created every round
cards_created = []

running = True # Variable flag
while running:
    # Displays information of the current money and current bet
    running = my_bets.display_info()
    if not running:
        break

    # Displays the first card of the dealer
    my_bets.dealer_card()

    # Displays the player cards and then the dealer cards
    my_bets.player_cards()
    my_bets.dealer_cards()

    # Checks the values of the player and the dealer and sets who wins
    my_bets.who_wins()

    # Variables to reset every round
    cards_created = []
    my_bets.player_hand = []
    my_bets.dealer_hand = []
    my_bets.player_value = 0
    my_bets.dealer_value = 0

    # Check if the wallet has more than 20 chips. If not, closes the program
    if my_bets.wallet < 20:
        input("Sorry, you ran out of money.  Please play again.")
        running = False
