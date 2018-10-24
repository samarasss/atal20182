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

# Caso o valor não possa ser alcançado pela combinação de moedas o valor -1 é retornado Ex: valor = 11  moedas = {5, 10, 25}
# Assuma que existe uma quantidade infinita de cada tipo de moeda


global resp
resp = sys.maxint

def retorna_minimo_moedas(valor, tipos_moedas):
    global resp
    resp = sys.maxint
    print(valor, tipos_moedas)
    tipos_moedas.sort(reverse = True)
    resultado = retorna_minimo_moedas_FB(tipos_moedas, valor, 0)

    if resultado == sys.maxint or resultado == None:
        return -1
    else:
        return resultado

def retorna_minimo_moedas_FB(tipos_moedas, valor,quantidadeMoedas):
  	if valor == 0:
		return 0
	
	resultado = sys.maxint
	
	contador = 0;
	
	for i in range(0, len(tipos_moedas)):
		if (valor >= tipos_moedas[i] and quantidadeMoedas < resp):
			return retorna_minimo_moedas_FB(tipos_moedas, (valor - tipos_moedas[i]), quantidadeMoedas + 1)
		
	return resultado	
