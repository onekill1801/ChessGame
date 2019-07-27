def solution_sudoku(problem):
	sudoku(problem,0,0);
	

def sudoku(problem,x,y):
	if x == 8:
		if y == 9:
			print(problem)
		else:
			if problem[x][y] == 0:
				for i in range(1,10):
					if check_area(problem,x,y,i):
						problem[x][y] = i
						sudoku(problem,x,y+1)
					problem[x][y] = 0
			else:
				sudoku(problem,x,y+1)
	else:
		if y == 8:
			if problem[x][y] == 0:
				for i in range(1,10):
					if check_area(problem,x,y,i):
						problem[x][y] = i
						sudoku(problem,x+1,0)	
					problem[x][y] = 0
			else:
				sudoku(problem,x+1,0)
		else: 
			if problem[x][y] == 0:
				for i in range(1,10):
					if check_area(problem,x,y,i):
						problem[x][y] = i
						sudoku(problem,x,y+1)
					problem[x][y] = 0
			else:
				sudoku(problem,x,y+1)

def test(problem):
	for x in range(1,10):
		if check_area(problem,0,1,x):
			print(x)

def check_area(problem,x,y,i):
	for index in range(0,9):
		if problem[x][index] == i:
			return 0
		if problem[index][y] == i:
			return 0
	for xx in range(x//3*3,x//3*3+3):
		for yy in range(y//3*3,y//3*3+3):
			if problem[xx][yy] == i:
				return 0
	return 1


if __name__ == '__main__':
	problem =  [[0,0,0,0,0,0,8,0,5],
				[0,0,0,0,0,5,0,6,0],
				[0,0,9,0,0,8,2,0,7],
				[4,0,0,9,2,0,0,0,1],
				[8,0,0,0,7,0,0,0,4],
				[3,0,0,0,1,4,0,0,6],
				[6,0,4,7,0,0,9,0,0],
				[0,8,0,4,0,0,0,0,0],
				[5,0,1,0,0,0,0,0,0]]
	solution_sudoku(problem)
	# test(problem)
	# print(problem)