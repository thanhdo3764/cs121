import random
import time

class Player:
	def __init__(self, ox, tbt, ply):
		"""Initializer for class"""
		self.checker = ox
		self.tieBreakType = tbt
		self.ply = ply

	def __repr__(self):
		"""Representation for class"""
		represent = print('Checker: ', self.checker,
			'\nTie break type: ', self.tieBreakType,
			'\nPly: ', self.ply)
		return(represent)

	def nextMove(self, board):
		"""Returns best ai move for current board"""
		# Saves the score of the board for AI
		colScore = self.scoreFor(board, self.checker, self.ply)
		# Saves the columns with the highest score
		biggestCol = []
		# Reverse column order if tbt = 'Right'
		if self.tieBreakType == 'Right': 
			colOrder = range(board.width-1, -1, -1)
		# Keep column order same if tbt = 'Left'
		else:
			colOrder = range(board.width)
		# For each column Score in specified order
		for col in colOrder:
			# If score is 100
			if colScore[col] == 100:
				biggestCol.append(col)
			# If score is 50 and there is no score higher
			elif colScore[col] == 50 and max(colScore) == 50:
				biggestCol.append(col) 
			# If score is 0 and there is no score higher
			elif colScore[col] == 0 and max(colScore) == 0:
				biggestCol.append(col) 
		# Randomize which col to return if tbt = 'Random'
		if self.tieBreakType == 'Random':
			randIndex = random.randint(0,len(biggestCol)-1)
			return biggestCol[randIndex]
		# Returns the first instance in biggestCol
		return biggestCol[0]

	def scoreFor(self, board, ox, ply):
		"""Returns a list of the score for each column.
		Score 100 means a win. Score 50 means default.
		Score 0 means a loss. Score -1 means col full.
		"""
		colScore = []
		for col in range(board.width):
			# If col isn't full
			if board.allowsMove(col):
				board.addMove(col, ox)
				# For Ply 1, if win in next move
				if board.winsFor(ox):
					colScore.append(100) #add 100 to score
				# For Ply > 1
				else:
					# Designates self and enemy
					if ply > 1:
						if ox == 'X':
							enemy = 'O'
						else:
							enemy = 'X'
						enemyScore = self.scoreFor(board, enemy, ply-1)
						# Added the following because ai wouldn't try to
						# block if enemy was guaranteed to win in the future
						# Only needs to be run by ai once within recursion
						if ply == self.ply:
							# evaluates previous enemy score without move
							board.delMove(col)
							preEnemyScore = self.scoreFor(board, enemy, 1)
							board.addMove(col, ox)
							# Max enemyScore cannot be -1
							# and don't calculate score if col is an enemy win.
							if max(enemyScore) != -1 and preEnemyScore[col] != 100:
								# Calculates score and adds to colScore
								colScore.append(100-max(enemyScore))
							# If enemy's max score is -1 or col is an enemy win
							else:
								colScore.append(50)
						# If this is a recursion of original function
						else:
							# Max enemyScore cannot be -1
							if max(enemyScore) != -1:
								# Calculates score and adds to colScore
								colScore.append(100-max(enemyScore))
							# If enemy's max score is -1
							else:
								colScore.append(50)
					# ply less than 1
					else:
						colScore.append(50)
				board.delMove(col)
			# col is full
			else:
				colScore.append(-1)
		return colScore

