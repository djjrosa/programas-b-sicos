tamanho = int(input(" Digite o tamanho da sequ�ncia de n�meros:"))

produto = 1 
i = 0

while i < tamanho:
	valor = int(input(" Digite um valor a ser multiplicado: "))
	produto = produto * valor
	i = i + 1

print(" A multiplica��o dos valores digitados � : ", produto)