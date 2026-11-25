def km_to_m(km):
    return km * 1000


def kg_to_g(kg):
    return kg * 1000


def m_to_cm(m):
    return m * 100


def cm_to_mm(cm):
    return cm * 10


def main():
    print("UNIT CONVERTER")
    print("1. Kilometers to Meters")
    print("2. Kilograms to Grams")
    print("3. Meters to Centimeters")
    print("4. Centimeters to Millimeters")

    choice = int(input("Enter choice: "))
    val = float(input("Enter value: "))

    if choice == 1:
        print("Result:", km_to_m(val))
    elif choice == 2:
        print("Result:", kg_to_g(val))
    elif choice == 3:
        print("Result:", m_to_cm(val))
    elif choice == 4:
        print("Result:", cm_to_mm(val))
    else:
        print("Invalid choice")


if __name__== "_main_":
    main()