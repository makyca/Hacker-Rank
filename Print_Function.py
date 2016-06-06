#Task 
#Read an integer N. Without using any string methods, try to print the following: 1,2,...,N
from __future__ import print_function
map(lambda x: print(x, end =''), range(1,(int(raw_input())+1)))
