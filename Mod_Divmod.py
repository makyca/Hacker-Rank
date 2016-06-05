#Task 
#Read in two integers, a and b, and print three lines. 
#The first line is the integer division a//b
#The second line is the result of the modulo operator: a%b
#The third line prints the divmod of a and b.
#Input Format 
#The first line contains the first integer, a, and the second line contains the second integer, b.
#Sample Input
#177
#10
#Sample Output
#17
#7
#(17, 7)
from __future__ import division
a = int(raw_input())
b = int(raw_input())
print a//b
print a%b
print divmod(a,b)
