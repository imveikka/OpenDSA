.. This file is part of the OpenDSA eTextbook project. See
.. http://opendsa.org for more details.
.. Copyright (c) 2012-2020 by the OpenDSA Project Contributors, and
.. distributed under an MIT open source license.

.. avmetadata::
   :author: Molly Domino

Bags
====

Objectives
----------

Upon completion of this module, students will be able to:

* Name the function and purpose of basic Java data structures
* State key characteristics of Bags in Java
* Build and populate Bags in Java

Suggested Reading
~~~~~~~~~~~~~~~~~

Chapters 1 - 3 Bags from  `Data Structures and Abstractions with Java, 4th edition  by Frank M. Carrano and Timothy Henry <https://www.amazon.com/Data-Structures-Abstractions-Java-4th/dp/0133744051/ref=sr_1_1?ie=UTF8&qid=1433699101&sr=8-1&keywords=Data+Structures+and+Abstractions+with+Java>`_


Introduction to Bags
--------------------

Data structures provide a model for organizing and manipulating a collection of
data.  They are an example of an Abstract Data Type or ADT.  Previously, if you
wanted to store an integer value representing, for example, the thermostat
temperature setting for a room, you would use a statement like 

.. code-block:: java

    int temp = 75;
    
However, what if you had to store and track the thermostat temperature settings
for 500 rooms of a commercial building?  It would be tedious to create an int
variable for each of them.  Conceptually client code can think of grouping the
data into an appropriate data structure, for example, a list or a bag.  Client
code can then interact with it accordingly, such as by adding or removing items.
With respect to the thermostat temperature setting example, client code would
add to the selected data structure an integer value to represent the temperature
setting for each room in the commercial building.  We would, of course, need a
way to identify which integer value was associated with a given room, concerns
like this will be explored in further detail throughout this course.  Common
introductory linear data structures are bags, stacks, queues, and lists.  Data
structures can also be organized as trees or graphs and in multiple dimensions,
they can be indexed by position or by a key such as in a dictionary.

This module introduces the Bag ADT.  It is a finite collection of objects in no
particular order and can contain duplicates.  Bags are used all the time in
everyday life to organize and manage collections of objects, such as the items
in a backpack, a grocery bag, or the movies you've seen this decade.  The
possible behaviors of a bag object are: get the number of items stored in the
bag, check to determine if the bag is empty, add and remove objects, iterate
over the items in the bag, and check to see if the bag contains a specific
object.

When designing a Bag class, there are many things a developer must think about.
In order to implement a Bag its data and methods need to be specified.  When
designing how the methods are expected to work we need to consider all aspects
of a method's intended behavior.  Essential to this is considering what should
happen when tasks cannot be completed, should the code silently fail, notify the
client code of the fact that the task cannot be completed, or perhaps some other
course of action?

A developer also has many options when implementing a data structure.  A key
decision is how to actually store the data.  The client code interacts with a
bag by invoking  its public methods, but under the hood  the bag could possibly
be built with an array or a linked chains of nodes.  Other data structure
implementation decisions involve determining  the various algorithms to
efficiently program specified methods.

Documentation of Bag Interface methods
--------------------------------------

Before looking at implementations of the Bag ADT, we'll first
look at the interface.


UML for BagInterface
~~~~~~~~~~~~~~~~~~~~

The image below presents the UML notation for the BagInterface class.

You may recall that UML, short for Unified Modeling Language, is a standardized
modeling language used to capture, visualize, and communicate the design of a
system.

There are many types of UML diagrams.  Throughout most of the course we will be
using diagrams similar to the one depicted below, these are referred to as **UML
Class Diagrams**.

Observe how the class diagram quickly communicates the name and characteristics
of the software components of a given system.  At a glance you can tell that
this image describes the specification for an Interface, it indicates the
methods that should be common to all classes that implement this ``BagInterface``,
i.e. methods that should be present in all implementations of a Bag.  It also
indicates the access modifiers for fields and methods, as well as details
regarding the parameters and return types for each method.  In this case you
will note the annotation to the left of each method's name indicating that each
method is public.


