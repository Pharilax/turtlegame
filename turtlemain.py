import turtle as turt # Used for displaying the game
import os # Used to clear screen
from random import randint # Used for player picking / question selection

''' Turtle program
This is a game that creates three players and has the user answer questions
in order to advance to the end of the game board. '''

# Creates the game window
wn = turt.Screen()
wn.setup(width=1100, height=350, starty=25)
wn.bgcolor("lightblue")
wn.title("Turtle game - Matt Virian")

def gameboard(): # Draws the game board
	# Alex is the gameboard maker
	alex = turt.Turtle()
	alex.hideturtle()
	alex.color("green")
	alex.pensize(2)
	alex.speed(200)
	alex.penup()
	alex.setpos(-450, -150)
	alex.left(90)
	alex.pendown()
	while alex.position()[0] <= 400:
		alex.forward(300)
		alex.right(90)
		alex.forward(75)
		alex.right(90)
		alex.forward(300)
		alex.left(90)
		alex.forward(75)
		alex.left(90)
	alex.forward(300)
	alex.left(90)
	while alex.position()[1] >= -250:
		alex.forward(900)
		alex.left(90)
		alex.penup()
		alex.forward(100)
		alex.left(90)
		alex.pendown()
		alex.forward(900)
		alex.right(90)
		alex.penup()
		alex.forward(100)
		alex.right(90)
		alex.pendown()
	alex.penup()
	alex.setpos(375, 150)
	alex.color("red")
	alex.pendown()
	alex.left(90)
	alex.forward(300)
gameboard()

def first_pick(): # Picks starting player
	print("Picking first player...")
	playerpick = randint(0, 2) # Picks a random number from 1 to 3
	if playerpick == 0:
		print("Current player is Orange!\n") # 0 is Orange
	elif playerpick == 1:
		print("Current player is Yellow!\n") # 1 is Yellow
	elif playerpick == 2:
		print("Current player is Blue!\n") # 2 is Blue
	return playerpick # Returns player value to current_player var

def rest_pick(current_player_rest): # Picks player for next turn
	print("Picking next player...")
	# if statements eval current player
	if current_player_rest == 0: 
		print('Current player is Yellow!\n') # Changes from 0 to 1
		current_player_rest = 1
		return current_player_rest
	elif current_player_rest == 1:
		print('Current player is Blue!\n') # Changes from 1 to 2
		current_player_rest = 2
		return current_player_rest
	elif current_player_rest == 2:
		print('Current player is Orange!\n') # Changes from 2 to 0
		current_player_rest = 0
		return current_player_rest

def player_move_correct(spaces): # Moves player forward x spaces if question right

	for i in range(0, spaces): # Used to loop movement x spaces

		if current_player == 0: # Orange moves
			p1.forward(75)
			p1_pos = list(p1.pos())
			if p1_pos[0] == 410: # Check for end of board
				break # Stops movement

		elif current_player == 1: # Yellow moves
			p2.forward(75)
			p2_pos = list(p2.pos())
			if p2_pos[0] == 410: # Check for end of board
				break # Stops movement

		elif current_player == 2: # Blue moves
			p3.forward(75)
			p3_pos = list(p3.pos())
			if p3_pos[0] == 410: # Check for end of board
				break # Stops movement

		else: # Catch anything else
			print('error')

def player_move_incorrect(spaces): # Moves player backward x spaces if question wrong

	for i in range(0, spaces): # Used to loop movement x spaces

		if current_player == 0: # Orange moves
			p1_pos = list(p1.pos())
			if p1_pos[0] == -490: # Check for beginning of board
				break # Stop movement
			p1.back(75) # Moves back one space

		elif current_player == 1: # Yellow moves
			p2_pos = list(p2.pos())
			if p2_pos[0] == -490: # Check for beginning of board
				break # Stop movement
			p2.back(75) # Moves back one space

		elif current_player == 2: # Blue moves
			p3_pos = list(p3.pos())
			if p3_pos[0] == -490: # Check for beginning of board
				break # Stop movement
			p3.back(75) # Moves back one space

		else: # Catches anything else
			print('error') 

def check_end_game(): # Checks if any player wins
	if current_player == 0:
		p1_pos = list(p1.pos())
		if p1_pos[0] == 410: # Check for end of board
			return True # Returns winner is orange
		else:
			return False
	elif current_player == 1:
		p2_pos = list(p2.pos())
		if p2_pos[0] == 410: # Check for end of board
			return True # Returns winner is yellow
		else:
			return False
	elif current_player == 2:
		p3_pos = list(p3.pos())
		if p3_pos[0] == 410: # Check for end of board
			return True # Returns winner is blue
		else:
			return False

