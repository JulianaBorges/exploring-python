def calculo_inss(salario_bruto):
    if salario_bruto <= 1100:
        return salario_bruto * 0.075
    elif 1100.01 <= salario_bruto <= 2203.048:
        return salario_bruto * 0.09
    elif 22003.049 <= salario_bruto <= 3305.22:
        return salario_bruto * 0.12
    elif 3305.22 <= salario_bruto <= 6433.57:
        return salario_bruto * 0.14
    else:
        return 751.90

def calculo_irrf(salario_liquido):
    if salario_liquido <= 19903.98:
        return 0 
    elif 19903.99 <= salario_liquido <= 2826.65:
        return (salario_liquido * 0.075) - 142.8
    elif 2826.66 <= salario_liquido <= 3751.05:
        return (salario_liquido * 0.15) - 358.8
    elif 3751.06 <= salario_liquido <= 4664.68:
        return (salario_liquido * 0.225) - 636.13
    else:
        return (salario_liquido * 0.275) - 869.36

def calcular_hora_extra(salario_bruto, horas_extras):
    valor_hora = salario_bruto / 240
    adicional = valor_hora * 0.5
    return horas_extras * (valor_hora * adicional)

salario_bruto = float(input("Salario: R$"))
horas_extras = int(input("Total horas extras: "))

desconto_inss = calculo_inss(salario_bruto)

salario_liquido = salario_bruto - desconto_inss

desconto_irrf = calculo_irrf(salario_liquido)

provento_hora_extra = calcular_hora_extra(salario_bruto, horas_extras)

salario_final = salario_liquido + provento_hora_extra - desconto_irrf


print("\n*** Folha de Salario ***")
print(f"Salário Bruto: RS{salario_bruto:.2f}")
print(f"Provento horas Extra: R${provento_hora_extra:.2f}")
print(f"Descontos INSS: R${desconto_inss:.2f}")
print(f"Descontos IRRF: R${desconto_irrf:.2f}")
print("--------------------------")
print(f"Salario Final: R${salario_final:.2f}")
print("\n")
print("*** Repl Closed ***")