.. odsafig:: Images/2114BagInterfaceClassDiagram.png
   :align: center


Example of BagInterface Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below you will find example code implementing the BagInterface.

Take a look at how the implementation (the code) matches with the design document
(the UML class diagram).


.. admonition:: The Bag Interface

    .. code-block:: java
    
       package bag;
       /**
       An interface that describes the operations of a bag of objects.
       A bag is an unordered collection of objects of a particular types.
       Duplicates are allowed.
       @author Frank M. Carrano
       @author Timothy M. Henry
       @author Margaret Ellis
       @version April 2020
       */
       public interface BagInterface<T>
       {
       /** Gets the current number of entries in this bag.
          @return  The integer number of entries currently in the bag. */
       public int getCurrentSize();
    
       /** Sees whether this bag is empty.
          @return  True if the bag is empty, or false if not. */
       public boolean isEmpty();
    
       /** Adds a new entry to this bag.
          @param newEntry  The object to be added as a new entry.
          @return  True if the addition is successful, or false if not. */
       public boolean add(T newEntry);
    
       /** Removes one unspecified entry from this bag, if possible.
                @return  Either the removed entry, if the removal.
                    was successful, or null. */
       public T remove();
    
       /** Removes one occurrence of a given entry from this bag.
               @param anEntry  The entry to be removed.
               @return  True if the removal was successful, or false if not. */
           public boolean remove(T anEntry);
    
       /** Removes all entries from this bag. */
       public void clear();
    
       /** Counts the number of times a given entry appears in this bag.
          @param anEntry  The entry to be counted.
                @return  The number of times anEntry appears in the bag. */
       public int getFrequencyOf(T anEntry);
    
       /** Tests whether this bag contains a given entry.
          @param anEntry  The entry to locate.
          @return  True if the bag contains anEntry, or false if not. */
       public boolean contains(T anEntry);
    
       /** Retrieves all entries that are in this bag.
          @param values  An array of generics to be filled with bag contents, if
                  not large enough will throw ArrayIndexOutOfBoundsException
          @return  The values array filled with the entries in the bag.
              Note: If the bag is empty, the array is returned unmodified */
       public T[] toArray(T[] values);
    
    
       } // end BagInterface


Interactive: Documentation of Bag Interface Methods [7:28]
----------------------------------------------------------

.. raw:: html


    <center>
       <iframe type="text/javascript" src='https://cdnapisec.kaltura.com/p/2375811/embedPlaykitJs/uiconf_id/52883092?iframeembed=true&entry_id=1_kn4272o0' style="width: 960px; height: 395px" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" frameborder="0"></iframe> 
    </center>


Interactive: Using Bags [4:34]
------------------------------

.. raw:: html

    <!-- TODO: Slides? none for this or previous video but maybe should have shopping cart demo? -->
    <center>
        <iframe type="text/javascript" src='https://cdnapisec.kaltura.com/p/2375811/embedPlaykitJs/uiconf_id/52883092?iframeembed=true&entry_id=1_9d2n6v3x' style="width: 960px; height: 395px" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" frameborder="0"></iframe> 
    </center>


Checkpoint 1
------------

.. avembed:: Exercises/SWDesignAndDataStructs/BagsCheckpoint1Summ.html ka
   :long_name: Checkpoint 1



Programming Practice: ArrayBags
-------------------------------

.. extrtoolembed:: 'Programming Practice: ArrayBags'
   :workout_id: 1910


Array Implementation of Bags
----------------------------

Suggested Reading
~~~~~~~~~~~~~~~~~

Chapter 2 Bag Implementation that Uses Arrays from `Data Structures and Abstractions with Java, 4th edition  by Frank M. Carrano and Timothy Henry <https://www.amazon.com/Data-Structures-Abstractions-Java-4th/dp/0133744051/ref=sr_1_1?ie=UTF8&qid=1433699101&sr=8-1&keywords=Data+Structures+and+Abstractions+with+Java>`_


