#// Array-based stack implementation
#/* *** ODSATag: AStack1 *** */
#class AStack implements Stack {
#  private Object stackArray[];    // Array holding stack
#  private static final int DEFAULT_SIZE = 10;
#  private int maxSize;            // Maximum size of stack
#  private int top;                // First free position at top
#
#  // Constructors
#  AStack(int size) {
#    maxSize = size;
#    top = 0;
#    stackArray = new Object[size]; // Create stackArray
#  }
#  AStack() { this(DEFAULT_SIZE); }
#/* *** ODSAendTag: AStack1 *** */
#
#  public String toString() {
#    StringBuffer out = new StringBuffer(top * 4);
#    for (int i=top-1; i>=0; i--) {
#      out.append(stackArray[i]);
#      out.append(" ");
#    }
#    return out.toString();
#  }
#/* *** ODSATag: AStack2 *** */
#
#  public void clear() { top = 0; }    // Reinitialize stack
#
#// Push "it" onto stack
/* *** ODSATag: AStackPush *** */
def push(self, it):
    if self.top >= self.maxSize:
        return False
    self.stackArray[self.top] = it
    self.top += 1
    return True
/* *** ODSAendTag: AStackPush *** */
#
#// Remove and return top element
/* *** ODSATag: AStackPop *** */
def pop(self):
    if self.top == 0:
        return None
    self.top -= 1
    return self.stackArray[self.top]
/* *** ODSAendTag: AStackPop *** */
#
#  public Object topValue() {          // Return top element
#    if (top == 0) return null;
#    return stackArray[top-1];
#  }
#
#  public int length() { return top; } // Return stack size
#
#  public boolean isEmpty() { return top == 0; } // Check if the stack is empty
#}
#/* *** ODSAendTag: AStack2 *** */
