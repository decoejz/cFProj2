from scipy import signal

def normaliza(sinal):
	maior = abs(max(sinal))
	menor = abs(min(sinal))
	if menor > maior:
		maior = menor
	
	resultado = []
	for i in sinal:
		resultado.append(i/maior)
	
	return(resultado)

def passaBaixa(sinal,fs):
	#exemplo de filtragem do sinal yAudioNormalizado
	# https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
	nyq_rate = fs/2
	width = 5.0/nyq_rate
	ripple_db = 60.0 #dB
	N , beta = signal.kaiserord(ripple_db, width)
	cutoff_hz = 4000.0
	taps = signal.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
	yFiltrado = signal.lfilter(taps, 1.0, sinal)

	return yFiltrado