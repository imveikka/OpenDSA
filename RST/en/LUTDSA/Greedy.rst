.. avmetadata::
   :author: Tuomas Eerola & Veikka Immonen
   :topic: Greedy Approach

The Greedy Approach
===================

Algorithm utilizing the :term:`greedy approach <greedy algorithm>` 
proceed step by step. 
On each step, the best option is selected based on the information 
available at that time (locally optimal choice). It is good to 
note that there are often multiple ways to define what is the 
optimal choice. For example, we need to visit a set of cities 
and we want to develop an algorithm that selects the route between 
the cities so that the total distance is as small as possible. 
The locally optimal choice might be a) the nearest city from 
the current city, or b) the nearest two cities that are not 
part of the route yet or are end points of the existing route. 
Depending on the choice we might end up in different solution.

Often the choice that seems the best on the current step does 
not lead to the optimal solution at then end, but the greedy 
approach often helps to find a reasonably good solution. 
Therefore, the greedy approach is suitable when we want to 
find a good solution fast, but we do not necessarily need the 
optimal solution. However, there are also problems for which 
a greedy algorithm that always finds the optimal solution is known.

.. topic:: Example

  We need to schedule jobs out of a set of :math:`N` jobs so that the profit 
  is maximized. Each job takes unit time for execution. Each job has a 
  deadline and profit. Profit is earned only if the job is completed by 
  the deadline.

  .. math::

     \begin{array}{c|c|c}
     \textbf{Job} & \textbf{Deadline} & \textbf{Profit} \\
     \hline
     1            & 3                 & 100 \\
     2            & 2                 &  50 \\
     3            & 1                 &  20 \\
     4            & 2                 & 100
     \end{array}

  The simple solutions is to test all the possible schedules 
  (orders of jobs) and to select then the one that gives the 
  highest profit. However, there are :math:`N!` different permutations 
  of :math:`N` jobs. Therefore such brute-force solution has a running 
  time of :math:`\Theta(N!)`. With a greedy approach we can be much 
  more efficient.

  Let us consider the following simple greedy algorithm:

  .. codeinclude:: Design/schedule
    
  The algorithm "greedily" starts with the most profitable job, 
  proceeds to the second most profitable, and so on. We start with 
  sorting the job list which can be done in :math:`\Theta(N \log(N))` time. 
  The actual scheduling part goes through the job list once and is 
  :math:`\Theta(N)`. Therefore, the whole algorithm is 
  :math:`\Theta(N \log(N))`. If we apply the algorithm to the above 
  table of jobs we get the following solution: 

  .. math::

     \begin{array}{c|c|c|c}
     \textbf{Job} & \textbf{Deadline} & \textbf{Profit} &
     \textbf{Schedule} \\
     \hline
     1            & 3                 & 100             & 2 \\
     2            & 2                 &  50             & - \\
     3            & 1                 &  20             & - \\
     4            & 2                 & 100             & 1
     \end{array}

  And the total profit is :math:`220`.

  We can do better than this. Let us consider the following modification 
  of the greedy algorithm:

  .. codeinclude:: Design/scheduleBetter

  The new version of the algorithm does not only choose the most 
  profitable jobs first but also schedule them in locally optimal manner: 

  .. math::

     \begin{array}{c|c|c|c}
     \textbf{Job} & \textbf{Deadline} & \textbf{Profit} &
     \textbf{Schedule} \\
     \hline
     1            & 3                 & 100             & 3 \\
     2            & 2                 &  50             & 1 \\
     3            & 1                 &  20             & - \\
     4            & 2                 & 100             & 2
     \end{array}

  Now, the total profit is :math:`270`.

  It can be proven that the latter greedy algorithm provides always 
  the optimal solution. However, due to the two nested loops, the 
  average running time of this algorithm is :math:`\Theta(N^2)`.
