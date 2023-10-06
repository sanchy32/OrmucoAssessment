'''Created 2023-10-16
@author: Godswill Agbofode'''

#3Alternate way
# line = input('Enter first line in the format "(Point 1, Point 2)"\n')
# nline = line[1:(int(len(line))-1)]
# line = nline.split(", ")
# x1, x2 = float(line[0]), float(line[1])
#
# line = input("Enter first line in the format <(Point 1, Point 2)>\n")
# nline = line[1:(int(len(line))-1)]
# line = nline.split(", ")
# x3, x4 = float(line[0]), float(line[1])

x1 = float(input("Enter starting point on first line\n"))
x2 = float(input("Enter ending point on first line\n"))
x3 = float(input("Enter starting point on second line\n"))
x4 = float(input("Enter ending point on second line\n"))

if x3 <= x4:
    if x1 >= x3 and x1<= x4 or x2 >= x3 and x2 <= x4:
        print("Yes they overlap")
        exit()
elif x4 <= x3:
    if x1 >= x4 and x1 <= x3 or x2 >= x4 and x2 <= x3:
        print("Yes they overlap")
        exit()

if x1 <= x2:
    if x3 >= x1 and x3 <= x2 or x4 >= x1 and x4 <= x2:
        print("Yes they overlap")
        exit()
elif x2 >= x1:
    if x3 >= x2 and x3 <= x1 or x4 >= x2 and x4 <= x1:
        print("Yes they overlap")
        exit()

print("No they don't overlap")