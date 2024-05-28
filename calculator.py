# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Pas possible de diviser par 0")
    return a / b

def main():
    print("Choisie l'opération:")
    print("1. Add")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Entre ton choix (1/2/3/4): ")

    num1 = float(input("Premier nombre : "))
    num2 = float(input("Second nombre: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        try:
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        except ValueError as e:
            print(e)
    else:
        print("Entrée invalide")

if __name__ == "__main__":
    main()
