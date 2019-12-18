import wave
import matplotlib.pyplot as plt
import numpy as np
# import audiolazy as lz

import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot,init_notebook_mode
import cufflinks
cufflinks.go_offline(connected=True)


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

# SYNTH_ADSR_PARAMS = dict(a=40*ms, d=20*ms, s=.7, r=50*ms)
# SYNTH_DURATION = .4 * s
# SYNTH_ENVELOPE = list(lz.adsr(SYNTH_DURATION, **SYNTH_ADSR_PARAMS) * .55)
# SYNTH_PAUSE_AT_END = lz.zeroes(.25 * s).take(lz.inf)
# synth_table = lz.sin_table.harmonize(dict(enumerate([.1, .15, .08, .05, .04, .03, .02])))
# (1 + z ** -2).plot().show()

trace0 = go.Scatter( x = time, y = wave_data[0], mode = 'markers', name = 'time domain') 
trace1 = go.Scatter( x = freq[:round(len(freq)/2)], y = abs(c[:round(len(c)/2)]), mode = 'markers', name = 'freq domain') 
data = [trace0, trace1]
py.iplot(data, filename='scatter-mode')
