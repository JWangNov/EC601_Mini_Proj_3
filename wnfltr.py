import wave
import matplotlib.pyplot as plt
import numpy as np

FILE_PATH = r"./dt_n_gnrt/inport.wav"

the_file = wave.open(FILE_PATH, "rb")
voice_channel = the_file.getparams()[0]
voice_sampl_rt = the_file.getparams()[2]
voice_frame = the_file.getparams()[3]
string_wav = the_file.readframes(voice_frame)
the_file.close()

wave_data = np.fromstring(string_wav, dtype=np.short)
wave_data.shape = -1, 2
wave_data = wave_data.T
time = np.arange(0, voice_frame) * (1.0 / voice_sampl_rt)
plt.subplot(211)
plt.plot(time, wave_data[0])
plt.xlabel("time domain")

N=50000
df = voice_frame/(N-1)
freq = [df*n for n in range(0,N)]
wave_data2=wave_data[0][0:N]
c=np.fft.fft(wave_data2)*2/N
plt.subplot(212)
plt.plot(freq[:round(len(freq)/2)],abs(c[:round(len(c)/2)]))
plt.xlabel("freq domain")
plt.show()
