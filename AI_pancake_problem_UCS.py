
 ##Created by : Priyanka Pradhan
 ##pancake sort problem by uniformed cost search algo

import heapq ##for heap queue algorithm aka priority queue algorithm
from random import randint ##for generation of randomarray


### creating a random array list 
def PCstack(i):
	stack = []
	 ##iterates over all possible values from 1 to i-1
	while len(stack)!= i: 
		k = randint(1, i)   ##generates random integers between 1 and i 
		## if the value of 'K' is not present in the stack it adds the integer at the end of the stack
		if not k in stack:    
			stack.append(k)	
	return stack  ##returns the list 


##calculate the cost of moving backwards in a stack
def backwardCost(stack):
	## initialize the distance 
	distance = 0
	bkcost = []

	##calculates the difference between that element's position and its predecessor's position
	for i in range(0, len(stack) - 1):
		distance = abs((stack[i] - stack[i + 1]) )
		bkcost.append(distance)
	return bkcost


def totalCost(stack):
	
	tc = [i  for i in (backwardCost(stack))]
	##
	totalcostSum = sum(tc)
	return totalcostSum


##create a new node of stack to store end list & total cost
def createNode(stack):
	tc = totalCost(stack)
	node = (tc, stack)  ##node is a tuple of totalcost (f + b) along with the list of elements in stack --one is int and other []

	return node 

##recursive function to check if the node is present in the heap
def Exists(heap, node):
	for k in range(0, len(heap)):
		if node[1] == heap[k][1]:
			return k, heap[k][0]
		# if no nodes found return -1
	return -1, -1


def pancakeSort(initialStack, numPancakes):
	## we need the pancake in descending order i.e from 10 to 1 , thus reverse is used to achieve this
	solution = sorted(list(range(1, numPancakes + 1)), key=int, reverse=True) 
	print( '\n the final goal state is :',solution , '\n The following flips has been done to achieve the goal state :- \n')
	flip = 0

	##create a list which will be used as an initial stack and then use heapq.heappush() function to push it onto a priority queue.
	PriorityQueue = []
	visited = []
	heapq.heappush(PriorityQueue, createNode(initialStack))
	heapq.heappush(visited, createNode(initialStack))
	
	while True:
		if len(PriorityQueue) == 0:
			break 	
		node = heapq.heappop(PriorityQueue)
		
		if node[1] == solution:
			break
		for i in range(2, (numPancakes + 1)):
			nodex = createNode(flipPancakes(list.copy(node[1]), i, numPancakes))

			##Exists() function to check if the current node exists on either the priority queue or visited list
			k, tc = Exists(PriorityQueue, nodex)
			p, tc2 = Exists(visited, nodex)
			if tc < 0 and tc2 < 0: 
				heapq.heappush(PriorityQueue, tuple(nodex))
				heapq.heappush(visited, tuple(nodex))
			elif tc > nodex[0]: 
				pqlst = list(tuple(PriorityQueue[k]))
				pqlst[0] = nodex[0]
				PriorityQueue[k] = tuple(pqlst)
		flip += 1
		print('\n Below , each tuple provides the information of Total cost followed by the list of pancakes \n Starting flip -->' , flip , '\n')  #"\nnodes in heap after %d flips:" % 
		##print( '\n the final goal state is :',solution )
		for k in range(0, len(PriorityQueue)):
			print(PriorityQueue[k], end='\n')
			#print(solution)
	return flip
        


# given a list representing a pancake stack, and two ints,reverse stack[i...(numPancakes - 1)]

def flipPancakes(stack, i, numPancakes):
	k = numPancakes - 1
	p = i
	index = abs(numPancakes - i)
	##a temporary integer list that collects the ints to be flipped and puts them in reverse order 
	temp = 0
	while p // 2 != 0:
		temp = stack[index]
		stack[index] = stack[k]
		stack[k] = temp
		
		index += 1
		## swap this element with another element at position k-1 on our new list (the old list)
		k -= 1
		p = (p + 1) / 2
	
	return stack

##given an int representing the number of pancakes in a stack, return a randomly generated stack


def main():
	flip = 0
	numRuns = 1
	###user input
	numPancakes=int(input('Kindly enter the number(integer) of pancakes you need in your stack : '))
	
		
	for i in range(0, numRuns):
				initialStack = PCstack(numPancakes)
				print('generating random pancake stack:', initialStack, '\n')
				flip += pancakeSort(initialStack, len(initialStack))
			
				
				print('\n\n total number of flips for getting the desired pancake stack' , (flip / numRuns) , '\n')

import time




if __name__ == '__main__':
	start_time = time.time()
	main()
print('execution time for uniform cost search : %s seconds' % (time.time() - start_time))
