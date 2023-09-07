.. avmetadata::
   :author: Tuomas Eerola & Veikka Immonen
   :topic: Algorithm Design Principles

Algorithm Design Principles
===========================

In this chapter we will go through some useful
principles for designing algorithms. These should be seen as
possible tools or ways to approach a new problem instead strict
guidelines for developing algorithms. It is often beneficial to
combine different principles to solve a problem.

The algorithm design principles presented here are:

-   :ref:`The greedy approach<Greedy>`: algorithms that make locally optimal
    choices at each step.
-   :term:`Divide and conquer<divide and conquer>`: a technique for 
    designing algorithms where a solution is found by breaking the 
    problem into smaller (similar) subproblems, solving the subproblems,
    then combining the subproblem solutions to form the
    solution to the original problem. Good examples of algorithms 
    that use the divide and conquer design principle are the
    sorting algorithms :ref:`Mergesort<Mergesort>` and
    :ref:`Quicksort<Quicksort>`.
-   :ref:`Backtracking<Backtracking>`: a heuristic for brute-force search of a 
    solution space. It is essentially a depth-first search 
    of the solution space. This can be improved using a 
    branch-and-bounds algorithm.
-   :ref:`Dynamic programming<DynamicProgramming>`: an approach to
    designing algorithms that works by storing a table of results
    for subproblems.
-   :ref:`Probabilistic algorithms<Probabilistic>`: algorithms
    that utilize randomness in some way to, for example,
    speed up the algorithm. 

