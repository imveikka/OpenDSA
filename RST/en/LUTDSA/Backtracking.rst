.. avmetadata::
   :author: Tuomas Eerola & Veikka Immonen
   :topic: Backtracking


Backtracking, and Branch and Bound
==================================

Backtracking
------------

Backtracking is a method, which allows us to systematically visit 
all possible combinations (solutions). It is a "brute-force" algorithm, 
whose implementation is typically straightforward. The method is 
useful when the number of combinations is so small that we have time 
to go through them all. In this chapter, we will first familiarize 
ourselves with the backtracking algorithms, which go through combinations 
of numbers. After this, we will see how you can use the backtracking in 
two problems and how to make the search for optimal solution more 
efficient.

From loops to recursion
-----------------------

Suppose we want to go through all combinations of 𝑛 numbers, where 
each number is an integer between :math:`1...m`. There are a total 
of :math:`m^n` such combinations (there are :math:`n` points and in each 
point the number can be chosen in :math:`m` ways). For example, 
if :math:`n=3` and :math:`m=4`, the combinations 
are :math:`[1,1,1], [1,1,2], [1,1,3], [1,1,4], [1,2,1], 
[1,2,2], [1,2,3], [1,2,4]`, etc.

If the value of :math:`n` is known in advance, we can create 
:math:`n` nested loops, each of which goes through :math:`m` 
numbers. For example, the following code loops through all 
combinations in case :math:`n=3`:math:`n=3`

.. codeinclude:: Design/combLoops

This is a good solution in itself, but there is one problem: 
the value of :math:`n` affects on the number of loops. If we 
wanted to change the value of :math:`n`, we would have to change 
the amount of loops in the code, which is not practicable. However, 
we can implement a solution recursively using backtracking so that 
the same code works for all values of :math:`n`.

Implementing the search
-----------------------

The following recursive procedure search forms combinations using 
backtracking. This can be used as brute-force search to find the 
optimal solution. The parameter :math:`k` is the position in the array 
where the next number is placed. If :math:`k=n` some combination has 
been completed, in which case it is printed. Otherwise, the search 
goes through all the ways to place numbers :math:`1...m` in 
position :math:`k` and continues recursively to :math:`k+1`. 
The search starts with the call ``search(0)``, and 
``numbers`` is an :math:`n`-sized array in which the combination is formed.

.. codeinclude:: Design/comb

Figure :num:`Figure #BackTrack1` shows how the search starts in case 𝑛=3 
and :math:`m=4`. The sign ":math:`-`" means a number that has not 
been selected yet. The first level of the search selects 
the combination to position :math:`0` of the first number. There 
are four options for choosing this, since the possible numbers 
are :math:`1...4`, so the search branches into four parts. 
After this, the search continues recursively and selects 
the numbers for the other positions.

.. _BackTrack1:

.. odsafig:: Images/bb1.png
   :width: 700px
   :align: center
  
   Forming the combination :math:`n=3` and :math:`m=4`.
    
We can evaluate the efficiency of the algorithm by calculating how 
many times the search procedure is called in total during the 
search. The procedure is called once with parameter :math:`0`, :math:`m` 
times with parameter :math:`1`, :math:`m^2` times with parameter 
:math:`2`, etc., so the number of invitations is total

.. math::
   1 + m + m^2 + \dots + m^n = \frac{m^{n+1} - 1}{m - 1} = \Theta(m^n)

At the last level of recursion, more invitations are made 
than at all other levels combined.

Subsets
-------

Let us then examine the situation, where we want to go through all 
:term:`subsets<subset>` of a set with :math:`n` elements. There are a total 
of :math:`2n` subsets, because each element either belongs or does 
not belong to a subset. For example, :math:`\{2,5\}` and 
:math`\{3,5,9\}` are subsets of the set :math:`\{2,3,5,9\}`. 
It turns out that we can form subsets by going through all 
combinations of :math:`n` numbers, where each number is 
:math:`0` or :math:`1`. The idea is that each number in the 
combination tells whether a certain element belongs to a subset. 
For example, when the set is :math:`\{2,3,5,9\}`, the combination 
:math:`[1,0,1,0]` matches subsets :math:`\{2,5\}` and the
combination :math:`[0,1,1,1`] corresponds to the subset 
:math:`\{3,5,9\}`.

