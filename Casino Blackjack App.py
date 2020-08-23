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
        self.bet = int(input("What would you like to bet? (minimum bet of 20): "))
        # Checks if the input is at least 20. If not, prints a warning and set to 20 the variable
        if self.bet < 20:
            print("Told you that the minimum bet is $20.  Bet set to $20.")
            self.bet = 20

        # Print the current money and the current bet for the round
        print(f"\nCurrent Money: ${self.wallet}\tCurrent Bet: ${self.bet}")

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
            f'║     {symbol}     ║',
            '║           ║',
            '║         A ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            f'║ 2   {symbol}     ║',
            '║           ║',
            '║           ║',
            '║           ║',
            f'║     {symbol}   2 ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            f'║ 3   {symbol}     ║',
            '║           ║',
            f'║     {symbol}     ║',
            '║           ║',
            f'║     {symbol}   3 ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            f'║ 4 {symbol}   {symbol}   ║',
            '║           ║',
            '║           ║',
            '║           ║',
            f'║   {symbol}   {symbol} 4 ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            f'║ 5 {symbol}   {symbol}   ║',
            '║           ║',
            f'║     {symbol}     ║',
            '║           ║',
            f'║   {symbol}   {symbol} 5 ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            f'║ 6 {symbol}   {symbol}   ║',
            '║           ║',
            f'║   {symbol}   {symbol}   ║',
            '║           ║',
            f'║   {symbol}   {symbol} 6 ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            f'║ 7 {symbol}   {symbol}   ║',
            f'║     {symbol}     ║',
            f'║   {symbol}   {symbol}   ║',
            '║           ║',
            f'║   {symbol}   {symbol} 7 ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            f'║ 8 {symbol}   {symbol}   ║',
            f'║     {symbol}     ║',
            f'║   {symbol}   {symbol}   ║',
            f'║     {symbol}     ║',
            f'║   {symbol}   {symbol} 8 ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            f'║ 9 {symbol}   {symbol}   ║',
            f'║   {symbol}   {symbol}   ║',
            f'║     {symbol}     ║',
            f'║   {symbol}   {symbol}   ║',
            f'║   {symbol}   {symbol} 9 ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            f'║ 10 {symbol} {symbol}    ║',
            f'║    {symbol} {symbol}    ║',
            f'║    {symbol} {symbol}    ║',
            f'║    {symbol} {symbol}    ║',
            f'║    {symbol} {symbol} 10 ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            f'║ J {symbol}       ║',
            '║     .     ║',
            '║   qoOop   ║',
            '║  (=====)  ║',
            f'║       {symbol} J ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            f'║ Q {symbol}       ║',
            '║     ✚     ║',
            '║   qoOop   ║',
            '║  (*-*-*)  ║',
            f'║       {symbol} Q ║',
            '╚═══════════╝'],
            ['╔═══════════╗',
            f'║ K {symbol}       ║',
            '║     *     ║',
            '║   qoOop   ║',
            '║  (*-*-*)  ║',
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
            else:
                print("""
                 ---------------------
                 |   Player's Hand   |
                 ---------------------\n""")

            count = 0 # Variable flag
            # Loop to print the cards one beside the other
            while count < 7:
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
                elif one_ace and self.player_value > 21:
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
            else:
                print(f"""
                 ---------------------
                 | Total value: {self.player_value}{spaces}|
                 ---------------------""")

            # Checks if the player wants one more card
            one_more = input("\nWould you like to hit? (y/n): ").lower().strip()

            # Checks if the value is already over 21
            if one_more == 'y' and self.player_value > 21:
                print("Sorry, you already went over 21.")
                break
            # If not, it creates another card
            elif one_more == 'y':
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
            elif one_ace and self.dealer_value > 21:
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
        \t{self.dealer_hand[0][6]}""")

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
        else:
            print("""
                     ---------------------
                     |   Dealer's Hand   |
                     ---------------------\n""")
        
        count = 0
        while count < 7:
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
        else:
            print(f"""
                     ---------------------
                     | Total value: {self.dealer_value}   |
                     ---------------------""")

print("Welcome to the Blackjack App.")

# Print the minimum bet info and get the input of how much are gonna willing to play
print("\nThe minimum bet at this table is $20.")
wallet = int(input("How much money are you willing to play with today?: "))
# Checks if the wallet value is over 20
if wallet < 20:
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
    my_bets.display_info()

    # Displays the first card of the dealer
    my_bets.dealer_card()

    # Displays the player cards and then the dealer cards
    my_bets.player_cards()
    my_bets.dealer_cards()

    # Checks the values of the player and the dealer and sets who wins
    if my_bets.dealer_value > 21:
        print("\nDealer went over 21.  You win!")
        my_bets.wallet += my_bets.bet
    elif my_bets.player_value > 21:
        print("\nYou went over 21.  You lose...")
        my_bets.wallet -= my_bets.bet
    elif my_bets.player_value > my_bets.dealer_value:
        print(f"\nDealer gets {my_bets.dealer_value} over {my_bets.player_value}.  You win!")
        my_bets.wallet += my_bets.bet
    else:
        print(f"\nDealer gets {my_bets.dealer_value} over {my_bets.player_value}.  You lose...")
        my_bets.wallet -= my_bets.bet

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