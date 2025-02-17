#/* *** ODSATag: LList *** */
#import java.util.NoSuchElementException;
#
#// Linked list implementation
#/* *** ODSATag: LListVars *** */
#class LList implements List {
#  private Link head;         // Pointer to list header
#  private Link tail;         // Pointer to last element
#  private Link curr;         // Access to current element
#  private int listSize;      // Size of list
#/* *** ODSAendTag: LListVars *** */
#
#/* *** ODSATag: LListCons *** */
#  // Constructors
#  LList(int size) { this(); }     // Constructor -- Ignore size
#  LList() { clear(); }
#
#  // Remove all elements
#  public void clear() {
#    curr = tail = new Link(null); // Create trailer
#    head = new Link(tail);        // Create header
#    listSize = 0;
#  }
#/* *** ODSAendTag: LListCons *** */
#  
#/* *** ODSATag: LListInsert *** */
# Insert "it" at current position
def insert(self, it):
    self.curr.next = Link(self.curr.element, self.curr.next)
    self.curr.element = it
    if (self.tail == self.curr):
        self.tail = self.curr.next  # New tail
    self.listSize += 1
    return True
#/* *** ODSAendTag: LListInsert *** */
#  
#  // Append "it" to list
#  public boolean append(Object it) {
#    tail.setNext(new Link(null));
#    tail.setElement(it);
#    tail = tail.next();
#    listSize++;
#    return true;
#  }
#
#/* *** ODSATag: LListRemove *** */
# Remove and return current element
def remove(self):
    if (self.curr == self.tail)                 # Nothing to remove
        return None
    it = self.curr.element                      # Remember value
    self.curr.element = self.curr.next.element  # Pull forward the next element
    if self.curr.next == self.tail:
        self.tail = self.curr                   # Removed last, move tail
    self.curr.next = self.curr.next.next        # Point around unneeded link
    self.listSize -= 1                          # Decrement element count
    return it                                   # Return value
#/* *** ODSAendTag: LListRemove *** */
#
#  public void moveToStart() { curr = head.next(); } // Set curr at list start
#  public void moveToEnd() { curr = tail; }          // Set curr at list end
#
#/* *** ODSATag: LListPrev *** */
#  // Move curr one step left; no change if now at front
#  public void prev() {
#    if (head.next() == curr) return; // No previous element
#    Link temp = head;
#    // March down list until we find the previous element
#    while (temp.next() != curr) temp = temp.next();
#    curr = temp;
#  }
#/* *** ODSAendTag: LListPrev *** */
#
#/* *** ODSATag: LListNext *** */
#  // Move curr one step right; no change if now at end
#  public void next() { if (curr != tail) curr = curr.next(); }
#/* *** ODSAendTag: LListNext *** */
#
#  public int length() { return listSize; } // Return list length
#
#
#  // Return the position of the current element
#  public int currPos() {
#    Link temp = head.next();
#    int i;
#    for (i=0; curr != temp; i++)
#      temp = temp.next();
#    return i;
#  }
#  
#/* *** ODSATag: LListPos *** */
#  // Move down list to "pos" position
#  public boolean moveToPos(int pos) {
#    if ((pos < 0) || (pos > listSize)) return false;
#    curr = head.next();
#    for(int i=0; i<pos; i++) curr = curr.next();
#    return true;
#  }
#/* *** ODSAendTag: LListPos *** */
#
#  // Return true if current position is at end of the list
#  public boolean isAtEnd() { return curr == tail; }
#
#  // Return current element value.
#  public Object getValue() throws NoSuchElementException {
#    if (curr == tail) // No current element
#      throw new NoSuchElementException("getvalue() in LList has current of " + curr + " and size of "
#        + listSize + " that is not a a valid element");
#    return curr.element(); 
#  }
#
#  // Check if the list is empty
#  public boolean isEmpty() { return listSize == 0; }
#}
#/* *** ODSAendTag: LList *** */
