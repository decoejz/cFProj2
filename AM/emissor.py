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
CONT = np.linspace(0, 88200, 88200)

#####AUDIO INICIAL######
# data, samplerate = sf.read('portadora.wav')
print('Comecou a gravar')
data = sd.rec(int(time * fs), samplerate=fs, channels=1)
sd.wait()
print('Acabou de gravar')

plt.plot(CONT,data)
plt.title('Sinal de áudio original')
plt.show()

#####NORMALIZANDO AUDIO INICIAL######
normalizado = normaliza(data)
plt.plot(CONT,normalizado)
plt.title('Sinal de áudio normalizado')
plt.show()

#####AUDIO FILTRADO######
filtrado = passaBaixa(normalizado,fs)
plt.plot(CONT,filtrado)
plt.title('Sinal de áudio filtrado')
plt.show()

#####AUDIO MODULADO######
# modulado = 

#####TOCANDO AUDIO MODULADO######
# sd.play(modulado, fs)
# sd.wait()

###########
# sig = signalMeu()
# x,s = sig.generateSin(freq, amplitude, time, fs)