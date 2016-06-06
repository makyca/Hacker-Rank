#Task
#You are given N numbers. Store them in a list and find the second largest number.
#NOTE: Do not use the insertion sort method.
#Input Format
#The first line contains N. The second line contains an array [] of N integers each separated by a space
n = int(raw_input())
lista = map(int, raw_input().split(' '))
print max([x for x in lista if x != max(lista)])