The following pseude code shows how we can visit all subsets using 
backtracking. The procedure ``search`` chooses, whether the element 
in :math:`k` is included in the subset or not, and marks this 
information in the array ``choice``. As before, the search starts 
with the call ``search(0)``. 

.. codeinclude:: Design/subset

Permutations
------------

With backtracking, we can also loop through all 
:term:`permutations<permutation>`, i.e. different orders of elements. 
When there are :math:`n` elements in the set, in total 
:math:`n!` permutations can be formed. For example, 
:math:`\{2,4,1,3\}` and :math:`\{4,3,1,2\}`
are permutations of the set :math:`\{1,2,3,4\}`.

In this situation, we want to go through combinations of 
:math:`n` numbers, where each number is between :math:`1...n` and 
no number is repeated. We achieve this by adding a new array 
named ``included`` which tells if a certain number is already included. 
At each step, the search selects only such numbers for the 
combination which have not been selected before. 

.. codeinclude:: Design/perm

The N Queens Problem
----------------------------

Next, we will go through two more demanding examples on how 
to utilize the backtracking to solve problems.

Our task is to calculate, in how many ways :math:`n` queens can be 
placed on an :math:`n \times n` chessboard so that no two queens 
threaten each other. In chess, queens can threaten each other 
horizontally, vertically or diagonally. For example, in the case 
of :math:`n=4`, there are two possible ways to place the queens 
as shown in Figure :num:`Figure #Queen1`.

.. _Queen1:

.. odsafig:: Images/queen_problem1.png
   :width: 500px
   :align: center
  
   Solution to the queens problem with :math:`n=4`.
    
We can solve the task by implementing an algorithm, which goes through 
the board from top to bottom and places one queen for each row. 
Figure :num:`Figure #Queen2` shows the operation of the search in 
the case :math:`n=4`. The queen of the first row can be placed 
in any column, but in the following lines, previous selections 
limit the search. The figure shows the placement of the second 
queen, when the first queen is in the second column. In this case, 
the only option is that the second queen is in the last column, 
because in all other cases the queens would threaten each other.

.. _Queen2:

.. odsafig:: Images/queens_problem2.png
   :width: 700px
   :align: center
  
   Applying backtracking to the :math:`n` queens problem.

The following function ``search`` presents the backtracking 
algorithm which calculates the solutions to the 
:math:`n` queens problem: 

.. codeinclude:: Design/queen

We assume that the rows and columns of the board are numbered 
from :math:`0...n-1`. The parameter :math:`y` tells on which 
row the next queen should be placed, and the search starts with 
the call ``search(0)``. If the row is :math:`n`, all queens have 
already been placed, so one solution has been found. Otherwise, 
a loop that goes through the possible columns (:math:`x`) is 
executed. If the queen can be placed in the column :math:`x` 
i.e. it does not threaten any previously placed queen, the table 
``location`` is updated accordingly (the queen :math:`y` is in the 
column :math:`x`) and the search continues recursively. The 
function ``can_be_placed`` examines whether a new queen can be 
placed on row :math:`y` and column :math:`x`.

Now we have an algorithm that allows us to review solutions to the 
queen problem. The algorithm solves cases with small values of 
:math:`n` very fast, but with larger values of :math:`n`, the 
algorithm starts to take a lot of time. The reason for this is 
that the number of locations where the queens can be placed 
increases exponentially. For example, in the case of :math:`n=20`, 
there are already more than 39 billion different solutions.

However, we can try to speed up the algorithm by improving it 
its implementation. One easy boost is to take advantage of symmetry. 
Each solution to the queen problem is matched by another solution, 
which is obtained by mirroring the solution horizontally. For example, 
in Figure :num:`Figure #Queen1`, the solutions can be changed to 
each other by mirroring. Thanks to this observation, we can halve 
the execution time of the algorithm adding the requirement that 
the first queen must be placed to the left half of the board, 
and finally multiplying the answer by two.

However, the queen problem is fundamentally a hard problem, and 
no essentially better solution than brute force is known. Currently, 
the largest case with a known solution is :math:`n=27`. Processing 
this case took about a year with a large computing cluster.

