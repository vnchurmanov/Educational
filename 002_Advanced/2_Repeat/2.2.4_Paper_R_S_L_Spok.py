player_1, player_2 = (input() for _ in range(2))
choices = ['Спок', 'ножницы', 'бумага', 'камень', 'ящерица']
winners = ['ничья', 'Player_2', 'Player_1', 'Player_2', 'Player_1']
print(winners[choices.index(player_1) - choices.index(player_2)])
