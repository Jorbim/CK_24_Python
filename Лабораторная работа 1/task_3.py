list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

a=len(list_players) # общее кол-во игроков

b= a//2 # делим на 2 команды

e = list_players[:b] # команда 1
d = list_players[b:] # команда 2

print(e)
print(d)
