def area_square(side):
    area = side * side
    return area


def area_rectangle(l,b):
    area =  l * b
    return area

def perimeter_rectangle(a,b):
    perimeter =  2 * (a+b)
    return perimeter

if __name__=="__main__":
    while True:
        print("menu driven program")
        print("area of square")
        print("area of rectangle")
        print("perimeter of rectangle")
        print("exit")
        choice = int(input("enter your choice"))
        if choice == 1:
            side = int(input("enter side"))
            print("area", side * side)

        elif choice == 2:
            length = int(input("enter length"))
            breadth = int(input("enter breadth"))
            print("area", length * breadth)

        elif choice == 3:
            a = int(input("enter number"))
            b = int(input("enter number"))
            print("perimeter", 2 * (a + b))
        elif choice == 4:
            break
        else:
            print("wrong choice")

