# DSP Visualization

Mini Project 3

Jialun Wang



## Modules

### wave

WAV is a sound file format developed by Microsoft. 
Although it supports multiple compression formats, 
it is usually used to store uncompressed sound data (PCM pulse code modulation). 
WAV has three important parameters: 
the number of channels, 
the sampling frequency, 
and the number of quantization bits.

Wave is Python's standard module for processing WAV files. 
It provides a convenient interface to the WAV sound format, 
which support both mono and stereo channels.  
Calling wave.open to open the wav file returns an instance of the Wave_read class.

### matplotlib.pyplot

The Matplotlib license is based on the Python Software Foundation (PSF) license. 
It is a 2D plotting library on python that can generate 
plots, histograms, histograms, error plots, scatter plots, etc.


The Matplotlib license is based on the Python Software Foundation (PSF) license. It is a python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Besides, plots, histograms, bar chart, etc. can be easily generated by its’ modules, called pyplot.

### numpy

Numpy is a library for the Python programming language, 
adding support for large, multi-dimensional arrays and matrices, 
along with a large collection of high-level mathematical functions to operate on these arrays.

In this demo, we use the fft () function in numpy to implement a fast Fourier transform, 
thereby converting the time domain signal of the audio file into a frequency domain signal.

### Fast Fourier Transform (FFT)

![FFT](https://github.com/JWangNov/EC601_Mini_Proj_3/blob/master/FFT.jpg)

The Fast Fourier Transform FFT is a more efficient algorithm for computing discrete Fourier transforms. 
It has a computational complexity of O(N log_2 N), 
which is more scalable than the original Discrete Fourier Transform (DFT) O(N^2) computational complexity.
It can greatly reduce the number of multiplications required by the computer to calculate the discrete Fourier transform. 
In particular, 
the more sample points N are transformed, The more significant the computational savings of the fast Fourier transform algorithm are.

### Discrete Fourier Transform (DFT)

The discrete Fourier transform is a discrete form of the Fourier transform in both the time domain and the frequency domain. 
The time domain sampling of the signal is transformed into the frequency domain sampling of the DTFT. 
Formally, the sequences at both ends of the transformation (in the time and frequency domains) are finite in length, 
but in fact, both sets of sequences should be considered as the main value sequence of discrete periodic signals. 
Even if DFT is performed on a discrete signal of finite length, 
it should be regarded as a transformation of its periodic extension. 
In practice, the DFT is usually calculated using a fast Fourier transform.

### AudioLazy

![adlzplt.png](https://github.com/JWangNov/EC601_Mini_Proj_3/blob/master/adlzplt.png)

AudioLazy is a module which can perform Z-transfrom, 
including linear time variant filters, cascade filters (behaves as a list of filters), resonators, etc.. 
In this module, each LinearFilter instance is compiled just in time when called



## Another Choice of Reading Audio Files

### Id3reader

MP3 is also a very popular audio format. 
It is designed to greatly reduce the amount of audio data. 
By discarding the part of PCM audio data that is not important to human hearing, 
it achieves the purpose of compression into smaller files.

Using wave to process mp3 format files will cause reading errors, 
while id3reader is a relatively unpopular but practical module that can be used to read and analyze mp3 format audio files.



## Audio Visualization Result

![result1](https://github.com/JWangNov/EC601_Mini_Proj_3/blob/master/Figure_1.png)

In this experiment, by using the wave module, we can read and processing the wav file (in which the .wav file saved in binary form). 
Then, we can use NumPy to perform FFT, to get frequency domain signal in addition to time domain signal. 
After that, we can use pyplot to transform discrete signals into picture form to visualize digital signals.



## Comparison between DFT and FFT

In this experiment, we take the following picture as an example.

![example](https://github.com/JWangNov/EC601_Mini_Proj_3/blob/master/eg.png)

Next, we perform discrete Fourier transform and fast Fourier transform on this graph, and generate the analysis result graph. 
During the analysis, it can be felt that the time required for the discrete Fourier transform of the picture is slightly longer 
than the time required for the fast Fourier transform. 
The results obtained are as follows.

***DFT***
![DFT](https://github.com/JWangNov/EC601_Mini_Proj_3/blob/master/eg_DFT.png)

***FFT***
![FFT](https://github.com/JWangNov/EC601_Mini_Proj_3/blob/master/eg_FFT.png)

We can see from the frequency amplitude map that we obtained that there is not much difference 
in the calculation accuracy of the two methods. 
Therefore, in practical applications, we can consider using FFT to implement DSP in a shorter time.

Here are more detailed results of our Fast Fourier Transform on the example picture. 
We can create a low-pass filter and a high-pass filter respectively to get the high-frequency and low-frequency parts of the image. 
The two filters and the filtering results are shown in the figure.

![Filter](https://github.com/JWangNov/EC601_Mini_Proj_3/blob/master/egIFFT.png)
