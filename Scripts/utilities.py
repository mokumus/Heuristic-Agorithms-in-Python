import math, random
from copy import deepcopy
from timeit import default_timer as timer
from datetime import timedelta

test1 = [[0, 90], [0, 16], [0, 30]]
test2 = [[0, 20], [0, 19], [0, 4], [0, 20]]
test3 = [[0, 37.12], [0, 10.60], [0, 2], [0, 31.26]]
test4 = [[0, 50], [0, 2], [0, 30], [0, 5], [0, 5], [0, 120], [0, 5]]
test5 = [[0, 50], [0, 2], [0, 30], [0, 5], [0, 5], [0, 120], [0, 5]]
test6 = [[0, 16], [0, 128], [0, 16], [0, 4], [0, 2], [0, 2], [0, 2], [0, 128]]
test7 = [[0, 90], [0, 16], [0, 30], [0, 20], [0, 44], [0, 4], [0, 4], [0, 16]]
test8 = [[0, 16], [0, 128], [0, 16], [0, 16], [0, 4], [0, 2], [0, 2], [0, 2], [0, 100], [0, 128]]
test9 = [[0, 2], [0, 2], [0, 30], [0, 2], [0, 16], [0, 2], [0, 2], [0, 23], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 60]]
test10 = [[0, 2], [0, 2], [0, 2], [0, 16], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 120]]

tests = [test1, test2, test3, test4, test5, test6, test7, test8, test9, test10]

def constructRandomTest(size):
	constructedTest = []
	for i in range(0, size):
		tmp = [0, random.randint(0, 100)]
		constructedTest.append(tmp)
	return constructedTest

randomTests = []
randomTests.append(constructRandomTest(50))
randomTests.append(constructRandomTest(100))
randomTests.append(constructRandomTest(250))


def draw(positions):
	t = turtleCircles.MyTurtle(900,400)
	t.drawCircles(positions)
	t.getscreen()._root.mainloop()

def chronometer(foo, arg):
	start = timer()
	output = foo(arg)
	output = writeOffsets(output)
	end = timer()
	elapsedTime = timedelta(seconds=end - start)
	print("=" * 40)
	print("Method: {}".format(foo.__name__.capitalize()))
	print("input:  {}".format(formatPairedList(arg)))
	print("output: {}".format(formatPairedList(output)))
	print("cost:   {}".format(cost(output)))
	print("Elapsed time: {}".format(elapsedTime))
	print("="*40)
	timeStr = "{}".format(elapsedTime)
	return elapsedTime.total_seconds()

def endlog():
	end = time()
	elapsed = end-start
	log("End Program", secondsToStr(elapsed))

def calculateTangent(r1, r2):
	return math.sqrt(4 * r1 * r2)

def clearOffsets(p):
	for i in p:
		i[0] = 0
	return p

def calculateOffsets(k):
	p = deepcopy(k)
	clearOffsets(p)
	for x in range(0, len(p)):
		if x == 0:
			p[x][0] = 0

		elif p[x-1][1] >= p[x][1]:
			p[x][0] = calculateTangent(p[x-1][1],p[x][1]) + p[x-1][0]

		else:
			closeOffset = calculateTangent(p[x-1][1],p[x][1]) + p[x-1][0]
			flagUp = True
			temp = 0
			for j in reversed(range(x)):
				if calculateTangent(p[j][1], p[x][1]) +  p[j][0] > closeOffset:
					temp = calculateTangent(p[j][1], p[x][1]) + p[j][0]
					p[x][0] = max(calculateTangent(p[j][1], p[x][1]) + p[j][0],p[x][0])
					flagUp = False

			if(flagUp):
				p[x][0] = max(temp,closeOffset)
	return p

def writeOffsets(p):
	return calculateOffsets(p)

def formatPairedList(l):
	str = "["
	for i in l:
		str += "[{:.1f}, {:.1f}], ".format(i[0],i[1])
	str = str[:-2]
	str += "]"
	return str

"""
Cost function for calculated offsets
"""
def cost(circles):
	distance = calculateOffsets(circles)
	biggestOffset = circles[-1][0] + circles[-1][1]

	for p in circles[:-1]:
		if p[0] + p[1] > biggestOffset:
			biggestOffset = p[0] + p[1]
	return biggestOffset

def randomPermutaion(circles):
	perm = deepcopy(circles)
	for pair in circles:
		ri1 = random.randint(0, len(circles) - 1)
		ri2 = random.randint(0, len(circles) - 1)
		perm[ri1], perm[ri2] = perm[ri2], perm[ri1]
	return perm

def reduceToRadius(p):
	radiuses = []
	for pair in p:
		radiuses.append(pair[1])
	return radiuses





