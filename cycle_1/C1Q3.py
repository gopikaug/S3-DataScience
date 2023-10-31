x=int(input("Enter the side(x):"))
y=int(input("Enter the side(y):"))
z=int(input("Enter the side(z):"))
if x==y==z:
    print("Triangle is Equilateral")
elif x==y or y==z or x==z:
    print("Triangle is Isosceles")
else:
    print("Triangle is Scalene")