Allocating tasks
----------------

Let's consider a situation where there are :math:`n` 
tasks and  :math:`n` employees. Tasks should be distributed 
to the employees so that, each employee performs exactly one task. 
For each task-employee combination the cost for completing the 
task is known. The goal is to find a solution where the total 
cost is as low as possible. A table below shows 
an example case where :math:`n=3`. The optimal way to divide 
the tasks is that Employee B performs the first task, C 
performs second task, and A performs the third task. 
The total cost of this solution is :math:`1+2+5=8`.

.. math::
   \large
   \begin{array}{c|c|c|c}
   \text{Employee A} & 4 & 8 & \textbf{5} \\
   \hline
   \text{Employee B} & \textbf{1} & 1 & 3 \\
   \hline
   \text{Employee C} & 4 & \textbf{2} & 6 \\
   \end{array}

We assume that tasks and employees are numbered from 
:math:`0...n-1` and we can read from the table array 
``cost[a][b]`` how much does the task :math:`a` costs 
when performed by the employee :math:`b` We can implement 
a backtracking algorithm which goes through the tasks 
in order and chooses an employee for each. The following 
procedure search takes two parameters: :math:`k` is the 
task to be processed next and :math:`h` is the cost so far. 
The search starts with the call ``search(0,0)``. The table 
``included`` keeps track of which employees have already been 
given a task, and the variable :math:`p` is the total cost 
in the best solution found so far. Before the search, the 
value of the variable :math:`p` is set to :math:`\infty` 
because no solution exists yet.

.. codeinclude:: Design/tasks

This is a working backtracking algorithm, and at the end of the 
search, the variable :math:`p` has the total cost of the best 
solution. However, the algorithm is very slow because it always 
goes through all the :math:`n!` possible solutions. Since we 
only want to find the best solution and not go through all the 
solutions, we can improve the algorithm by adding a condition 
which stops forming a solution if it cannot get better than an 
earlier solution.

Branch And Bound
----------------

We next test the previous algorithm with the case, where :math:`n=20` 
and the table ``cost`` contains random integers between :math:`1` and 
:math:`100`. In this case, the algorithm described above would go through

.. math::
   20! = 2432902008176640000

different solutions which would take hundreds of years. 
In order to solve the case, we need to improve the algorithm so, 
that it does not go through all solutions but still finds the 
best solution. This is where a technique called 
:term:`branch and bound<branch-and-bounds algorithm>` can be applied. 
The idea is to make the backtracking more efficient by reducing 
the number of solutions to be investigated with suitable upper and 
lower bounds.

The key observation is that we can restrict the search with the 
help of the variable :math:`p`. This variable has at every 
moment the total cost of the best solution found so far. 
Therefore it tells the upper bound on how large the total cost 
of best solution can be. On the other hand, the variable :math:`h` has 
the current cost of solution being formed. This is the lower bound 
for the total cost. If :math:`h>=p` the solution being formed 
cannot get better than the earlier best. We can add to the 
following inspection to the beginning of the algorithm:

.. codeinclude:: Design/tasksImproved1

Thanks to this, the formation of the solution ends immediately 
if its cost is equal to or higher than the cost of the best known 
solution. With this simple modification the problem (:math:`n=20`) 
can be solved within minutes instead of hundreds of years.

We can improve the algorithm even more by calculating a more 
accurate estimate for the lower bound. The cost of the solution 
under construction is certainly at least :math:`h` but we can 
also estimate how much employees allocated for the remaining 
tasks add to the cost:

.. codeinclude:: Design/tasksImproved2

Here the function estimate should give some estimate on how much does 
it cost to complete the remaining tasks :math:`k...n-1`. One simple 
way to get an estimate is to go through the remaining tasks and choose 
the cheapest employee for each task without caring whether the 
employee has been selected before. This gives the lower bound for 
the remaining costs. With this modification the original problem can be solved in seconds. 

|

This page was translated and modified from Antti Laaksonen, 
Tietorakenteet ja algoritmit (Chapter 8) published under Creative 
Commons BY-NC-SA 4.0 license.



