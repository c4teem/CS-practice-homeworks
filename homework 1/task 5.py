# FIVE

radius = int(input("Enter radius: "))
x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x*x + y*y < radius*radius:
    print("The dot is inside the circle")
else:
    print("The dot is not inside the circle")