Interactive: Fixed-Size Array Implementation [9:39]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <!-- TODO: Slides? no, I think because of text within page @bemdmison would it be more consistent if I revisit that on this page?-->
    <center>
    <iframe type="text/javascript" src='https://cdnapisec.kaltura.com/p/2375811/embedPlaykitJs/uiconf_id/52883092?iframeembed=true&entry_id=1_e766pflq' style="width: 960px; height: 395px" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" frameborder="0"></iframe> 
    </center>


ArrayBagsWithJUnitExample Class Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's take a look at the evolution of our design specification.

The Fixed-Size Array Implementation Video described a **realization** of the
Bag ADT.  We took the abstract **concept** of a Bag and **implemented** this
concept in code, in this case by using an Array called contents along with other
fields and methods.

This implementation, referred to by the name ArrayBag1, is now a data structure
that can be used by client code.  Once properly implemented this data structure
will exhibit the characteristics and behaviors of a Bag.

The UML class diagram below visualizes this realization/implementation.

Note the arrow type used.

The open headed arrow with the dashed line indicates that ``ArrayBag1<T>``
implements the ``BagInterface<T>``, essentially this illustrates the intention
for the ``ArrayBag1`` class to realize the operations/behaviors expected of a
Bag (as described by the BagInterface).

We encourage you to take a moment to explore the UML class diagram further, take
note of the fields and their data types, the methods, their **visibility**,
parameter and return types, and the level of detail afforded by the UML
notation.

Observe as well how the UML class diagram can be used to capture and communicate
both the **intended design** of the components of some envisioned system, as
well as the **actual implementation** of the components of a software system.

It helps us quickly understand the functionalities offered by the classes within
the given system.

For example if we wanted to determine the number of items in a Bag we can easily
infer that ``getCurrentSize()`` would provide that information by returning an
``int`` value when we invoke the method.

We can even go a step further than simply inferring, we can use the design
diagram to identify fields or methods that may potentially return some needed
information or help us complete some task or operation.  We can then look at
the documentation for the class to confirm or clarify our initial impressions.

We encourage you to post questions if you are unclear about any of the items
depicted below.


.. odsafig:: Images/2114ArrayBagClassDiagram.png
   :align: center


Interactive: ArrayBagsWithJUnit Example Demonstration [8:17]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <center>
    <iframe type="text/javascript" src='https://cdnapisec.kaltura.com/p/2375811/embedPlaykitJs/uiconf_id/52883092?iframeembed=true&entry_id=1_42v9vnzf' style="width: 960px; height: 395px" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" frameborder="0"></iframe> 
    </center>

Code Example
~~~~~~~~~~~~

.. admonition:: Try It Yourself

  In Eclipse, use the *Project > Download Assignment...* menu command to download the exercise project named "exArrayBagsWithJUnit". 
  



Checkpoint 2
------------

.. avembed:: Exercises/SWDesignAndDataStructs/BagsCheckpoint2Summ.html ka
   :long_name: Checkpoint 2

Demo More bag method implementation
-----------------------------------


Interactive: More on the Bag Method Implementation [5:28] 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <center>
    <iframe type="text/javascript" src='https://cdnapisec.kaltura.com/p/2375811/embedPlaykitJs/uiconf_id/52883092?iframeembed=true&entry_id=1_nk6yv7gj' style="width: 960px; height: 395px" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" frameborder="0"></iframe> 
    </center>
    <br>
    <a href="https://courses.cs.vt.edu/cs2114/SWDesignAndDataStructs/course-notes/ArrayBagMethods.pdf" target="_blank">
    <img src="../html/_static/Images/projector-screen.png" width="32" height="32">
    Video Slides 7.7.7.1-ArrayBagMethods.pdf</img>
    </a>

ArrayBag Class UML Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is the UML class diagram for the ArrayBag class described in the video
above.  Observe how the class diagram differs from the diagram for the
Fixed-Size Array Implementation.

Notably, the **contents** field is no longer ``final``.

As you may recall from the Fixed-Size Array Implementation we did not have a
mechanism for increasing the capacity of the bag, declaring **contents** as ``final``
meant that the array that **contents** referenced could not change.

