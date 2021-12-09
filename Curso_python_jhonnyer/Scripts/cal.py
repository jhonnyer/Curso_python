n1=float(input("Ingresa el primer numero: "))
n2=float(input("Ingresa el primer numero: "))

while(True):
    print("""Elige una opcion de lo que quieras realizar
    1) Sumar los dos numeros:
    2) Restar los dos numeros ingresados: 
    3) Multiplicar los dos numeros
    4) Salir de la aplicación """)
    opcion=input("Ingresa una opción: ")
    if opcion=="1":
        print("La suma de: ",n1," + ",n2," es: ",n1+n2)
    elif opcion=="2":
        print("La resta de: ",n1," - ",n2," es: ",n1-n2)
    elif opcion=="3":
        print("La multiplicacion de: ",n1," * ",n2," es: ",n1*n2)
    elif opcion=="4":
        print("Hasta luego")
        break
    else:
        print("Comando desconocido, vuelve a ingresar una opción nuevamente")
