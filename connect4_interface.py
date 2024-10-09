from tkinter import *
from tkinter.font import *
from connect4_Game import *
from time import sleep

# Setup gameboard
height = 800 #height of root
canvasHeight = height*9/10
countRow = 6
countCol = 7
# Adjusts diameter to larger side
if countRow > countCol:
	countMore = countRow
else:
	countMore = countCol
diameter = (canvasHeight - canvasHeight/10)/countMore
width = int(diameter*countCol + height/10 + 500) # width of root

# Setup window
root = Tk()
root.configure(bg='grey90')
root.geometry(str(width)+'x'+str(height))
root.title('Connect 4')
# centers the contents in root
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
myFont = Font(family='gill sans', size=int(30*height/800))

# Setup game
game = Connect4(countCol, countRow)
ai = Player('O', 'Random', 7)

# frame parent
frame = Frame(root, bg='grey90')
# Children of frame
instructions = Label(
	frame,
	text='Click to move in a column. Get 4 in a row to win!',
	font=myFont,
	height=2,
	bg = 'grey90'
	)
instructions.grid(
	pady=height/160,
	row=0,
	column=0,
	columnspan=countCol+2)
# Displays game text
label = Label(
	frame,
	text='Player Black\'s Turn',
	font=myFont,
	width=20,
	height=2,
	relief='sunken',
	bd=3,
	)
label.grid(
	padx=height/40,
	pady=height/160,
	row=1,
	column=countCol+3,
	sticky='N',
	)
# Displays the board
canvas = Canvas(
	frame,
	width=diameter*countCol + diameter/2,
	height=diameter*countRow + diameter/2,
	bg='yellow',
	highlightbackground='yellow3',
	highlightthickness=int(diameter/10),
	)
canvas.grid(
	padx=height/40,
	pady=height/400,
	row=1,
	column=0,
	rowspan=4,
	columnspan=countCol+2,
	)
# Shows board index
for i in range(countCol):
	colIndex = Label(
		frame,
		text=str(i%10),
		font=myFont,
		bg='grey90',
		)
	colIndex.grid(
		row=5,
		column=i+1,
		)

# Modifying canvas
circles = []
smallerCircles = []
# Regular circles
y = diameter/4
for row in range(countRow):
	circleRow = []
	x = diameter/4
	for col in range(countCol):
		circle = canvas.create_oval(
			x,
			y,
			x+diameter,
			y+diameter,
			fill='grey90',
			outline='yellow2',
			width=diameter/10,
			)
		circleRow.append(circle)
		x += diameter
	y += diameter
	circles.append(circleRow)
# Smaller circles for detail
y = diameter/4
for row in range(countRow):
	circleRow = []
	x = diameter/4
	for col in range(countCol):
		circle = canvas.create_oval(
			x + diameter/8,
			y + diameter/8,
			x + diameter*7/8,
			y + diameter*7/8,
			fill='grey90',
			width=0,
			)
		circleRow.append(circle)
		x += diameter
	y += diameter
	smallerCircles.append(circleRow)

# menuFrame parent
menuFrame = Frame(root, bg = 'grey90')

def resetGame():
	"""Resets frame, canvas, and game to default settings"""
	global turn
	playAgainButton.grid_remove()
	menuButton.grid_remove()
	turn = 0
	game.clear()
	#resets visual board
	for row in range(countRow):
		for col in range(countCol):
			recolor(row, col)

def menuReturn():
	"""Hides game and displays menu"""
	frame.grid_remove()
	menuFrame.grid()

def recolor(row, col):
	"""Fills canvas circles to default color"""
	canvas.itemconfig(circles[row][col], fill = 'grey90')
	canvas.itemconfig(smallerCircles[row][col], fill = 'grey90')

def fillCircles(col, player):
	"""Animates canvas circle at designated col for designated player"""
	# For each available row in a col
	for row in range(game.availableRow(col)+1):
		if player == 'X': 
			# Fill row at col with black if player is X
			canvas.itemconfig(
				circles[row][col],
				fill='grey20',
				)
			canvas.itemconfig(
				smallerCircles[row][col],
				fill='grey5',
				)
			canvas.update()
			time.sleep(0.01)
		else:
			# Fill row at col with red if player is O
			canvas.itemconfig(
				circles[row][col],
				fill='red',
				)
			canvas.itemconfig(
				smallerCircles[row][col],
				fill='red3',
				)
			canvas.update()
			time.sleep(0.01)
		# Recolors circle except the lowest available row
		if row < game.availableRow(col):
			recolor(row, col)

