#Task 
#Read an integer N. For all non-negative integers i<N , print i^2. 
#Input Format 
#The first and only line contains the integer, N.
#Output Format 
#Print  lines, one corresponding to each i.
n = int(raw_input())
i = 0
while i<n:
    print i*i
    i+=1
