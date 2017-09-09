'''
Programmer: Amitoj Gill
Date: 09/06/2017
Objective: The objective of this program is to ask user to guess blanks in a 
number of quotes. 
'''

import sys

def play_game():
	'''
	GOAL: play_game() functionn's goal is to run as program is exicuted and it calls 
	all the sub functions
	INPUTS: No input
	OUTPUTS: Returns None
	'''

	current_game_mode, allowed_attempts = game_input()

	print "You have slected", current_game_mode + " game mode and you will get", str(allowed_attempts) +" guesses at each problem."

	current_content = content(current_game_mode)

	for element in current_content:
		border()
		text = element.get('text')
		current_answers = element.get('answers')
		current_quote_list = text.split()
		position = current_content.index(element)
		game_level = position + 1
		greetings(game_level,allowed_attempts)
		game_operation(current_quote_list, current_answers, game_level, allowed_attempts)
	
	game_won()
	return None


def game_operation(current_quote_list, current_answers, game_level, allowed_attempts):
	'''
	GOAL: game_operation() goals is to run internal operations of the game
	INPUTS: current_quote_list as a List, current_answers as a list, game_level as an 
	integer, allwed_attempts as an integer
	OUTPUTS: no return
	'''
	first_blank = find_first_blank(current_quote_list)
	string_quote = " ".join(current_quote_list) # converts the quote list back to 

	user_answer, current_blank = prompt(string_quote, first_blank)

	while find_first_blank(current_quote_list) != None:
		if check_answer(user_answer, current_blank, current_answers) == True:
			allowed_attempts = allowed_attempts
			current_quote_list = update_quote(current_quote_list,user_answer,current_blank)
			first_blank = find_first_blank(current_quote_list)
			if first_blank == None:
				print_complete_quote(current_quote_list)
			else:
				string_quote = " ".join(current_quote_list)
				user_answer, current_blank = prompt(string_quote, first_blank)
				
		else:
			allowed_attempts -= 1
			user_answer, current_blank =  wrong_answer(allowed_attempts, string_quote, first_blank)


def wrong_answer(allowed_attempts, string_quote, first_blank):
	'''
	GOAL: wrong_answer() goal is called when the answer is wrong
	INPUTS: allowed_attemmpts as an integer, string_quote as a string, 
	frist_blank as a string.
	OUTPUTS: if user is out of tries it calls game_lost() function, 
	else: askes user to try again.
	'''
	if allowed_attempts == 0:
		game_lost()
		
	else:
		try_again(allowed_attempts)
		user_answer, current_blank = prompt(string_quote, first_blank)
		return user_answer, current_blank


def border():
	'''
	GOAL: border() goal is to print a border as it is calls in 
	other functions
	INPUTS: No inputs
	OUTPUTS: no returns, it prints several lines to the screen. 
	'''
	print " "
	print "="*150
	print " "


def print_complete_quote(current_quote_list):
	'''
	GOAL: print_complete_quote() goal is to print completed string 
	after user gets all 
	the answers correct.
	INPUTS: current_quote_list as a list
	OUTPUTS: it prints joined string of the quote.
	'''
	string_quote = " ".join(current_quote_list)
	print " "
	print string_quote


def game_input():
	'''
	GOAL: game_imput() goal is to ask for user in put at the begging 
	of the program
	INPUTS: no imputs
	OUTPUTS: calls game_mode() and set_number_of_attempts() function
	'''
	border()
	current_game_mode =  game_mode() 
	border()
	allowed_attempts =  set_number_of_attempts()
	border()

	return current_game_mode, allowed_attempts

def greetings(game_level,allowed_attempts):
	'''
	GOAL: greetings() goal is to greet the user at begginging of each level
	INPUTS: game_level as an integer, allowed_attempts as an integer
	OUTPUTS: displays on screen a message about game level and number 
	attempts user has a given quote
	'''
	print "Welcome to level "+ str(game_level) + " !!!"
	print "Good Luck! You have " + str(allowed_attempts) + " trie(s) to answer this question."
	border()
	return None

def game_lost():
	'''
	GOAL: game_lost() function's goal is to let user know they lost 
	the game 
	INPUTS: no inputs
	OUTPUTS: prints a message on the screen letting user knwo they lost 
	and game i over.
	'''
	space = " "*25
	border()
	print space, "Sorry, You Lost"
	print space, "Good luck next time."
	print space, "GAME OVER"
	border()
	sys.exit()

def try_again(allowed_attempts):
	'''
	GOAL: try_again() function's goal is to let user know they need to try again 
	and numbe of attemts left. 
	INPUTS: allowed_attempts as a integer
	OUTPUTS: outputs to screen a message for trying again and nubmer of 
	attempts left.
	'''
	print " "
	print "That is not a correct answer, let's try again."
	print "You have " + str(allowed_attempts) + " trie(s) left. Good Luck!"

def game_won():
	'''
	GOAL: game_won() function's goal is to display congratulation message 
	after player won the game
	INPUTS: no input
	OUTPUTS: prints message on the screen and exits the program
	'''
	border()
	print "CONGRATULATIONS!!! YOU WON"
	border()
	sys.exit()


def update_quote(current_quote_list, correct_answer, current_blank):
	'''
	GOAL: update_quote() function's goal is to provide updated quote 
	with correct answer
	INPUTS: current_quote_list as a list, correct_answer as a string, 
	and current_blank as a string
	OUTPUTS: returns updated_quote as a list
	'''
	updated_quote = []
	update_word = ""
	blank_length = len(current_blank)

	for word in current_quote_list:
		blank = word[:blank_length]
		
		if blank == current_blank:
			#print blank
			update_word = correct_answer + blank_in_word(word)
			updated_quote.append(update_word)
		else:
			updated_quote.append(word)


	return updated_quote


