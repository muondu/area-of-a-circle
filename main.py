import time
radious = int(input("Enter your radious: "))
def area_of_circle(radius):
    area = radius * radious * 3.142
    print("Calculating area...")
    time.sleep(2)
    return area
circle = area_of_circle(radious)
c = str(circle)
print("The area of the circle is " + c)