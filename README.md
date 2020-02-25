# codenames
Codenames "spymaster" bot

This project is a work in progress. I'll be updating this document with more information soon, and updates to the code to follow.

gameboard.py
This file contains the code to define and interact with the game components:
1. Creates and stores 25 Card objects, each one having a unique word, a team assignment and an in-play status.
2. Stores all relevant info about the particular game (e.g. - clues given, in-play words)
3. Provides all functions required to interact with the gameboard (e.g. - selecting a card, and checking a clue would be valid)

player.py
This file contains the code to define and access player-logic:
1. Uses various tools from NLTK to understand the words on the board and generate clues
2. The game allows for multiple types of players using different logics or able to identify different types of clues
3. Player logic is still in-progress. The public file is relatively simple version using Word2Vec and the publicly available, pre-trained Google News vectors.
