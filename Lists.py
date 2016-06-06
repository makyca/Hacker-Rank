#Task 
#Initialize your list (L = []) and follow the N commands given over N lines. Each command will have its own value(s) separated by a space.
#Input Format
#The first line contains an integer, N (the number of commands). 
#The N subsequent lines each contain one of the  commands described above.
#Sample Input
#4
#insert 0 5
#insert 1 10
#insert 0 6
#remove 6
L = []
n = int(raw_input())
i=0

while i<n:
    i +=1
    line = raw_input()
    if line.find(' '):
        line = line.split()
    
    if line[0]=='append':
        L.append(int(line[1]))
    elif line[0]=='insert':
        L.insert(int(line[1]),int(line[2]))
    elif line[0]=='remove':
        L.remove(int(line[1]))
    elif line[0]=='pop':
        L.pop()
    elif line[0]=='index':
        L.index(int(line[1]))
    elif line[0]=='count':
        L.count(int(line[1]))
    elif line[0]=='sort':
        L.sort()
    elif line[0]=='reverse':
        L.reverse()
    else: print L
