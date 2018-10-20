from Node import Node
import LinkedList

def main():
	
	#Open files
	activision = open("activision.txt", "r")
	vivendi = open("vivendi.txt", "r")
	
	head = Node()
	total = 0;
	#Read lines and create LL
	if activision.mode == "r":
		f1 = activision.readlines()
		
		for x in f1:
			head.add(int(x))
	
	if vivendi.mode == "r":
		f2 = vivendi.readlines()
		for x in f2:
			head.add(int(x))
			
	head = head.next
	
	'''''''''''''''''''''''''''
	Each solution returns a set to make it easier to compare
	the results to one another.
	To check a solution, uncomment the method call below and
	replace the appropriate variables inside the print statement
	'''''''''''''''''''''''''''
	
	
	#Solutions
	#set1 = nestedLoops(head)
	#set2 = bubbleSort(head)
	#set3 = nestedLoops(mergeSort(head))
	#set4 = boolList(head)
	
	#print(set# == set#)

	
def boolList(head):
	temp = head
	seen = [None]*6001
	seenSet = set()
	while temp != None:
		if seen[int(temp.item)] == None:
			seen[int(temp.item)] = False
		elif seen[int(temp.item)] == False:
			seen[int(temp.item)] = True
		temp = temp.next
	for (i, item) in enumerate(seen, start = 0):
		if item is True:
			seenSet.add(i)
	return seenSet

def mergeSort(head):
	if head == None or head.next == None:
		return head
	
	middle = getMiddle(head)
	secondHalf = middle.next
	middle.next = None
	
	return merge(mergeSort(head), mergeSort(secondHalf))

def merge(firstHalf, secondHalf):
	temp = Node()
	curr = temp
	while firstHalf != None and secondHalf != None:
		if firstHalf.item <= secondHalf.item:
			curr.next = firstHalf
			firstHalf = firstHalf.next
		else:
			curr.next = secondHalf
			secondHalf = secondHalf.next
		curr = curr.next
	curr.next = secondHalf if firstHalf == None else firstHalf
	return temp.next
	
def getMiddle(head):
	if head == None:
		return head
	slow = head
	fast = head
	
	while fast.next != None and fast.next.next != None:
		slow = slow.next
		fast = fast.next.next
	return slow
	
def bubbleSort(head):
	first = head
	second = head.next
	swapped = True
	seen = set()
	
	while first.next != None and swapped:
		swapped = False
		
		while second != None:
			if first.item > second.item:
				temp = first.item
				first.item = second.item
				second.item = temp
				swapped = True
			
			if first.item == second.item:
				seen.add(int(first.item))
			second = second.next
			first = first.next
		first = head
		second = head.next
	return seen
	
def nestedLoops(head):
	temp1 = head
	temp2 = head.next
	seen = set()
	while temp1.next != None: #item being checked
		while temp2 != None: #compated to
			if temp1.item == temp2.item: #if item repeats
				seen.add(int(temp1.item))
				break
			else:
				temp2 = temp2.next
	
		temp1 = temp1.next
		temp2 = temp1.next
	return seen


main()