#!/usr/bin/python3

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:val for key, val in zip(letters, points)}
letter_to_points[" "] = 0
#for key, val in zip(letters, points):
#	print(f"{key} = {val} pts")

def score_word(word):
	point_total = 0
	for char in word:
		if char.upper() in letter_to_points:
			point_total += int(letter_to_points.get(char.upper()))
		else:
			point_total += 0
#	print(f"Point total for {word} is {point_total}")
	return point_total
	
def play_word(player, word):
	global player_to_words
	player_to_words[player].append(word)
	
player_to_words = {	'player1'   : ["BLUE", "TENNIS", "EXIT"],
             		'wordNerd'   : ["EARTH", "EYES", "MACHINE"],
             		'Lexi Con' : ["ERASER", "BELLY", "HUSKY"],
             		'Prof Reader' : ["ZAP", "COMA", "PERIOD"] }

def update_point_totals():
	global player_to_words
	player_to_points = {}
	for player in player_to_words:
		player_points = 0
		words = player_to_words[player]
		for word in words:
			player_points += score_word(word)
		player_to_points[player] = player_points
		print(f"{player} has {player_to_points[player]} pts.")

play_word("player1", "SCOPA")
update_point_totals()
print(player_to_words[player])
