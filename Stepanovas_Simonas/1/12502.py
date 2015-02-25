class Family:
	def __init__(self, name, hoursWorked):
		self.name = name;
		self.hours = hoursWorked;
		self.money = 0;
	
	def hoursOverworked(self, hoursEach):
		self.hoursOver = self.hours - hoursEach;
		

def readFile(file):
	f = open(file);
	array = []
	n = int(f.readline());
	for line in f: # read rest of lines
		array.append([int(x) for x in line.split()])
	return n, array

def hoursForEachFamily(x, y):
	return (x + y) / 3;

	
def computeMoney(hoursOver, hEach, z):
	moneyA = hoursOver / hEach * z;
	return moneyA;
	
n, array = readFile('data2.txt');

families = [];

for i in range(0, n):
	moneyC = array[i][2];
	families.append([Family('A', array[i][0]), Family('A', array[i][1])]);	
	hEach = hoursForEachFamily(families[i][0].hours, families[i][1].hours);
	for j in range(0, 2):
		hoursOver = families[i][j].hoursOverworked(hEach);
		families[i][j].money = computeMoney(families[i][j].hoursOver, hEach, moneyC);
	for j in range(0, 2):
		print("A family worked %d hours more and earned $%d" %(families[i][j].hoursOver, families[i][j].money))
	print();

