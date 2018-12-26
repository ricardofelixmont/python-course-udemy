#!/usr/bin/env python3.6
class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    # 3 - indexing
    def __getitem__(self, index):
        return self.players[index]

    def __repr__(self):
        return f'Club {self.name}: {self.players}'
    
    def __len__(self):
        return len(self.players)

    def __str__(self):
        return f'Club {self.name}: with {len(self.players)} players.'

# 1 - Create an object 
some_club = Club('Arsenal')

# 2 - add players to the team
some_club.players.append('Carlos')
some_club.players.append('Ricardo')

# 3 - access players list with indexing like some_club[0]
# Utilizei o dunder method __getitem__
print(some_club[0])

# 4 - 
print(some_club)

