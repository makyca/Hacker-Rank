#Task
#You have to print a list of all possible coordinates on a 3D grid where the sum of Xi+Yi+Zi is not equal to N. If X=2, 
#the possible values of X can be 0,1 and 2. The same applies to Y and Z.
#Input Format
#Four integers X,Y,Z and N each on four separate lines, respectively.
x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
N = int(raw_input())

possibleCoordinates = [[x,y,z] for x in range(x+1) for y in range(y+1) for z in range(z+1) if (x+y+z) != N]

print possibleCoordinates
