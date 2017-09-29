
## Linear Equations using the Echelon or Gauss-Jordan Methods
Version/Date: Sept 26, 2017

### Exercise
>PREDICT_400-DL_SEC56
>Wk2 Module

### File(s)
Wk2LinearEq.ipynb

### Instructions
Present a system of equations that you have come across professionally (or personally, if that is not an option) that contains three or more linear equations. and three or more variables. Create one if you have to, but be sure to describe the scenario. Follow up by solving your set of equations using both the Echelon and Gauss-Jordan methods. Which method do you prefer? Why?




```python
!pwd
```

    /mnt/c/Users/andrewknight/Dev/MSPA-PREDICT400/Wk2



```python
!python3 --version
```

    Python 3.5.2



```python
%%markdown
This business example looks a costs for manufacturing three different product models. Comparing revenue and manufacturing 
costs for each, setup a system of linear equations with three variables. 
Per unit costs (in USD) for producing three different models options (one,two,three) number of units defined by x, y, z.
Total manufacturing targets for each are listed in the total column.

I have tried different variations on this scenario, trying different values to test the output. I tested scenarios involving 
cost, revenue, build times and other variables. The numbers have been adjusted for this example. 

Testing both the Echelon method and Gaussian-Jordan method by hand, I verified the output using linalg.solve in code below.
TODO: I have not yet normalized the values to be non-negative. I believe scipy can be used for this but not complete.

This primary question to answer is... **How many of each model should we build to hit the desired total targets? **

| Models       | one   | two   | three | Total  |
| ------------ | ------| ------| ------| -------|
| Number       | x     | y     | z     | 500    |
| Revenue      | 120   | 160   | 200   | 87000  |
| Cost         | 18    | 20    | 25    | 11000  |
```


This business example looks a costs for manufacturing three different product models. Comparing revenue and manufacturing 
costs for each, setup a system of linear equations with three variables. 
Per unit costs (in USD) for producing three different models options (one,two,three) number of units defined by x, y, z.
Total manufacturing targets for each are listed in the total column.

I have tried different variations on this scenario, trying different values to test the output. I tested scenarios involving 
cost, revenue, build times and other variables. The numbers have been adjusted for this example. 

Testing both the Echelon method and Gaussian-Jordan method by hand, I verified the output using linalg.solve in code below.
TODO: I have not yet normalized the values to be non-negative. I believe scipy can be used for this but not complete.

This primary question to answer is... **How many of each model should we build to hit the desired total targets? **

| Models       | one   | two   | three | Total  |
| ------------ | ------| ------| ------| -------|
| Number       | x     | y     | z     | 500    |
| Revenue      | 120   | 160   | 200   | 87000  |
| Cost         | 18    | 20    | 25    | 11000  |



```python
import numpy as np
```


```python
# Use the following system of equations
# ax + by + cz = 500
# dx - ey + fz = 87000
# gx + hy - iz = 11000

#Three product models one, two, three
count_one = 1
count_two = 1
count_three = 1
rev_one = 120
rev_two = 160
rev_three = 200
cost_one = 18
cost_two = 20
cost_three = 25

count_total = 500
rev_total = 87000
cost_total = 11000

# Find the solution using np
A = np.array([[count_one,count_two,count_three],[rev_one,rev_two,rev_three],[cost_one,cost_two,cost_three]])
print('\nA matrix:\n' + str(A))

B = np.array([[count_total],[rev_total],[cost_total]]) #soln values as a col vector
print('\nB matrix:\n' + str(B))
    
try:
    Xsolve = np.rint(np.linalg.solve(A,B)) #Alt way to solve using np.linalg.solve
    print('\nXsolve = np.linalg.solveA,B\nXsolve matrix:\n' + str(Xsolve))
except LinAlgError:
    X = np.linalg.lstsq(A,B)[0]
    print('\nX = np.linalg.solveA,B\nX matrix:\n' + str(X))
```

    
    A matrix:
    [[  1   1   1]
     [120 160 200]
     [ 18  20  25]]
    
    B matrix:
    [[  500]
     [87000]
     [11000]]
    
    Xsolve = np.linalg.solveA,B
    Xsolve matrix:
    [[  42.]
     [ 242.]
     [ 217.]]



```python
# Note: see handwritten solutions attached.
# After working through the equations using Echelon and Gauss-Jordan for this example, 
# I prefer the matrix manipulation of the Gauss-Jordan method over the Echelon for systems of equations
# consisting of three variables. Echelon is my preference for systems involving only two variables as it only 
# requires two transformations.
```


```python
%%HTML
<iframe height="400px" width="100%" src="https://github.com/knightman/MSPA-PREDICT400/blob/master/Wk2/SolutionNotes.jpg"></iframe>
```


<iframe height="400px" width="100%" src="https://github.com/knightman/MSPA-PREDICT400/blob/master/Wk2/SolutionNotes.jpg"></iframe>

