casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento?'))

prestação = casa / (anos * 12)

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos, a prestação será de R${prestação:.2f}.')
print(f'30% do seu salário corresponde a R${salario * 0.30:.2f}.')

if prestação <= salario * 0.30:
     print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
