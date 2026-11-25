def km_to_m(km):
    return km * 1000

def kg_to_g(kg):
    return kg * 1000

def m_to_cm(m):
    return m * 100

print("UNIT CONVERTER")
print("1. Kilometers to Meters")
print("2. Kilograms to Grams")
print("3. Meters to Centimeters")

choice = int(input("Enter choice: "))

if choice == 1:
    km = float(input("Enter kilometers: "))
    print("Meters:", km_to_m(km))

elif choice == 2:
    kg = float(input("Enter kilograms: "))
    print("Grams:", kg_to_g(kg))

elif choice == 3:
    m = float(input("Enter meters: "))
    print("Centimeters:", m_to_cm(m))

else:
    print("Invalid choice")