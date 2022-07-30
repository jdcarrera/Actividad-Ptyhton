# Se hará un programa que realizará la nomina de x empleados, y se guardaran los registros en un archivo txt de manera ordenada

print("Bienvenido Señor@ gerente, a continuación, el programa le pedirá los datos necesarios para realizar la nómina de sus empleados \n")
lim=int(input("¿cuantos registros desea imprimir? \n"))

for i in range (lim):
    
    document=int(input("Ingrese su numero de documento, sin puntos ni comas, ni espacios \n"))
    names=(input("Escriba los nombres del empleado \n"))
    lastname=(input("Escriba sus apellidos \n"))
    salary=float(input("Digite su salario base \n"))
    days_Worked= int(input("¿Cuantos dias ha trabajado en el mes? \n"))
    
    finalSalary= (salary/30)*days_Worked
    print("Su salario basico es: $ "+ str(finalSalary))

    epsAndPension= finalSalary*0.08
    salary_epsandP=finalSalary-epsAndPension

    print("El salario menos eps y pension, es de: $"+ str(salary_epsandP))

    if finalSalary<=2000000:
        subsidy_T= (117100/30)*days_Worked
        transport_subsidy= finalSalary+subsidy_T
        print("El salario final con el subsidio de transporte es de: $"+str(transport_subsidy))
    else:
        finalSalary>2000000
        print("El salario final sin subsidio de transporte es de: $"+str(finalSalary))

    with open ("registersnom.txt", "a") as register:
        register.write("\nDocumento: " + str(document))
        register.write("\nNombres: " + str(names))
        register.write("\nApellidos: " + str(lastname))
        register.write("\nSalario final: $" + str(finalSalary))
        register.write("\nDias Trabajados: " + str(days_Worked))
        register.write("\n")