def mouseInputHuman(event):
	"""Decides player and color based on round turn.
	Receives player move with mouse click, then updates game.
	"""
	global turn
	# Setup for player X
	if turn % 2 == 0: 
		player = 'X'
		playerColor = 'Black'
		otherPlayer = 'Red'
	# Setup for player O
	else:
		player = 'O'
		playerColor =  'Red'
		otherPlayer = 'Black'
	# Registers which col player clicked
	col = int((event.x - diameter/4)/diameter)
	# If mouse click is valid
	if game.allowsMove(col):
		# Don't allow clicks until turn is finished
		canvas.unbind('<Button-1>')
		# Animate move
		fillCircles(col, player)
		# Add move to game
		game.addMove(col, player)
		# Now next players turn
		label['text'] = 'Player '+ otherPlayer+'\'s Turn'
		turn += 1
		canvas.bind('<Button-1>', mouseInputHuman)
	# If the player just won or game is full
	if game.winsFor(player):
		label['text'] = 'Player '+ playerColor+ ' Wins'
		# Stop input and reveal hidden buttons
		canvas.unbind('<Button-1>')
		playAgainButton.grid()
		menuButton.grid()
	elif game.isFull():
		label['text'] = 'Full board.\nTie game.'
		# Stop input and reveal hidden buttons
		canvas.unbind('<Button-1>')
		playAgainButton.grid()
		menuButton.grid()

def aiTurn():
	"""Calculates ai move of current board then updates game"""
	# Calculates ai move
	col = ai.nextMove(game)
	label['text'] = 'Computer(Red) went\ncolumn ' + str(col)
	label.update()
	# Animate move
	fillCircles(col, 'O')
	# Add move to game
	game.addMove(col, 'O')
	time.sleep(0.7) # Gives human reading time
	# ai turn over, now human turn
	label['text'] = 'Your(Black) Turn'
	# Allow mouse click again
	canvas.bind('<Button-1>', mouseInputAI)
	# If ai wins or board is full
	if game.winsFor('O'):
		label['text'] = 'Computer(red) Wins'
		# Stop input and reveal hidden buttons
		canvas.unbind('<Button-1>')
		playAgainButton.grid()
		menuButton.grid()
	elif game.isFull():
		label['text'] = 'Full Board.\nTie Game.'
		# Stop input and reveal hidden buttons
		playAgainButton.grid()
		menuButton.grid()
		canvas.unbind('<Button-1>')

def mouseInputAI(event):
	"""Receives human move with mouse click and updates game.
	After human turn, let ai make their move.
	"""
	# Registers which col human chose
	col = int((event.x-diameter/4)/diameter)
	# If invalid move, end function
	if game.allowsMove(col) != True:
		return
	# If valid move, don't allow more input until AI turn finished
	canvas.unbind('<Button-1>')
	# Animate move
	fillCircles(col,'X')
	# Add move to game
	game.addMove(col,'X')
	# If human won or board is full
	if game.winsFor('X'):
		label['text'] = 'You(Black) Win'
		# Stop input and reveal hidden buttons
		canvas.unbind('<Button-1>')
		playAgainButton.grid()
		menuButton.grid()
	elif game.isFull():
		label['text'] = 'Full Board.\n Tie Game.'
		# Stop input and reveal hidden buttons
		canvas.unbind('<Button-1>')
		playAgainButton.grid()
		menuButton.grid()
	else:
		root.after(0, aiTurn) # Slight pause before ai turn

def createGameHuman():
	# Resets game, circles, and turn, and hides play again and menu
	resetGame()
	label['text'] = 'Player Black\'s Turn' # Default text
	# Indicate what game mode playAgainButton will play
	playAgainButton['command'] = createGameHuman 
	# Close menu and open PVP game
	menuFrame.grid_remove()
	frame.grid()
	# Bind mouse click for PVP
	canvas.bind("<Button-1>", mouseInputHuman)

def createGameAI():
	# Resets game, circles, and turn, and hides play again and menu
	resetGame()
	label['text'] = 'Your(Black) Turn' # Default text
	# Indicate what game mode playAgainButton will play
	playAgainButton['command'] = createGameAI
	# Close menu and open PVP game
	menuFrame.grid_remove()
	frame.grid()
	# Bind mouse click for PvAI
	canvas.bind("<Button-1>", mouseInputAI)

def quitGame():
	root.destroy()

# Menu buttons
pvpButton = Button(
	menuFrame,
	text='Player VS Player',
	font=myFont,
	width=20,
	height=2,
	command=createGameHuman,
	bg='red',
	)
pvpButton.grid(
	padx=5,
	pady=5,
	)
pvAIButton = Button(
	menuFrame,
	text='Player VS AI',
	font=myFont,
	width=20,
	height=2,
	command=createGameAI,
	)
pvAIButton.grid(
	padx=5,
	pady=5,
	)

# Frame buttons
playAgainButton = Button(
	frame,
	text='Play Again',
	font=myFont,
	height=2,
	width=20,
	)
playAgainButton.grid(
	padx=height/40,
	pady=height/160,
	row=2,
	column=countCol+3,
	)
menuButton = Button(
	frame,
	text='Return to Menu',
	command=menuReturn,
	font=myFont,
	height=2,
	width=20,
	)
menuButton.grid(
	padx=height/40,
	pady=height/160,
	row=3,
	column=countCol+3,
	)
quitButton = Button(
	frame,
	text='Quit',
	command=quitGame,
	font=myFont,
	height=2,
	width=20,
	)
quitButton.grid(
	padx=height/40,
	pady=height/160,
	row=4,
	column=countCol+3,
	sticky='S')

def main():
	# AI adjustable at line 31
	menuFrame.grid()
	root.mainloop()

if __name__ == '__main__':
	main()