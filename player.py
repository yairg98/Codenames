# -*- coding: utf-8 -*-
"""
Codenames Board Generator

@author: yairg
"""

# Python NLTK library - Stemming (eliminates prefixes and suffixes)
# Python statistics library
# Use "restrict_vocab=50000" in gensim most_similar function to limit range of results


import gameboard
from gensim.models import KeyedVectors


class Player:
    
    # Use pre-trained word2vec model (Google News)
    model = KeyedVectors.load_word2vec_format(
        'GoogleNews-vectors-negative300.bin.gz', binary=True, limit=1250000
        )
    
    def __init__(self, board, team):
        self.board = board
        self.team = team
    

    # Return a list of valid potential clue words for a given cluster
    def most_similar(self, cluster, N=10):
        valid_clues = []
        most_similar = Player.model.most_similar(cluster, topn=N, restrict_vocab=40000)
        for clue in most_similar:
            if self.board.is_valid(clue[0]):
                valid_clues.append(clue[0])
        return valid_clues
    
    
    def max_distance(self, clue, cluster):
        distance = 1
        similarity = 1
        for word in cluster:
            similarity = Player.model.similarity(clue, word)
            if similarity < distance:
                distance = similarity
        return distance
    
    
    # Return the best clue for a given cluster
    def best_in_cluster(self, cluster):
        clues = self.most_similar(cluster)
        best = [0,0]
        for clue in clues:
            distance = self.max_distance(clue, cluster)
            if distance > best[1]:
                best[0] = clue
                best[1] = distance
        return best
    
    
    # Find the best clue for a given team and number of cards
    def find_best(self, N):
        best = [0,0]
        for cluster in self.board.clusters(self.team, N):
            print("Cluster: ")
            print(cluster)
            best_in_cluster = self.best_in_cluster(cluster)
            print(best_in_cluster)
            if best_in_cluster[1] > best[1]:
                best[0] = best_in_cluster[0]
                best[1] = best_in_cluster[1]
                best_cluster = cluster
        print(best_cluster)
        return best

    