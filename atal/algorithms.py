#coding: utf-8

import sys

# Esse metodo recebe uma lista com as matriculas dos alunos
# e retorna essa lista em ordem crescente de matriculas
def retorna_matriculas_decrescente(alist):
	for j in xrange(len(alist)):
		for i in xrange(len(alist)-1):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
	return alist

# Esse metodo recebe e valor para ser dado o troco e uma lista com os tipos de moedas possiveis
# e retorna o numero minimo de moedas possiveis em que o troco pode ser dado
#
# Caso o valor não possa ser alcançado pela combinação de moedas o valor -1 é retornado Ex: valor = 11  moedas = {5, 10, 25}
# Assuma que existe uma quantidade infinita de cada tipo de moeda
def retorna_minimo_moedas(valor, tipos_moedas):
	print valor, tipos_moedas
	resultado = retorna_minimo_moedas_FB(tipos_moedas, valor)
	if resultado == sys.maxint:
		return -1
	else:
		return resultado

def retorna_minimo_moedas_FB(tipos_moedas, valor):
	if valor == 0:
		return 0
	
	resultado = sys.maxint
	
	for moeda in tipos_moedas:
		
		if (moeda <= valor):
			resultado = min(resultado, retorna_minimo_moedas_FB(tipos_moedas, valor - moeda) + 1) 
		
	return resultado	 

# Mochila Binaria interativo
  
# Retorna o valor maximo que cabe na mochila com 
# capacidade peso_maximo
def mochila_binaria(peso_maximo, pesos, valores, n): 
  
	# criar matriz
	
	matriz = [[0] * (peso_maximo + 1) for _ in range(n + 1)]
	
	
	for i in range(1, len(matriz)):
		for j in range(1, len(matriz[i])):
			if i == 0:
				matriz[i][j] = 0
			elif j == 0:
				matriz[i][j] = 0
			elif pesos[i-1] > j:
				matriz[i][j] = matriz[i-1][j]
			else:
				matriz[i][j] = max(matriz[i-1][j - pesos[i-1]] + valores[i-1], matriz[i-1][j])
	
	return matriz[n][peso_maximo]
