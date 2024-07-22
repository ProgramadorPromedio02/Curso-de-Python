num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

try: 
    resultado = num1 / num2
    print(f"{num1} / {num2} =", resultado)
except ZeroDivisionError as e:
    print(e)
else:
    print("Else")
finally:
    print("Finally")


