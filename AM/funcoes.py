from scipy import signal
from signalTeste import *
import numpy as np
import matplotlib.pyplot as plt
import peakutils
from peakutils.plot import plot as pplot

sig = signalMeu()

def normaliza(sinal):
	maior = abs(max(sinal))
	menor = abs(min(sinal))
	if menor > maior:
		maior = menor
	resultado = sinal/maior
	# resultado = []
	# for i in sinal:
	# 	resultado.append(i/maior)
	
	return(resultado)

def passaBaixa(sinal,fs):
	#exemplo de filtragem do sinal yAudioNormalizado
	#https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
	nyq_rate = fs/2
	width = 5.0/nyq_rate
	ripple_db = 60.0 #dB
	N , beta = signal.kaiserord(ripple_db, width)
	cutoff_hz = 4000.0
	taps = signal.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
	yFiltrado = signal.lfilter(taps, 1.0, sinal)
	
	return(yFiltrado)

def modula(sinal,freq,tempo,fs):
	k = 0
	x,multiplicado = sig.generateSin(freq,5,tempo,fs)
	modulado = np.multiply(sinal,multiplicado) + k * multiplicado

	return(modulado)

def plotandoFreq(sinal,fs):
	# sinal = sinal[:,0]
	freq, t = sig.calcFFT(sinal,fs)
	#Encontrando a posição dos picos
	indexes = peakutils.indexes(t, thres=3, min_dist=70)
	#Picos - lista
	peaks_x = peakutils.interpolate(freq,t, ind=indexes)
	pplot(freq, t, indexes)
	plt.title('Furier')
	plt.show()