def find_first_blank(current_quote_list):
	'''
	GOAL: find_first_blank() function's goal is to find the first blank 
	in a given quote list
	INPUTS: current_quote_list as a list
	OUTPUTS: rerutns first_blank as a string
	'''

	for word in current_quote_list:
		if word != blank_in_word(word):
			first_blank = word[:7]
			#print first_blank
			break
		else:
			first_blank = None
			

	return first_blank

def game_mode():
	'''
	GOAL: game_mode() function's goal is to ask user for game mode 
	they wish to play
	INPUTS: Takes an input from the user as a string
	OUTPUTS: returns the mode of the game.
	'''
	valid_inputs = ["M","m", "E", "e", "H", "h"]
	mode = raw_input("Which game mode would you like to play?\nEnter: E for Easy | M for Medium | H for hard\n").lower()

	while mode not in valid_inputs:
		mode = raw_input("Which game mode would you like to play?\nEnter: E for Easy | M for Medium | H for hard\n").lower()

	if mode == "m":
		return "Medium"
	elif mode == "h":
		return "Hard"
	else: 
		return "Easy"



def set_number_of_attempts():
	'''
	GOAL: set_number_of_attempts() function's goal is to set number attempts
	user can have per quote. 
	INPUTS: get's a input from the user
	OUTPUTS: returns attempts as an integer
	'''
	attempts = int(input("How many attempts would you like per quote?\nEnter: an integer\n")) 
	return attempts


def content(mode):
	'''
	GOAL: content() function's goal is to provide content based os game mode 
	INPUTS: mode input as a string
	OUTPUTS: list of quotes in content variable.
	'''
	content = []

	quotes = [
	{'level':'Hard',
	'text':'I have a ___1___ that my four little ___2___ will one day live in a ___3___ where they will not be judged by the color of their ___4___, but by the content of their ___5___. - Marthin Luther King Jr.',
	'answers':["dream","children","nation","skin","character"]},
	{'level':'Hard',
	'text':"It isn't the ___1___ ahead to climb that wear you down. It's the ___2___ in your ___3___. - Muhammad Ali",
	'answers':["mountains","pebble", "shoe"]},
	{'level':"Medium",
	'text':"If you can't ___1___ then ___2___, if you can't ___2___ then ___3___, if you can't ___3___ then ___4___, but whatever you do you have to keep moving ___5___. - Martin Luther King Jr.",
	'answers':["fly","run","walk","crawl","forward"]},
	{'level':"Medium",
	'text':"An ___1___ for an ___1___ only ends up making the whole world ___2___. - Mahatma Gandhi",
	'answers':["eye","blind"]},
	{'level':'Hard',
	'text':"Try not to become a ___1___ of ___2___, but rather try to become a ___1___ of ___3___. - Albert Einstein",
	'answers':["man","success","value"]},
	{'level':'Easy',
	'text':"Change will not come if we ___1___ for some other ___2___ or some other ___3___. We are the ones we've been ___4___ for. We are the ___5___ that we seek. - Barck Obama",
	'answers':['wait','person','time','waiting','change']},
	{'level':'Medium',
	'text':"The world will not be ___1___ by those who do evil, but by those who ___2___ them without doing ___3___. - Albert Einstein",
	'answers':['destroyed', 'watch','anything']},
	{'level':'Easy',
	'text':"Not all of us can do ___1___ things. But we can do ___2___ things with ___1___ love. - Mother Teresa",
	'answers':['great','small' ]},
	{'level':'Easy',
	'text':"Don't ___1___ the ___2___, make the ___2___ ___1___. - Muhammad Ali",
	'answers':['count', 'days']}
	]

	for quote in quotes:
		if quote.get("level") == mode:
			content.append(quote)

	return content


def blank_in_word(word):
	'''
	GOAL: blank_in_word() function's goal is to check if the word 
	is a blank or not
	INPUTS: takes in word as a string
	OUTPUTS: returns result eihter a blank or the word both string.
	'''
	list_of_blanks = ["___1___","___2___","___3___", "___4___", "___5___"]
	result = ""

	for blank in list_of_blanks:
		blank_length = len(blank)

		#print blank

		if blank in word:
			result = word[blank_length:]
			break
		else:
			result = word
	return result

def prompt(quote,blank):
	'''
	GOAL: prompt() functions goal is to ask user for ansewer for 
	any given quote and a blank
	INPUTS: quote as a string, blank as a string
	OUTPUTS: returns user input as guess variable and blank 
	intially passed in.
	'''
	guess = ""

	if blank == None:
		return None
	else:
		print " "
		print quote
		print " "
		guess = raw_input("What should be substituted in for " + blank +" ? \n")

		return guess, blank


def check_answer(current_answer, current_blank, list_of_correct_answers):
	'''
	GOAL: check_answer() function's goal is to check if user anser 
	is the correct
	INPUTS: current_answer as a string, current_blank as a string, 
	list_of_correct_answers as a list
	OUTPUTS: if answer is correct returns True, else False, or Error 
	'''

	answer_index = int(current_blank.replace("_",""))-1

	#print i, len(list_of_correct_answers)
	if answer_index < len(list_of_correct_answers):
		if current_answer == list_of_correct_answers[answer_index]:
			return True
		else: 
			return False
	else:
		return "Error"


#test()

play_game() #exicutes the play_game() function 