This implementation of the ArrayBag does not impose such a constraint.

.. odsafig:: Images/2114ArrayBagClassDiagram2.png
   :align: center

Checkpoint 3
------------

.. avembed:: Exercises/SWDesignAndDataStructs/BagsCheckpoint3Summ.html ka
   :long_name: Checkpoint 3


Methods that Remove and Design Improvement Lesson and Demo
----------------------------------------------------------

[5:28] Methods that Remove and Design Improvement, Part 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <center>
    <iframe type="text/javascript" src='https://cdnapisec.kaltura.com/p/2375811/embedPlaykitJs/uiconf_id/52883092?iframeembed=true&entry_id=1_afd08368' style="width: 960px; height: 395px" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" frameborder="0"></iframe> 
    </center>
    <br>
    <a href="https://courses.cs.vt.edu/cs2114/SWDesignAndDataStructs/course-notes/BagsDesignImprovePart1.pdf" target="_blank">
    <img src="../html/_static/Images/projector-screen.png" width="32" height="32">
    Video Slides BagsDesignImprovePart1.pdf</img>
    </a>

[6:45] Methods that Remove and Design Improvement, Part 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <center>
    <iframe type="text/javascript" src='https://cdnapisec.kaltura.com/p/2375811/embedPlaykitJs/uiconf_id/52883092?iframeembed=true&entry_id=1_x16wqf9x' style="width: 960px; height: 395px" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" frameborder="0"></iframe> 
    </center>
    <br>
    <a href="https://courses.cs.vt.edu/cs2114/SWDesignAndDataStructs/course-notes/BagsDesignImprovePart2.pdf" target="_blank">
    <img src="../html/_static/Images/projector-screen.png" width="32" height="32">
    Video Slides BagsDesignImprovePart2.pdf</img>
    </a>

[9:03] Methods that Remove and Design Improvement, Part 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <center>
    <iframe type="text/javascript" src='https://cdnapisec.kaltura.com/p/2375811/embedPlaykitJs/uiconf_id/52883092?iframeembed=true&entry_id=1_54w07n1k' style="width: 960px; height: 395px" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" frameborder="0"></iframe> 
    </center>
    <br>
    <a href="https://courses.cs.vt.edu/cs2114/SWDesignAndDataStructs/course-notes/BagsDesignImprovePart3.pdf" target="_blank">
    <img src="../html/_static/Images/projector-screen.png" width="32" height="32">
    Video Slides BagsDesignImprovePart3.pdf</img>
    </a>

Checkpoint 4
------------

.. avembed:: Exercises/SWDesignAndDataStructs/BagsCheckpoint4Summ.html ka
   :long_name: Checkpoint 4


Interactive: Array resizing description and coding Demo [14:47]
---------------------------------------------------------------

.. raw:: html
     
    <center>
    <iframe type="text/javascript" src='https://cdnapisec.kaltura.com/p/2375811/embedPlaykitJs/uiconf_id/52883092?iframeembed=true&entry_id=1_10v1aoku' style="width: 960px; height: 395px" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" frameborder="0"></iframe> 
    </center>
    <br>
    <a href="https://courses.cs.vt.edu/cs2114/SWDesignAndDataStructs/course-notes/7.7.9.1-DoubleArray.pdf" target="_blank">
    <img src="../html/_static/Images/projector-screen.png" width="32" height="32">
    Video Slides 7.7.9.1-DoubleArray.pdf</img>
    </a>

Tradeoffs of using an array implementation for a bag
----------------------------------------------------

.. list-table:: Tradeoffs
   :header-rows: 1

   * - Pros
     - Cons
   * - Adding an entry to the bag is fast
     - Increasing the size of the array requires time to copy its entries
   * - Removing an unspecified entry is fast
     - Removing a specified entry requires time to locate the entry


Programming Practice: The Bag Interface
---------------------------------------

.. extrtoolembed:: 'Programming Practice: The Bag Interface'
   :workout_id: 1909
