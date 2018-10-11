from signalTeste import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
#import wave
import time
#import pickle
import peakutils
from peakutils.plot import plot as pplot


#frequências possíveis
freq1 = 1209
freq2 = 1336
freq3 = 1477
freq4 = 697
freq5 = 770
freq6 = 852
freq7 = 941

#soma de freqências - correspondência com as teclas
um = freq4 + freq1
dois = freq4 + freq2
tres = freq4 + freq3
quatro = freq5 + freq1
cinco = freq5 + freq2
seis = freq5 + freq3
sete = freq6 + freq1
oito = freq6 + freq2
nove = freq6 + freq3
zero = freq7 + freq2

#lista das possíveis frequências
numbers = [freq1,freq2,freq3,freq4,freq5,freq6,freq7]

#Lista da soma das frequências 
totals = [zero, um, dois, tres, quatro, cinco, seis, sete, oito, nove]

looping = True


while looping:
	# print("entrou no looping")

	# Frequência e duração
	fs = 44100
	cont = np.linspace(0, 88200, 88200)
	duration = 2  # seconds

	#Gravação de sinal
	dirtySignal = sd.rec(int(duration * fs), samplerate=fs, channels=1)
	sd.wait()
	#time.sleep(1)

	#limpa o sinal -- correção do erro da placa de audio
	dirtySignal = dirtySignal[:,0]
	# sd.play(dirtySignal, fs)
	
	#Objeto da classe para calculo da FFT
	sig = signalMeu()
	freq, t = sig.calcFFT(dirtySignal,fs)

	#Encontrando a posição dos picos
	indexes = peakutils.indexes(t, thres=0.1, min_dist=70)

	#Picos - lista
	peaks_x = peakutils.interpolate(freq,t, ind=indexes)
	print("picos:           ", peaks_x)

	#inicio de lista de picos certos
	anser = []

	#Quando encontrarmos apenas 2 picos adicionar a anser o valor
	if len(peaks_x) == 2:
		for i in numbers:
			if abs(i - peaks_x[0]) < 2:
				anser.append(i)
			elif abs(i - peaks_x[1]) < 2:
				anser.append(i)

		#somar os valores para fazer a comparação
		total = anser[0] + anser[1]

		#Confere para ver se o valor obtido na soma é um valor que existe na lista de números e printa o número encontrado.
		if total in totals:
			tecla = totals.index(total)
			print("Tecla pressionad:     ", tecla)

			#Gráfico do sinal sonoro recebido
			plt.plot(cont,dirtySignal)
			plt.title("Sinal recebido")
			plt.show()

			#Plota o gráfico com as frequências e os picos 
			pplot(freq, t, indexes)
			plt.title('Frequências')
			plt.show()

			#Tudo certo podemos sair do loop
			looping = False



