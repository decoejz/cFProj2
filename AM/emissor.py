import sys
from signalTeste import *
from funcoes import *
import sounddevice as sd
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd

freq = 13000
amplitude = 5
time = 2 #seconds
fs = 44100

#####AUDIO INICIAL######
# data, samplerate = sf.read('portadora.wav')
print('Comecou a gravar')
gravado = sd.rec(int(time * fs), samplerate=fs, channels=1)
sd.wait()
print('Acabou de gravar')

cont = np.linspace(0, 88200, 88200)
plt.plot(cont,gravado)
plt.title('Sinal de áudio original')
plt.show()

#####NORMALIZANDO AUDIO INICIAL######
normalizado = normaliza(gravado)
plt.plot(cont,normalizado)
plt.title('Sinal de áudio normalizado')
plt.show()


###########
sig = signalMeu()
x,s = sig.generateSin(freq, amplitude, time, fs)