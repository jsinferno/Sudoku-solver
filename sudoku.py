from random import shuffle, randint

numbers = [str(num) for num in range(1,10)]


def create_grid(grid):
	return [[x for x in grid[i:i+9]] for i in range(0,81,9)]


def solve(oldgrid):
	grid = create_grid([x for y in oldgrid for x in y])

	for cycle in range(5):

		for along in range(9):
			grid[along] = check_line(grid[along])



		for across in range(9):
			down = [mylist[across] for mylist in grid]
			down = check_line(down)
			

			for x in range(9):
				grid[x][across] = down[x]


		for line in range(0,9,3):
			for part in range(0,9,3):
				check = grid[line][part:part+3]+grid[line+1][part:part+3]+grid[line+2][part:part+3]
				check = check_line(check)
				total = 0
				for i in range(line,line+3):
					for g in range(part,part+3):
						grid[i][g] = check[total]
						total+=1


	if find_next_empty(grid)[0] == None: return [grid,True]
	return [oldgrid,False]



def check_line(line):

	for i,num in enumerate(line):
		new = []
		if num == "0" or type(num) == list:
			for number in numbers:
				if number not in line:
					new.append(number)
			if type(num) == list:
				new = [x for x in new if x in num]
			if len(new) == 1: 
				line[i] = new[0]
			else: line[i] = new
	return only_list(line)



def only_list(line):
	new_line = [num for alist in [lst for lst in line if type(lst) == list] for num in alist]

	stop = []
	for num in new_line:
		if num not in stop and new_line.count(num) and num not in line == 1:
			for i,alist in enumerate(line):
				if type(alist) == list and num in alist:
					line[i] = num
		else: stop.append(num)
	return line


def print_grid(grid):
	for i,x in enumerate(grid):
			print(["0" if type(y) == list or y == "0" else y for y in x[0:3]],["0" if type(y) == list or y == "0" else y for y in x[3:6]],["0" if type(y) == list or y == "0" else y for y in x[6:9]])
			if i%3==2: print("")



def is_valid(row,col,guess,oldgrid):
	grid = create_grid([x if type(x) != list else x[0] for y in oldgrid for x in y])

	up,wide = (row//3)*3,(col//3)*3	
	all_numbers = [mylist[col] for mylist in grid] + grid[row] + grid[up][wide:wide+3]+grid[up+1][wide:wide+3]+grid[up+2][wide:wide+3]
	if guess in all_numbers:
		return False
	return True


	
def find_next_empty(grid):
	for r in range(9):
		for c in range(9):
			if grid[r][c] == "0" or grid[r][c] == " " or type(grid[r][c]) == list : return [r,c]
	return [None,None]


def valid_grid(oldgrid):
	grid = create_grid([x for y in oldgrid for x in y])


	for row,line in enumerate(grid):
		for col,num in enumerate(line):
			grid[row][col] = "0"

			if num!="0" and not is_valid(row, col, num, grid):
				return False
			grid[row][col] = num
	else: return True

				
	


def make_grid(oldgrid = create_grid(["0"] *81)):
	grid = create_grid([x for y in oldgrid for x in y])

	row,col = find_next_empty(grid)
	if row == None: return [grid,True]

		
	shuffle(numbers)
	for guess in numbers:
		if is_valid(row,col,guess,grid):
			grid[row][col] = guess
		

			n = make_grid(grid)
			if n[1]:
				return n



	else: 
		grid[row][col] = "0"
		return [grid,False]
	
	



					


def take_away(oldgrid):
	grid = create_grid([x for y in oldgrid for x in y])
	
	x,y = randint(0,8),randint(0,8)
	while grid[x][y] == "0":
		x,y = randint(0, 8), randint(0, 8)
	fill_in = grid[x][y] 

	grid[x][y] = "0"

	if solve(grid)[1]:
		return take_away(grid)
	else:
		grid[x][y] = fill_in
		return grid

	
	




  




if __name__ == "__main__":

	g = [['1', '2', '3', '4', '5', '6', '0', '0', '0'], ['4', '5', '6', '7', '8', '9', '0', '0', '0'], ['7', '8', '9', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0']]
	print_grid(g)

	print(valid_grid(g))
	
	
	
	# answer,creation = [],[]
	# grid = ["0"] *81


	
	# grid = create_grid(grid)


	# print(answer)
	# flatten = [column for rows in answer for column in rows]
	# creation = create_grid(flatten)
	# print("Beginner: 1, Intermediate: 2, Hard: 3")
	# amount = input()
	# for cycle in range(70):
	# 	take_away(creation)

	# print_grid(creation)
	# print("--------------------------------")
	# print_grid(answer)


	



	# for r in range(9):
	# 	for c in range(9):
	# 		if creation[r][c] == "0":
	# 			creation[r][c] = " "
				
	# drawGrid(creation)

	













# def text(message,x,y,size):
#     FONT = ('Arial', size, 'normal')
#     myPen.penup()
#     myPen.goto(x,y)    		  
#     myPen.write(message,align="left",font=FONT)

# #A procedure to draw the grid on screen using Python Turtle
# def drawGrid(grid):
#   intDim=35
#   for row in range(0,10):
#     if (row%3)==0:
#       myPen.pensize(3)
#     else:
#       myPen.pensize(1)
#     myPen.penup()
#     myPen.goto(topLeft_x,topLeft_y-row*intDim)
#     myPen.pendown()
#     myPen.goto(topLeft_x+9*intDim,topLeft_y-row*intDim)
#   for col in range(0,10):
#     if (col%3)==0:
#       myPen.pensize(3)
#     else:
#       myPen.pensize(1)    
#     myPen.penup()
#     myPen.goto(topLeft_x+col*intDim,topLeft_y)
#     myPen.pendown()
#     myPen.goto(topLeft_x+col*intDim,topLeft_y-9*intDim)

#   for row in range (0,9):
#       for col in range (0,9):
#         if grid[row][col]!=0:
#           text(grid[row][col],topLeft_x+col*intDim+9,topLeft_y-row*intDim-intDim+8,18)




# if __name__ == "__main__":
# 	import turtle
# 	myPen = turtle.Turtle()
# 	myPen._tracer(0)
# 	myPen.speed(0)
# 	myPen.color("#000000")
# 	myPen.hideturtle()
# 	topLeft_x=-150
# 	topLeft_y=150
# 	turtle.done()