def questionpick(): # Picks difficulty of question

	while True: # Loops over question selection until game is done

		def questionpool(diff): # Picks actual question
			while True: # Loops to pick different questions after every turn

				global current_player # Allows editing of variable current_player
				quest_num = randint(0,4) # Decides question number

				if diff == 0: # Easy questions stored as dictionary
					easy = {
						'What is 2 + 2?': 4,
						'What is 10 - 5?': 5,
						'What is 4 * 4?': 16,
						'What is 20 + 10?': 30,
						'What is 8 * 0?': 0,
					}
					easy_keys = easy.keys() 
					question = (list(easy_keys)[quest_num]) # Gets question
					easy_values = easy.values()
					current_val = (list(easy_values)[quest_num]) # Gets answer to question

					while True: # Loops for error checking on user answer
						print(question) # Prints question
						try:
							user_ans = int(input('Please submit your answer: '))
							# Checks user input for answer

						except ValueError: # Catches anything that isn't an int
							print('Please input a number!')
							continue # Asks for answer again

						break # Escapes question loop

					if user_ans == current_val: # Right answer
						print('Correct!')
						print('Moving forward 1 space...')
						print('-' * 30)
						player_move_correct(1) # Moves the player
						if check_end_game() is True: # Game exit condition
							return # Exit questionpool()
						current_player = rest_pick(current_player) # Changes to next player
						break # Escapes question loop

					else: # Wrong answer
						print('Incorrect!')
						print('Moving backwards 3 spaces...')
						print('-' * 30)
						player_move_incorrect(3) # Moves the player
						current_player = rest_pick(current_player) # Changes to next player
						break # Escapes question loop

				elif diff == 1: # Medium questions
					medium = {
						'What is 50 * 5?': 250,
						'What is 11 * 11?': 121,
						'What is the square root of 49?': 7,
						'What is 2 to the 4th power?': 16,
						'What is 1/8 of 80?': 10,
					}
					medium_keys = medium.keys()
					question = (list(medium_keys)[quest_num]) # Gets question
					medium_values = medium.values()
					current_val = (list(medium_values)[quest_num]) # Gets answer to question
					
					while True: # Loops for error checking on user answer
						print(question) # Prints question
						try:
							user_ans = int(input('Please submit your answer: '))
							# Checks user input for answer

						except ValueError: # Catches anything that isn't an int
							print('Please input a number!')
							continue # Asks for answer again

						break # Escapes question loop

					if user_ans == current_val: # Right answer
						print('Correct!')
						print('Moving forward 2 spaces...')
						print('-' * 30)
						player_move_correct(2) # Moves the player
						if check_end_game() is True: # Game exit condition
							return # Exit questionpool()
						current_player = rest_pick(current_player) # Changes to next player
						break # Escapes question loop

					else: # Wrong answer
						print('Incorrect!')
						print('Moving backwards 2 spaces...')
						print('-' * 30)
						player_move_incorrect(2) # Moves the player
						current_player = rest_pick(current_player) # Changes to next player
						break # Escapes question loop

				elif diff == 2: # Hard questions
					hard = {
						'What is 27 * 47?': 1269,
						'What is 729 / 9?': 81,
						'What is 12 to the 4th power?': 20736,
						'What is the square root of 9025?': 95,
						'What is the factorial of 5?': 120,
					}
					hard_keys = hard.keys()
					question = (list(hard_keys)[quest_num]) # Gets question
					hard_values = hard.values()
					current_val = (list(hard_values)[quest_num]) # Gets answer to question

					while True: # Loops for error checking on user answer
						print(question) # Prints question
						try:
							user_ans = int(input('Please submit your answer: '))
							# Checks user input for answer

						except ValueError: # Catches anything that isn't an int
							print('Please input a number!')
							continue # Asks for answer again

						break # Escapes question loop

					if user_ans == current_val: # Right answer
						print('Correct!')
						print('Moving forward 3 spaces...')
						print('-' * 30)
						player_move_correct(3) # Moves the player
						if check_end_game() is True: # Game exit condition
							return # Exit questionpool()
						current_player = rest_pick(current_player) # Changes to next player
						break # Escapes question loop

					else: # Wrong answer
						print('Incorrect!')
						print('Moving backwards 1 space...')
						print('-' * 30)
						player_move_incorrect(1) # Moves the player
						current_player = rest_pick(current_player) # Changes to next player
						break # Escapes question loop

		quest_diff = randint(0, 2) # Decides question difficulty
		if quest_diff == 0: # Easy questions
			print("Question difficulty: easy.")
			print("1 space for correct, -3 for wrong.\n")
			questionpool(quest_diff) # Calls questionpool() for easy questions
		elif quest_diff == 1: # Medium questions
			print("Question difficulty: medium.")
			print("2 spaces for correct, -2 for wrong.\n")
			questionpool(quest_diff) # Calls questionpool() for medium questions
		elif quest_diff == 2: # Hard questions
			print("Question difficulty: hard.")
			print("3 spaces for correct, -1 for wrong.\n")
			questionpool(quest_diff) # Calls questionpool() for hard questions

		if check_end_game() is True: # Ensures a winner has been chosen
			return # Exits questionpick()


while True:
	# Clears the screen every time the game resets
	os.system('cls')

	# Creates the three players
	p1 = turt.Turtle()
	p1.penup()
	p1.setpos(-490, 100)
	p1.color("orange")
	p1.pensize(4)

	p2 = turt.Turtle()
	p2.penup()
	p2.setpos(-490, 0)
	p2.color("yellow")
	p2.pensize(4)

	p3 = turt.Turtle()
	p3.penup()
	p3.setpos(-490, -100)
	p3.color("blue")
	p3.pensize(4)

	current_player = first_pick() # Creates global variable for the current player
	questionpick() # Main game function

	# End of game
	# Runs only when player reaches the finish line
	print('Congratulations!')
	if current_player == 0:
		print("The winner is Orange!")
	elif current_player == 1: 
		print("The winner is Yellow!")
	elif current_player == 2:
		print("The winner is Blue!")

	while True: 
	# Used to check for user input
	# Loops until Y or N is typed
		ans = input('Play again? (Y/N) ') 
		if ans.upper() == 'Y': # Restarts game
			print('Playing again...')
			break
		elif ans.upper() == 'N': # Quits the game
			print('Exiting...')
			turt.bye()
			raise SystemExit
		else: # Catches any other input
			print('Please type Y or N!')
			continue

	p1.ht()
	p2.ht()
	p3.ht()
	# Resets the three turtles so that new players can be created

	continue # Loops if game is restarted
