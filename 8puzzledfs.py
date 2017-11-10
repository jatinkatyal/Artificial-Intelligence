sol = [1,2,3,4,5,6,7,8,0]
current = [5,7,1,8,0,2,3,6,4]

'''
0 1 2
3 4 5
6 7 8
'''
def dispBoard(board):
	i=0
	while i<9:
		if i%3==0:
			print()
		print(str(board[i])+' ',end='')
		i+=1
	print()


def getMoves(board):
	moves = []
	pos = board.index(0)
	if pos < 6:
		boardCpy=board[:]
		boardCpy[pos],boardCpy[pos+3]=boardCpy[pos+3],boardCpy[pos]
		moves.append(boardCpy)
	if pos >2:
		boardCpy=board[:]
		boardCpy[pos],boardCpy[pos-3]=boardCpy[pos-3],boardCpy[pos]
		moves.append(boardCpy)
	if pos in [0,1,3,4,6,7]:
		boardCpy=board[:]
		boardCpy[pos],boardCpy[pos+1]=boardCpy[pos+1],boardCpy[pos]
		moves.append(boardCpy)
	if pos in [1,2,4,5,7,8]:
		boardCpy=board[:]
		boardCpy[pos],boardCpy[pos-1]=boardCpy[pos-1],boardCpy[pos]
		moves.append(boardCpy)
	return moves

if __name__ == "__main__":
	queue = [current]
	visited =[]
	while queue:
		current = queue.pop(-1)
		if current not in visited:
			dispBoard(current)
			visited.append(current)
			if current == sol:
				print('solution found')
				break
			else:
				moves = getMoves(current)
				for move in moves:
					if move not in visited:
						queue.append(move)
		else:
			print("Repeated state, skipping")
		print(' '*10+str(len(visited)))