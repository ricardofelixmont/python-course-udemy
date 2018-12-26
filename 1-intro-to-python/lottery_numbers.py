lottery_numbers = {13, 21, 22, 5, 8}


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""
players = [{'name':'Caio','numbers':{2,5,4,8,6}}, {'name':'Andre','numbers':{4,13,7,2,3}}]
print(players)
"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers. We still cannot use f-strings in this exercise.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""
for player in players:

    print('Player {} got {} numbers right.'.format(player['name'], len((lottery_numbers & player['numbers']))))


# if i want to show one by one
# print('Player {} got {} numbers right. Player {} got {} numbers right'.format(players[0]['name'], len((lottery_numbers & players[0]['numbers'])),players[1]['name'], len((lottery_numbers & players[1]['numbers']))))

