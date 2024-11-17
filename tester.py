from geo.utils import pythagoras, circle

# Calculate the length of hypotenuse (c) when a=3 and b=4
a, b = 3, 4
c = pythagoras(a, b)
print('c =', c)

# Calculate the area of a circle with radius r=10
r = 10
area = circle(r)
print('area =', area)
