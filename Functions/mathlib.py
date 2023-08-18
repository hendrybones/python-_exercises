
def calculate_area(dimension1,dimension2,shape="triangle"):
    if shape =="triangle":
        area=1/2*(dimension1*dimension2)
    elif shape == "rectangle":
        area = dimension1 * dimension2
    else:
        print("Error inpun neither triangle or rectangle")
        area=None
    return area
a=calculate_area(2,4)
print(a)


    #pattenr
def patternz(n=5):
    for i in range(n):
        s = ''
    for j in range(i + 1):
        s = s + '* '
    print(s)


def calc_area(base, height):
    area = (1/2)*base*height
    return area
a=calc_area(2,2)
print(a)

bas=int(input("Enter base: "))
he=int(input("Enter height: "))
area = (1/2)*bas*he
print("Area of the traingle: ",area)
# rectangle
height=int(input("Enter height: "))
width=int(input("Enter width: "))
rectangle=height* width
print("Area of rectangle",rectangle)