class Data:
	def __init__(self, mo, dy, yr):
		self.month = mo
		self.day = dy
		self.year = yr

	def __repr__(self):
		r = "month: %02d\nday: %02d\nyear: %02d" %(self.month, self.day, self.year)
		return r

	def __str__(self):
		s = "%02d/%02d/%04d" %(self.month, self.day, self.year)
		return s

	def isLeapYear(self):
		if self.year % 400 == 0:
			return True
		if self.year % 100 == 0:
			return False
		if self.year % 4 == 0:
			return True
		return False

	def addDay(self):
		DIM = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		if self.isLeapYear():
			DIM[2] = 29
		else:
			DIM[2]= 28
		if self.day == DIM[self.month]:
			self.month += 1
			self.day = 1
			if self.month == 13 and self.day == 1:
				self.month = 1
				self.year += 1
		else:
			self.day += 1

	def addNDays(self, n):
		for i in range(n):
			self.addDay()

def main():
	d = Data(1,1,2000)
	print(repr(d))
	print(d.isLeapYear())
	d.addNDays(-1)
	print(d)

if __name__ == '__main__':
	main()






