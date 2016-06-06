#Task 
#Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates 
#those values that exist in either M or N but do not exist in both.
#Input Format
#The first line of input contains an integer, M.
#The second line contains M space-separated integers. 
#The third line contains an integer, N. 
#The fourth line contains N space-separated integers.
#Output Format
#Output the symmetric difference integers in ascending order, one per line.
Memova = int(raw_input())
m = set(map(int, raw_input().split(' ')))
Nemova = int(raw_input())
n = set(map(int, raw_input().split(' ')))
mix1 = n.symmetric_difference(m)
for x in sorted(list(mix1)):
    print x
