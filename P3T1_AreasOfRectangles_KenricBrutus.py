# CTI-110
# P3T1 Area of Rectangles
# Kenric Brutus
# 6/19/2018

# Calculating which rectangle has the highest area.


# The dimensions of rectangle 1.
length1 = int(input("Enter the length of rectangle 1: "))
width1 = int(input("Enter the width of rectangle 1: "))


# The dimensions of rectangle 2.
length2 = int(input("Enter the length of rectangle2: "))
width2 = int(input("Enter the width of rectangle2: "))


# The area of the rectangles.
area1 = length1 * width1
area2 = length2 * width2


# Which has the greater area.
if area1 > area2:
    print("Rectangle 1 has the greater area.")
elif area2 > area1:
    print("Rectangle 2 has the greater area.")
else:
    print("Both have the same area.")