class Connect4:
	def __init__(self, width, height):
		"""Initializer for class"""
		self.width = width
		self.height = height
		self.data = []
		# Creates board data
		for row in range(self.height):
			boardRow = []
			for col in range(self.width):
				boardRow += [' ']
			self.data += [boardRow]
		
	def __repr__(self):
		"""Representation for class"""
		s = ''
		# Creates board representation
		for row in range(self.height):
			s += '|'
			for col in range( self.width ):
				s += self.data[row][col] + '|'
			s += '\n'
		# Creates horizontal separator
		for i in range(2 * self.width + 1):
			s += '-'
		s += '\n'
		# Creates indices of each column
		for i in range(self.width):
			s += ' ' + str(i % 10)
		return s # return string
	
	def addMove(self, col, ox):
		"""Adds move at col, at lowest row, for ox"""
		# Starting from the bottom of the board
		for row in range(self.height-1, -1, -1): 
			# If the space is empty
			if self.data[row][col] == ' ':
				# Replace the space with ox
				self.data[row][col] = ox
				break

	def clear(self):
		"""Clears board by replacing data with empty space"""
		for row in range(self.height):
			for col in range(self.width):
				self.data[row][col] = ' '
	
	def delMove(self, col):
		"""Removes uppermost checker in col"""
		for row in range(self.height):
			# If upper most row in col is not empty
			if self.data[row][col] != ' ':
				# Replace checker with ' '
				self.data[row][col] = ' '
				break
	
	def allowsMove(self, col):
		"""Returns a boolean.
		Returns True if col is valid and top row is empty.
		Returns False otherwise.
		"""
		if col in range(self.width) and self.data[0][col] == ' ':
			return True
		else:
			return False

	def availableRow(self, col):
		"""Returns the lowest empty row at col"""
		for row in range(self.height-1, -1, -1): 
			if self.data[row][col] == ' ':
				return row
	
	def isFull(self):
		"""Returns a boolean.
		Returns False when sum of allowsMove for each col is zero.
		Returns True otherwise.
		"""
		counter = 0
		for i in range(self.width):
			counter += self.allowsMove(i)
		if counter == 0:
			return True 
		else:
			return False

	def winsFor(self,ox):
		"""Returns a boolean.
		Returns True if ox wins for any orientation
		Returns False if not
		"""
		# Checks win horizontal
		for row in range(self.height):
			for col in range(self.width - 3):
				if (
					self.data[row][col] == ox
					and self.data[row][col+1] == ox
					and self.data[row][col+2] == ox
					and self.data[row][col+3] == ox
					):
					return True 
		# Checks win vertical
		for row in range(self.height-3):
			for col in range(self.width ):
				if (
					self.data[row][col] == ox
					and self.data[row+1][col] == ox
					and self.data[row+2][col] == ox
					and self.data[row+3][col] == ox
				   ):
					return True
		# Checks win NE to SW
		for row in range(self.height-3):
			for col in range(3, self.width):
				if (
					self.data[row][col] == ox
					and self.data[row+1][col-1] == ox
					and self.data[row+2][col-2] == ox
					and self.data[row+3][col-3] == ox
					):
					return True
		# Checks win NW to SE
		for row in range(self.height-3):
			for col in range(self.width - 3):
				if (
					self.data[row][col] == ox
					and self.data[row+1][col+1] == ox
					and self.data[row+2][col+2] == ox
					and self.data[row+3][col+3] == ox
				   ):
					return True
		# Return False if no win
		return False
	
	def hostGame(self):
		"""Creates game for player vs player.
		Players input col, then the board updates.
		"""
		# For each turn on the board
		for turn in range(self.width * self.height):
			print(self)
			# Player X if turn even, O if not
			if turn % 2 == 0:
				player = 'X'
			else:
				player = 'O'
			print('Player ', player, ' turn')
			# Asks for colNum input
			colNum = int(input('Choose a column. . . '))
			# Keep asking for colNum if input is invalid
			while self.allowsMove(colNum) == False:
				colNum = int(input('Invalid Column.\n Choose a column. . . '))
			# Add player checker at colNum
			self.addMove(colNum, player)
			# If the player just won or board is full
			if self.winsFor(player):
				print(self)
				print('Player ', player, ' wins!')
				self.clear()
				break
			elif self.isFull():
				print(self)
				print('Full board. Tie game.')
				self.clear()

	def playGameWith(self, aiPlayer):
		"""Creates game for player vs AI.
		Game shifts between human and AI depending on turn.
		Game asks human input for move or calculates AI move
		and then updates board.
		"""
		for turn in range(self.width * self.height):
			print(self)
			# Player X if turn even, O if not
			if turn % 2 == 0:
				player = 'X'
			else:
				player = 'O'
			print('Player ', player, ' turn')
			# Ask for user input if player is X
			if player == 'X':
				colNum = int(input('Choose a column. . . '))
				# Keep asking for colNum if input is invalid
				while self.allowsMove(colNum) == False:
					colNum = int(input('Invalid Column.\n Choose a column. . . '))
				# Add player checker to colNum
				self.addMove(colNum, player)
			# Calculates and adds AI move if player is O
			else:
				oMove = aiPlayer.nextMove(self)
				print('Player O chose column ', oMove)
				self.addMove(oMove, 'O')
			# If the player just won or board is full
			if self.winsFor(player):
				print(self)
				print('Player ', player, ' wins!')
				self.clear()
				break
			elif self.isFull():
				print(self)
				print('Full board. Tie game.')
				self.clear()

	def playAIGame(self, aiPlayer1, aiPlayer2):
		"""Creates a game for AI vs AI.
		Switches between 2 AIs turn.
		"""
		for turn in range(self.width * self.height):
			print(self)
			if turn % 2 == 0:
				player = 'X'
			else:
				player = 'O'
			print('\nPlayer ', player, ' turn')
			if player == 'X':
				move = aiPlayer1.nextMove(self)
			if player == 'O':
				move = aiPlayer2.nextMove(self)
			print('Player', player, ' chose column ', move)
			self.addMove(move, player)
			time.sleep(0.5)
			#if the player just won or board is full
			if self.winsFor(player):
				print(self)
				print('Player ', player, ' wins!')
				self.clear()
				break
			elif self.isFull():
				print(self)
				print('Full board. Tie game.')
				self.clear()
				
def main():
	# Player(ox, tbt, ply)
	ai1 = Player('X', 'Left', 2)
	ai2 = Player('O', 'Left', 2)
	# Connect4(width, height)
	b = Connect4(7,6)
	#b.addMove(0, 'O'), b. addMove(1, 'O'), b. addMove(2, 'O'), b.addMove(0, 'X'), b.addMove(1, 'X'), b.addMove(2, 'X'), b.addMove(0, 'X'), b.addMove(1, 'O'), b.addMove(2, 'O'), b.addMove(0, 'X'), b.addMove(1, 'O'), b.addMove(0, 'O'), b.addMove(0, 'X'), b.addMove(0, 'X'), b.addMove(0, 'X'), b.addMove(0, 'X')
	b.playAIGame(ai1,ai2)
	#b.playGameWith(ai2)


if __name__ == '__main__':
	main()