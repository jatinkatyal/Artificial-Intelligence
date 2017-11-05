class Tree:
	"""
		Class to hold tree with all possibilities 
		of the game
	"""
	def __init__(self,board,path=[]):
		self.board = board[:]
		self.children = []
		self.path = path
		self.populate()
	
	def populate(self):
		"""
			Generates possible future states from 
			current board
		"""
		for i in getMoves(self.board):
			temp = self.board[:]
			temp[i] = 'X'
			for j in getMoves(temp):
				temp2=temp[:]
				temp2[j] = 'O'
				path = self.path[:]
				path.append(i)
				temp2 = Tree(temp2,path)
				self.children.append(temp2)

def checkWin(board):
	"""
		Checks if game is won by a player or not,
		can return false on draw or incomplete 
		game. Also returns winner if won.
	"""
	for i in range(3):
		if board[i*3] and board[i*3]==board[i*3+1] and board[i*3]==board[i*3+2]:
			return True,board[i*3]
		if board[i] and board[i]==board[i+3] and board[i]==board[i+6]:
			return True,board[i+3]
	if board[0] and board[0]==board[4] and board[0]==board[8]:
		return True,board[0]
	if board[2] and board[2]==board[4] and board[2]==board[6]:
		return True,board[2]
	return False,'None'

def getMoves(board):
	"""
		Returns list of empty board locations
	"""
	moves = []
	for i in range(len(board)):
		if board[i]=='':
			moves.append(i)
	return moves

def display(board):
	"""
		Displays board
	"""
	for i in range(9):
		if i%3==0 and i>0:
			print()
		if board[i]:
			print(board[i],end='')
		else:
			print(' ',end='')
	print()

def makeMove(board,turn):
	"""
		Prompts user to make a move otherwise 
		makes a move for system
	"""
	if turn:
		pos = bestMove(board)
		board[pos]='X'
		print("System Marked at "+str(pos+1))
	else:
		pos = int(input("Enter position to mark: "))-1
		if pos in getMoves(board):
			board[pos] = 'O'
		else:
			print("Invalid Move")
			makeMove(board,turn)

def bestMove(board):
	"""
		Determines a move for system, should take 
		less time to deterimine as game progresses
	"""
	tree = Tree(board)
	moves = getMoves(board)
	winningMoveCount = [0 for i in moves]
	queue = [tree]
	while queue:
		current = queue.pop(-1)
		state,winner = checkWin(current.board)
		if state and winner=='X':
			for move in moves:
				if move in current.path:
					winningMoveCount[moves.index(move)]+=2
		elif state and winner=='O':
			for move in moves:
				if move in current.path:
					winningMoveCount[moves.index(move)]-=2
		for child in current.children:
			queue.append(child)
	print([i+1 for i in moves],winningMoveCount)
	return moves[winningMoveCount.index(max(winningMoveCount))]


if __name__=='__main__':
	board = ['','','','','','','','','']
	turn = False
	while getMoves(board):
		makeMove(board,turn)
		display(board)
		state,winner = checkWin(board)
		if state:
			break
		turn = not turn
	print(str(winner)+" won!")