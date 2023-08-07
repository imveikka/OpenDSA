
#/* *** ODSATag: ListADT *** */
# List class ADT.
class List:
  # Remove all contents from the list, so it is once again empty.
  def clear(self):

  # Insert "it" at the current location.
  def insert(self, it):

  # Append "it" at the end of the list.
  def append(self, it):

  # Remove and return the current element.
  def remove(self):

  # Set the current position to the start of the list.
  def moveToStart(self):

  # Set the current position to the end of the list.
  def moveToEnd(self):

  # Move the current position one step left, no change if already at beginning.
  def prev(self):

  # Move the current position one step right, no change if already at end.
  def next(self):

  # Return the number of elements in the list.
  def length(self):

  # Return the position of the current element.
  def currPos(self):

  # Set the current position to "pos".
  def moveToPos(self, pos):

  # Return true if current position is at end of the list.
  def isAtEnd(self):

  # Return the current element.
  def getValue(self):
  
  # Tell if the list is empty or not.
  def isEmpty():
#/* *** ODSAendTag: ListADT *** */
