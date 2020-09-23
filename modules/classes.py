import os
class Contact:

	def __init__(self, n, t, c):
		self.name = n
		self.phone = t	
		self.num = c



	def getContact(self):
		arr = [self.name, self.phone]
		return arr

	



class App:
	def __init__(self):
		self.contacts = []
		self.count = 0
	
	def InsertContact(self, n, t):
		a = Contact(n, t, self.count)
		self.count += 1
		self.contacts.append(a)

	def getElements(self):
		return self.contacts

	def PrintElements(self):
		os.system('cls')
		for i in self.contacts:
			print(i.name)
	def NameForPosition(self, pos):
		return [self.contacts[pos].name,self.contacts[pos].phone, self.contacts[pos].num]

	


	def Delete(self, ref):
		self.count -= 1
		print(ref-1)
		self.contacts.pop(ref)			

