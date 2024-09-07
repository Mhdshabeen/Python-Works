# write a prgm to find the area and diameter of a circle

#read radius from the user

#area = 3.14*radius**2 or 3.14*radius*radius

radius=int(input("Enter the radius of circle:> "))

area=3.14*radius**2

diameter=radius*2

print(f"Area of the circle with given radius=> {area} ")

print(f"Diameter of the circle =>{diameter}")