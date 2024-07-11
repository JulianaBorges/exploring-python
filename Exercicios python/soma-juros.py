#entrada dos valores
valor = float(input('Qual o valor do desposito? '))
anos  = int(input('qual a quantidade de ano? ') )
taxa = float(input('qual a taxa? '))

#calculo dos valores
juros = valor * (taxa/100)* anos 

#saida do resultado 
print(f'Seu rendimento será : R${juros: .2f}')