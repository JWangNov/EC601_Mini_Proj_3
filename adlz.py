from audiolazy.lazy_stream import Stream
from audiolazy import Stream

a = Stream(2, -2, -1) # Periodic
b = Stream(3, 7, 5, 4) # Periodic
c = a + b # Elementwise sum, periodic
c.take(15) # First 15 elements from the Stream object
[5, 5, 4, 6, 1, 6, 7, 2, 2, 9, 3, 3, 5, 5, 4]

a = Stream([1, 2, 3, 2, 1]) # Finite, since it's a cast from an iterable
b = Stream(3, 7, 5, 4) # Periodic
c = a + b # Elementwise sum, finite
list(c)
[4, 9, 8, 6, 4]

filt = 1 - z ** -1 # Diff between a sample and the previous one
filt
1 - z^-1
data = filt([.1, .2, .4, .3, .2, -.1, -.3, -.2]) # Past memory has 0.0
data # This should have internally [.1, .1, .2, -.1, -.1, -.3, -.2, .1]
data *= 10 # Elementwise gain
[int(round(x)) for x in data] # Streams are iterables
[1, 1, 2, -1, -1, -3, -2, 1]
data_int = filt([1, 2, 4, 3, 2, -1, -3, -2], zero=0) # Now zero is int
list(data_int)
[1, 1, 2, -1, -1, -3, -2, 1]
