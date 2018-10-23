from signalTeste import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
#import wave
import time
#import pickle
import peakutils
from peakutils.plot import plot as pplot
import soundfile as sf
from funcoes import *


looping = True

# Frequência e duração
fs = 44100
cont = np.linspace(0, 88200, 88200)
amplitude = 1
freqP = 13000
duration = 20  # seconds
time = 10
port = signalMeu()
P = port.generateSin(freqP, amplitude, time, fs)


while looping:

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
	indexes = peakutils.indexes(t, thres=3, min_dist=70)

	#Picos - lista
	peaks_x = peakutils.interpolate(freq,t, ind=indexes)
	print("picos:           ", peaks_x)

	for p in peaks_x:
		if abs(13000 - p) < 20:
			demod = dirtySignal * P
			demod = passaBaixa(demod)
			