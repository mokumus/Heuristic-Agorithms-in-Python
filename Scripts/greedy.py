import utilities

def greedy(p):
	greedyList = []
	radiuses = []
	for pair in p:
		radiuses.append(pair[1])

	size = len(radiuses)
	while len(radiuses) > 0:
		if len(radiuses) > 0:
			greedyList.append([0, (max(radiuses))])
			radiuses.remove(max(radiuses))
		if len(radiuses) > 0:
			greedyList.append([0, (min(radiuses))])
			radiuses.remove(min(radiuses))
		if len(radiuses) > 0:
			greedyList.append([0, (min(radiuses))])
			radiuses.remove(min(radiuses))
	return greedyList

if __name__ == "__main__":
	for i, test in enumerate(utilities.tests):
		print("#Test{}".format(i+1))
		time = utilities.chronometer(greedy, test)




