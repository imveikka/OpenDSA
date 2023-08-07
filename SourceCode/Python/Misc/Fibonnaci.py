#import java.io.*;
#
#// Tester for Fibonnaci code
#public class Fibonnaci {
#
#static boolean SUCCESS = true;
#static int Values[];
#
#/* *** ODSATag: FibR *** */
# Recursively generates and returns the n'th Fibonacci number
def fibr(n):
    if n <= 0:
        return -1
    if n == 1 or n == 2:            # Base case
        return 1
    return fibr(n-1) + fibr(n-2)    # Recursive call
#/* *** ODSAendTag: FibR *** */
#
#/* *** ODSATag: FibRT *** */
def fibrt(n):
    # Assume Values has at least n slots,
    # and all slots are initialized to 0
    if n <= 0:
        return -1
    if n <= 2:                              # Base case
        return 1
    if Values[n] == 0:
        Values[n] = fibrt(n-1) + fibrt(n-2) # Recursive call
    return Values[n]    
#/* *** ODSAendTag: FibRT *** */
#
#/* *** ODSATag: FibI *** */
def fibi(n):
    if n <= 0:
        return -1
    curr, prev, past = 1, 1, 0      # curr holds current Fib value 
    for i in range(3, n+1):         # Compute next value
        past = prev                 # past holds fibi(i-2)
        prev = curr                 # prev holfd fibi(i-1)
        curr = past + prev          # curr now holds fibi(i)
    return curr
#/* *** ODSAendTag: FibI *** */
#
#public static void main(String args[]) throws IOException {
#  long temp1, temp2, temp3;
#
#  Values = new int[92];
#
#  for (int i=0; i<=91; i++) Values[i] = 0;
#  temp1 = fibr(30);
#  temp2 = fibrt(30);
#  temp3 = fibi(30);
#  System.out.println("Got " + temp1);
#  if ((temp1 != temp2) || (temp1 != temp3))
#    SUCCESS = false;
#
#  if (SUCCESS) {
#    PrintWriter output = new PrintWriter("success");
#    output.println("Success");
#    output.flush();
#    output.close();
#    System.out.println("Success!");
#  } else {
#    System.out.println("Testing failed");
#  }
#}
#
#}
