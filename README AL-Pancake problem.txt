README FILE - 
created by : Priyanka Pradhan

version - Python 3.9

THE PANCAKE PROBLEM
A messy cook has a disordered stack of 10 differently sized pancakes [size from 1 to 10] and a spatula that can 
be inserted at any point in the stack and used to flip all pancakes above it. The goal is for the cook to have them 
in the “correct” order for the customer, that is, the large on the bottom up to the smallest on top ([10, 9, 8, 7, 
6, 5, 4, 3, 2, 1]):
1. Define the problem as a searching problem.
2. Define a possible cost function (backward cost).
3. Define a possible heuristic function (forward cost).
4. Implement an A* algorithm in Python.
5. Could the Uniform-Cost-Search algorithm be used? 
If so, provide also an implementation of the same Pancake Problem with UCS



Run the python files (seperately) -
1 - User input will be asked for 'entering the integer number of pancakes they want'
2 - code will generate a random array of numbers ( for eg- if you wanted 5 pancakes it would create a list like [ 2,4,3,1,5 ] 
3 - It will display the final outcome here ( [5,4,3,2,1 ] and then the following flips would be shown below
4 - The searching and flipping function would start 
5 - each tuple will display the total cost for that flip , along with the list of pancake in current state 
6- the last flip will display no tuple that means it has already sorted the pancakes to the desired stack.


Assumptions for A*: 
--> Pancake sorting is defined as a A* searching problem with possible backward and heuristic cost function , the initial pancake stack is disoriented
and the code should stack the pancakes in correct order i.e the large on the bottom up to the smallest on top e.g - ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
--> each node is taken as a tuple of total cost and the current order of pancakes
--> total cost is defined as the sum of backward and forward (heuristic cost)
--> backward cost would be sum of distances between size of pancakes 
--> forward cost be if the distance between 2 sizes are greater than 1 and cost is also 1 , if the distance is less than 1 then cost would be 0
--> the code generates random pancake stacks of different sizes and flip through the end untill it attains the correct order of the stack.

Assumptions for UCS :
--> Pancake sorting is defined as a uniformed cost searching problem , the only cost will be the cost itself (just backward)
and the code should stack the pancakes in correct order i.e the large on the bottom up to the smallest on top e.g - ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
--> each node is taken as a tuple of total cost and the current order of pancakes
--> the code generates random pancake stacks of different sizes and flip through the end untill it attains the correct order of the stack.


Conclusion - UCS search takes more time to execute than A* search for same disordered stack.


references -
https://courses.cs.washington.edu/courses/cse573/20wi/slides/3-InformedSearch-annotated.pdf
https://www.geeksforgeeks.org/a-pancake-sorting-question/
https://helloacm.com/introducing-the-pancake-sorting-algorithm/