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
amplitude = 1
freqP = 14000
duration = 5  # seconds
time = 5
port = signalMeu()
x, Port = port.generateSin(freqP, amplitude, time, fs)
sd.default.channels = 1
sd.default.samplerate = fs


#while looping:

#Gravação de sinal
print('Vai começar a gravar')
dirtySignal = sd.rec(int(duration * fs))
sd.wait()
print('Acabou de gravar')
#time.sleep(1)

#limpa o sinal -- correção do erro da placa de audio
dirtySignal = dirtySignal[:,0]

#Demodulando o sinal

demod = dirtySignal*Port #np.multiply(dirtySignal,Port)
demod = passaBaixa(demod,fs)

#Objeto da classe para calculo da FFT
sig = signalMeu()
freqS, tS = sig.calcFFT(dirtySignal,fs)
print("frequencias:     ",tS)

#Encontrando a posição dos picos
indexesS = peakutils.indexes(tS, thres=3, min_dist=70)

#Picos - lista
peaks_xS = peakutils.interpolate(freqS,tS, ind=indexesS)
print("picos:           ", peaks_xS)

#for p in freq:
	#if abs(13000 - p) < 200:
print("entrou no if")


freq, t = sig.calcFFT(demod,fs)
#Encontrando a posição dos picos
indexes = peakutils.indexes(t, thres=3, min_dist=70)

#Picos - lista
peaks_x = peakutils.interpolate(freq,t, ind=indexes)
print("picos:           ", peaks_x)

#Gráfico do sinal sonoro recebido
plt.plot(dirtySignal)
plt.title("Sinal recebido (tempo)")
plt.show()

#Plota o gráfico com as frequências e os picos 
pplot(freqS, tS, indexesS)
plt.title('Sinal recebido (Frequências)')
plt.show()

#Gráfico do sinal sonoro recebido
plt.plot(demod)
plt.title("Sinal demodulado (tempo)")
plt.show()

#Plota o gráfico com as frequências e os picos 
pplot(freq, t, indexes)
plt.title('Sinal demodulado (Frequências)')
plt.show()

print("começou a emitir")
sd.play(demod)
sd.wait()
print("terminou a emissão")
#break
			