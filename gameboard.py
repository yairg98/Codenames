# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:17:47 2020

@author: yairg
"""
import random
from itertools import combinations
from nltk import stem


# Load words from text file
with open('Wordlist.txt', 'r', encoding='utf-8-sig') as wordlist:
    word_str = wordlist.read().replace(' ', '_') # Extract words as a single string
    words = word_str.split(',') # Separate into list
    random.shuffle(words)
    

# Card class - stores all information about a particular card
class Card:
    
    def __init__(self, word, status): 
        self.word = word
        self.status = status # Red = R / Blue = B / Assassin = A
        self.in_play = True # False if the card has already been picked
        
    def card_id(self, codegiver):
        
        if codegiver and self.status:
            card_id = '{' + self.status + '} '
        else:
            card_id = '--- '
        card_id += self.word
        return card_id
        

# Board class - stores all cards and other game information
class Board:
    
    def __init__(self):
        self.cards = []
        self.used = [] # Keep track of used clues    
        
        # Choose 25 random words for the board
        all_words = random.sample(words, k=25)
        random.shuffle(all_words)
        
        # Assign blue, red, and assassin words
        blue_words = all_words[0:8]
        red_words = all_words[8:17]
        # other_words = all_words[17:24]
        assassin_word = all_words[24]
        
        # Generate a card for each word (in a random order)
        random.shuffle(all_words)
        for word in all_words:
            if word in blue_words:
                self.cards.append(Card(word, 'B')) # Initialize blue card
            elif word in red_words:
                self.cards.append(Card(word, 'R')) # Initialize red card
            elif word == assassin_word:
                self.cards.append(Card(word, 'A')) # Initialize assassin card
            else:
                self.cards.append(Card(word, '')) # Initialize plain card
        
        
    # Display all cards with option to show status or exclude out-of-play cards
    def disp_cards(self, codegiver = False, active_only = False):
        i = 0
        for card in self.cards:
            if card.in_play or not active_only:
                print(str(i) + '. ' + card.card_id(codegiver))
                i += 1
        
        
    # Return list of all in-play cards for the given team
    def get_words(self, status):
        # List of cards to return
        available_cards = []
        
        # Find all relevant cards (right team and in-play)
        for card in self.cards:
            if card.status == status and card.in_play:
                available_cards.append(card.word)
        
        return available_cards
    
    
    # Return list of all possible combinations of N cards for the given team
    def clusters(self, team, N):
        team_cards = self.get_words(team)
        clusters = list(combinations(team_cards, N))
        return clusters
    
    
    # Check if phrase consists of one or multiple words
    def single_word(self, word):
        return (False if '_' in word else True)
    
    
    # Check that a word does not share a root with any word on the board
    def is_unique(self, word):
        stemmer = stem.SnowballStemmer("english")
        root = stemmer.stem(word)
        for card in self.cards:
            if root == stemmer.stem(card.word):
                return False
        return True
    
    
    # Return True if word has not been used as a clue yet
    def is_new(self, word):
        return False if word in self.used else True
    
    
    # Return True if a word is a valid clue
    def is_valid(self, word):
        if (
                self.single_word(word)
                and self.is_unique(word)
                and self.is_new(word)
                ):
            return True
        else:
            return False