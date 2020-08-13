import numpy as np
import matplotlib.pyplot as plt

dt = .001
t = np.arange(0,1,dt)
f = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t)
f = f + 2.5*np.random.randn(len(t))
filepath = '/home/devin/Documents/Galvanize/repos/Human-activity-recognition-using-smartphone-data/data/RawData/acc_exp13_user07.txt'
arr = np.loadtxt(filepath)
# f = arr[:,[1]]
f2 = arr[8013:9170,[2]]
n = len(t)
fhat = np.fft.fft(f,n)
PSD = fhat* np.conj(fhat)/n
freq = (1/(dt*n))*np.arange(n)
L = np.arange(1,np.floor(n/2),dtype='int')


indices = PSD>100
PSDclean = PSD *indices
fhat = indices * fhat
ffilt = np.fft.ifft(fhat)


fig, ax = plt.subplots(nrows=2,ncols=1)
ax[0].plot(freq[L], PSD[L])
ax[1].plot()
# plt.xlim(freq[L[0]],freq[L[-1]])
plt.show()