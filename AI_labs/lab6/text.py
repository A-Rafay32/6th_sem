import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

freq_samp, aud = wavfile.read('Audio_car.wav')

print('Signal Shape', aud.shape)
print("Signal Dtype",aud.dtype)
print("Signal Duration",round(aud.shape[0]/float(freq_samp),2),'seconds')

aud = aud / np.power(2,15)
aud = aud[:100]
time_axis = 1000*np.arange(0, len(aud),1) / float(freq_samp)

plt.plot(time_axis, aud, color = 'b')
plt.xlabel("milliseconds")
plt.ylabel('Amplitude')
plt.title("Input audio signal")
plt.show()