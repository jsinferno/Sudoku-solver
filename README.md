# Sudoku-solver
interactive sudoku web app, solver and creator

From the start I set up my solver as a logical one (which you can see from some unused code I left in) rather than a brute force one. many complications arouse from this. firstly I didn't realise the number of tactics that can be used in sudoku (and still don't) which meant my solver was worse than a decently competent person.

Therefore I swapped to a recursive brute force approach and as I struggled with recursion I made it a lot harder than it needed to be. However this too came with complications as now i had no way of creating a grid as i myself could not know if it was solvable by a human. 

Therefore the messy solution in this repositry or more specifically sudoku.py is to use brute force for solving and then my limited logical solver for creating a grid leading to very easy grids being created.
