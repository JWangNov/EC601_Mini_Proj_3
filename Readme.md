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

wave is Python's standard module for processing WAV files. 
Calling wave.open to open the wav file returns an instance of the Wave_read class.

### matplotlib.pyplot

Matplotlib is a 2D plotting library on python that can generate 
plots, histograms, histograms, error plots, scatter plots, etc.

### numpy

Numpy is a library for the Python programming language, 
adding support for large, multi-dimensional arrays and matrices, 
along with a large collection of high-level mathematical functions to operate on these arrays.

In this demo, we use the fft () function in numpy to implement a fast Fourier transform, 
thereby converting the time domain signal of the audio file into a frequency domain signal.

The Fast Fourier Transform (FFT) is a fast algorithm for computing the discrete Fourier transform. 
It can greatly reduce the number of multiplications required by the computer to calculate the discrete Fourier transform. 
In particular, 
the more sample points N are transformed, The more significant the computational savings of the fast Fourier transform algorithm are.
