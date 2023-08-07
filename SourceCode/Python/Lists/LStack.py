#/* *** ODSATag: LStack1 *** */
#// Linked stack implementation
#class LStack implements Stack {
#  private Link top;               // Pointer to first element
#  private int size;               // Number of elements
#
#  // Constructors
#  LStack() { top = null; size = 0; }
#  LStack(int size) { top = null; size = 0; }
#/* *** ODSAendTag: LStack1 *** */
#
#  public String toString() {
#    StringBuffer out = new StringBuffer(size * 4);
#    for (Link temp = top; temp != null;  temp = temp.next()) {
#      out.append(temp.element());
#      out.append(" ");
#    }
#    return out.toString();
#  }
#/* *** ODSATag: LStack2 *** */
#
#  // Reinitialize stack
#  public void clear() { top = null; size = 0; }
#
#// Put "it" on stack
/* *** ODSATag: LStackPush *** */  
def push(self, it):
    top = Link(it, self.top)
    self.size += 1
    return True
/* *** ODSAendTag: LStackPush *** */
#
#// Remove "it" from stack
/* *** ODSATag: LStackPop *** */    
def pop(self):
    if self.top == None:
        return None
    it = self.top.element
    self.top = self.top.next
    self.size -= 1
    return it
/* *** ODSAendTag: LStackPop *** */
#
#  public Object topValue() {      // Return top value
#    if (top == null) return null;
#    return top.element();
#  }
#
#  // Return stack length
#  public int length() { return size; }
#  
#  // Check if the stack is empty
#  public boolean isEmpty() { return size == 0; }
#}
#/* *** ODSAendTag: LStack2 *** */
