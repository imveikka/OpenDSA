.. This file is part of the OpenDSA eTextbook project. See
.. http://opendsa.org for more details.
.. Copyright (c) 2012-2020 by the OpenDSA Project Contributors, and
.. distributed under an MIT open source license.

.. avmetadata::
   :author: Cliff Shaffer
   :satisfies: binary search
   :topic: Searching

Searching in an Array
=====================

Sequential Search
-----------------

If you want to find the position in an unsorted array of :math:`n`
integers that stores a particular value, you cannot really do better
than simply looking through the array from the beginning and move
toward the end until you find what you are looking for.
This algorithm is called :term:`sequential search`.
If you do find it, we call this a :term:`successful search`.
If the value is not in the array, eventually you will reach the end.
We will call this an :term:`unsuccessful search`.
Here is a simple implementation for sequential search.

.. codeinclude:: Searching/Sequential
      :tag: Sequential

It is natural to ask how long a program or algorithm will take to
run.
But we do not really care exactly how long a particular program will
run on a particular computer.
We just want some sort of estimate that will let us compare one
approach to solving a problem with another.
This is the basic idea of :term:`algorithm analysis`.
In the case of sequential search, it is easy to see that if the value
is in position :math:`i` of the array, then sequential search will
look at :math:`i` values to find it.
If the value is not in the array at all, then we must look at
:math:`n` values if the array holds :math:`n` values.
This would be called the :term:`worst case` for sequential search.
Since the amount of work is proportional to :math:`n`,
we say that the worst case for sequential search has
:term:`linear cost <linear growth rate>`.
For this reason, the sequential search algorithm is sometimes
called :term:`linear search`.

Binary Search
-------------

Sequential search is the best that we can do when trying to find a
value in an unsorted array. [#]_
But if the array is sorted in increasing order by value, then we can
do much better.
We use a process called :term:`binary search`.

Binary search begins by examining the value in the middle
position of the array; call this position :math:`mid` and the
corresponding value :math:`k_{mid}`.
If :math:`k_{mid} = K`, then processing can stop immediately.
This is unlikely to be the case, however.
Fortunately, knowing the middle value provides useful information
that can help guide the search process.
In particular, if :math:`k_{mid} > K`, then you know that the value
:math:`K` cannot appear in the array at any position greater
than :math:`mid`. 
Thus, you can eliminate future search in the upper half of the array.
Conversely, if :math:`k_{mid} < K`, then you know that you can
ignore all positions in the array less than :math:`mid`.
Either way, half of the positions are eliminated from further
consideration.
Binary search next looks at the middle position in that part of the
array where value :math:`K` may exist.
The value at this position again allows us to eliminate half
of the remaining positions from consideration.
This process repeats until either the desired value is found, or
there are no positions remaining in the array that might contain the
value :math:`K`.
Here is an illustration of the binary search method.

.. inlineav:: binarySearchCON ss
   :long_name: Binary Search Algorithm Slideshow
   :links: AV/Searching/binarySearchCON.css
   :scripts: AV/Searching/binarySearchCON.js
   :output: show

With the right math techniques, it is not too hard to show that the
cost of binary search on an array of :math:`n` values is at most
:math:`\log n`.
This is because we are repeatedly splitting the size of the subarray
that we must look at in half.
We stop (in the worst case) when we reach a subarray of size 1.
And we can only cut the value of :math:`n` in half :math:`\log n`
times before we reach 1. [#]_

Analyzing Binary Search
-----------------------

.. inlineav:: BsearchDandCRecurCON ss
   :long_name: Binary Search recurrence slideshow
   :links: AV/AlgAnal/BsearchDandCRecurCON.css
   :scripts: AV/AlgAnal/BsearchDandCRecurCON.js
   :output: show

Function ``binarySearch`` is designed to find the (single) occurrence of
:math:`K` and return its position. 
A special value is returned if :math:`K` does not appear in the array.
This algorithm can be modified to implement variations 
such as returning the position of the first
occurrence of :math:`K` in the array if multiple occurrences are
allowed, and returning the position of the greatest value less than
:math:`K` when :math:`K` is not in the array.

Comparing sequential search to binary search, we see that as :math:`n`
grows, the :math:`\Theta(n)` running time for sequential search in the
average and worst cases quickly becomes much greater than the
:math:`\Theta(\log n)` running time for binary search.
Taken in isolation, binary search appears to be much more
efficient than sequential search.
This is despite the fact that the constant factor for binary search is 
greater than that for sequential search, because the calculation for
the next search position in binary search is more expensive than just
incrementing the current position, as sequential search does.

Note however that the running time for sequential search will be
roughly the same regardless of whether or not the array values are
stored in order.
In contrast, binary search requires that the array values be ordered
from lowest to highest.
Depending on the context in which binary search is to be used, this
requirement for a sorted array could be detrimental to the running
time of a complete program, because  maintaining the values in sorted
order requires a greater cost when inserting new elements into the
array.
This is an example of a tradeoff between the
advantage of binary search during search and the disadvantage related
to maintaining a sorted array.
Only in the context of the complete problem to be solved can we know
whether the advantage outweighs the disadvantage.

