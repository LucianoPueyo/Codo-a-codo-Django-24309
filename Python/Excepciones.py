continuar = True
while continuar:
    try:
        #a = 7 / 0
        print("Ingrese dos numeros para ser divididos")
        a = int(input("> "))
        b = int(input("> "))

        print(a / b)

        continuar = False

    except ValueError:
        print("Solo se pueden ingresar numeros")

    except ZeroDivisionError:
        print("El usuario intentó dividir por 0")

    except:
        print("Ups ocurrio un error")

print("Adios")