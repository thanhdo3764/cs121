contacts =  dict()

contacts['Thanh'] = 'thanh.d.do@wsu.edu'
contacts['John Smith'] = 'john.smith@gmail.com'
print(contacts)

print(contacts.keys())

class Counter:

	def __init__(self):
		self.items = dict()

	def add(self, itemType):
		if(itemType not in self.items.keys()):
			self.items[itemType] = 1
		else:
			self.items[itemType] += 1

	def getCount(self, itemType):
		return self.items.get(itemType, 0)

mycounter = Counter()
mycounter.add('ItemA')
mycounter.add('ItemB')
mycounter.add('ItemA')
print(mycounter.getCount('ItemA'))
print(mycounter.getCount('ItemC'))

car = {'brand': 'Ford', 'model': 'mustang', 'year': 1984}

fleet = dict()
fleet['sally'] = car

print(fleet)























