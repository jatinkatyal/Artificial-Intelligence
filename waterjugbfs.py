def getMoves(v1,v2,v1Cap,v2Cap):
	moves=[]
	if v1<v1Cap:
		moves.append([v1Cap,v2,'Fill Vessel 1'])
		if v2 > 0:
			if v1+v2<=v1Cap:
				a= v1 + v2
				b=0
			else:
				a=v1Cap
				b=v2-(v1Cap-v1)
			moves.append([a, b, 'Pour in 1 from 2'])

	if v2 < v2Cap:
		moves.append([v1,v2Cap,'Fill Vessel 2'])
		if v1 > 0:
			if v1+v2<=v2Cap:
				a = 0
				b = v1 + v2
			else:
				a=v1 - (v2Cap-v2)
				b=v2Cap
			moves.append([a, b, 'Pour in 2 from 1'])

	return moves


if __name__ == "__main__":
	v1Cap = int(input("Vessel 1 cap?: "))
	v2Cap =  int(input("Vessel 2 cap?: "))
	sol = int(input("required?:"))
	root = [0,0]
	visited = []
	queue = [root]
	while queue:
		current = queue.pop(0)
		if current not in visited:
			visited.append(current)
			v1,v2 = current
			if sol==v1 or sol==v2:
				print("Solution found")
				break
			else:
				moves = getMoves(v1,v2,v1Cap,v2Cap)
				for move in moves:
					v1,v2,msg = move
					if [v1,v2] not in visited:
						queue.append([v1,v2])
			print(' '*10+str(len(visited)))

				