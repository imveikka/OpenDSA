.. This file is part of the OpenDSA eTextbook project. See
.. http://opendsa.org for more details.
.. Copyright (c) 2012-2020 by the OpenDSA Project Contributors, and
.. distributed under an MIT open source license.

.. avmetadata::
   :author: Cliff Shaffer
   :requires: comparison; sorting terminology
   :satisfies: mergesort
   :topic: Sorting

.. index:: ! Mergesort

Mergesort Concepts
==================

Mergesort Concepts
------------------

A natural approach to problem solving is divide and conquer.
To use divide and conquer when sorting, we might consider breaking the
list to be sorted into pieces, process the pieces, and then put them
back together somehow.
A simple way to do this would be to split the list in half, sort
the halves, and then merge the sorted halves together.
This is the idea behind :term:`Mergesort`.

Mergesort is one of the simplest sorting algorithms conceptually,
and has good performance both in the asymptotic 
sense and in empirical running time.
Unfortunately, even though it is based on a simple concept,
it is relatively difficult to implement in practice.
Here is an example implementation of Mergesort in Python:

.. codeinclude:: Sorting/Mergesort 
   :tag: mergesort 

Here is a visualization that illustrates how Mergesort works.

.. avembed:: AV/Sorting/mergesortAV.html ss
   :long_name: Mergesort Visualization

The hardest step to understand about Mergesort is the merge function.
The merge function starts by examining the first record of each
sublist and picks the smaller value as the smallest record overall.
This smaller value is removed from its sublist and placed into the
output list.
Merging continues in this way, comparing the front
records of the sublists and continually appending the smaller to the
output list until no more input records remain.

Here is an implementation in Python for ``merge`` on lists:

.. codeinclude:: Sorting/Mergesort 
   :tag: merge

Here is a visualization for the merge operation.

.. inlineav:: mergesortCON ss
   :long_name: Merging Slideshow
   :scripts: AV/Sorting/mergesortCON.js
   :output: show


This visualization provides a running time analysis for Merge Sort.

.. inlineav:: MergeSortAnalysisCON ss
   :long_name: Mergesort Analysis Slideshow
   :links: AV/Sorting/MergeSortAnalysisCON.css
   :scripts: AV/Sorting/MergeSortAnalysisCON.js
   :output: show
