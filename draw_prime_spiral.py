from graphics import *
import time

X_SIZE = 1040
Y_SIZE = 1040

PRIMES = set()
with open("primes.txt", "r") as prime_file:
	for line in prime_file.readlines():
		prime_nums = line.split(',')
		for num in prime_nums:
			if num.isnumeric():
				PRIMES.add(int(num))

def main():
	win = GraphWin("Spiral", X_SIZE, Y_SIZE)
	x_default = X_SIZE/2
	y_default = Y_SIZE/2
	small_max = 270379
	direct = "u"
	path_len = 2
	cur_path = path_len
	steps = 1
	points = []
	pt = Point(x_default, y_default, steps)
	pt.draw(win)
	pt.setFill("red")

	path = [x_default, y_default]
	for i in range(0, small_max):
		if cur_path > 0:
			if direct == "u":
				path[0] -= 2
				cur_path -= 2
				steps += 1
				if steps in PRIMES:
					pt = Point(path[0], path[1], steps)
					pt.draw(win)
					points.append(pt)
			elif direct == "l":
				path[1] -= 2
				cur_path -= 2
				steps += 1
				if steps in PRIMES:
					pt = Point(path[0], path[1], steps)
					pt.draw(win)
					points.append(pt)
			elif direct == "d":
				path[0] += 2
				cur_path -= 2
				steps += 1
				if steps in PRIMES:
					pt = Point(path[0], path[1], steps)
					pt.draw(win)
					points.append(pt)
			elif direct == "r":
				path[1] += 2
				cur_path -= 2
				steps += 1
				if steps in PRIMES:
					pt = Point(path[0], path[1], steps)
					pt.draw(win)
					points.append(pt)
		elif direct == "l" or direct == "r":
			path_len += 2
			cur_path = path_len
			if direct == "l":
				direct = "d"
			else:
				direct = "u"
		elif direct == "u" or direct == "d":
			cur_path = path_len
			if direct == "u":
				direct = "l"
			else:
				direct = "r"
	print("done")
	drawn = False
	t = Text(Point(-1, -1, -1),"")
	while True:
		click = win.getMouse()
		if not drawn:
			for p in points:
				if click.getX() == p.getX() and click.getY() == p.getY()\
						or click.getX() == p.getX()-1 and click.getY() == p.getY()\
						or click.getX() == p.getX()+1 and click.getY() == p.getY()\
						or click.getX() == p.getX() and click.getY() == p.getY()-1\
						or click.getX() == p.getX() and click.getY() == p.getY()+1\
						or click.getX() == p.getX()-1 and click.getY() == p.getY()-1\
						or click.getX() == p.getX()-1 and click.getY() == p.getY()+1\
						or click.getX() == p.getX()+1 and click.getY() == p.getY()-1\
						or click.getX() == p.getX()+1 and click.getY() == p.getY()+1:
					t = Text(p,p.getNum())
					t.draw(win)
					drawn = True
		else:
			t.undraw()
			drawn = False

if __name__ == "__main__":
	main()
