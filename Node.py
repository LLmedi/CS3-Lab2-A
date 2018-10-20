class Node(object):
	item = -1
	next = None
	
	def __init__(self, item = None, next = None):
		self.item = item
		self.next = next
		
	def add(self, newItem):
		temp = self
		while temp.next != None:
			temp = temp.next
		temp.next = Node(newItem)
		
	#def delete(self):
		
	def printAll(self):
		temp = self
		while temp.next != None:
			print(temp.item)
			temp = temp.next