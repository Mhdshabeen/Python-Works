# write a program to find the area and perimete of triangle

#read side,base and height from user

#area= 1/2*base*height

#perimeter=side1+side2+base

side1=int(input("Enter the length of side A :> "))

side2=int(input("Enter the length of side C :>"))

base=int(input("Enter the length of base B :> "))

height=int(input("Enter the height of tringle :> "))

area=1/2*base*height

perimeter=side1+side2+base

print(f"Area of the triangle with given base and height=>{area}")

print(f"Perimeter of the triangle with given sides=> {perimeter}")



