def normaliza(sinal):
	maior = abs(max(sinal))
	menor = abs(min(sinal))
	if menor > maior:
		maior = menor
	
	resultado = []
	for i in sinal:
		resultado.append(i/maior)
	
	return(resultado)