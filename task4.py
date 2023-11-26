class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcArea(self):
        return round(1.5 * 1.732 * self.side_length, 2)

    def calcPeri(self):
        return 6 * self.side_length

    def calcAngleSum(self):
        return 6 * 120

    def display(self):
        print("Area of Hexagon:", self.calcArea())
        print("Perimeter of Hexagon:", self.calcPeri())
        print("Sum of angles of Hexagon:", self.calcAngleSum())


class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcAreaSquare(self):
        return self.side_length ** 2

    def calcPeriSquare(self):
        return 4 * self.side_length

    def display(self):
        print("Area of Square:", self.calcAreaSquare())
        print("Perimeter of Square:", self.calcPeriSquare())


def get_last_digit_cnic():
    cnic = input("Enter your CNIC number: ")
    last_digit = cnic[-1]
    return int(last_digit)


def main():
    last_digit = get_last_digit_cnic()

    hexagon_side_length = last_digit
    square_side_length = last_digit + 1

    hexagon = Hexagon(hexagon_side_length)
    square = Square(square_side_length)

    while True:
        print("Menu:")
        print("1. Calculate properties of Hexagon")
        print("2. Calculate properties of Square")
        print("Enter any other key to exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            hexagon.display()
        elif choice == '2':
            square.display()
        else:
            print("Exiting the program.")
            break


if __name__ == "__main__":
    main()
