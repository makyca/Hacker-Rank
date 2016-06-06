#Task 
#You are given an integer, N, on a single line. The next line contains N space-separated integers. 
#Create a tuple, T, of those N integers, then compute and print the result of hash().
#Input Format
#The first line contains an integer, N (the number of elements in the tuple). 
#The second line contains N space-separated integers describing T.
#Output Format
#Print the result of hash().
n = int(raw_input())
print hash(tuple(map(int, raw_input().split(" "))))
