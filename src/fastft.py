import numpy as np
import matplotlib.pyplot as plt


def compute_fft(data, dt=.001):
    
    n = len(data)
    fhat = np.fft.fft(data,n)
    PSD = fhat* np.conj(fhat)/n
    freq = (1/(dt*n))*np.arange(n)
    L = np.arange(1,np.floor(n/2),dtype='int')
    return PSD, freq, L




if __name__ == '__main__':

    dt = .001
    t = np.arange(0,1,dt)
    f = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t)
    f = f + 2.5*np.random.randn(len(t))

    filepath = '/home/devin/Documents/Galvanize/repos/Human-activity-recognition-using-smartphone-data/data/RawData/acc_exp13_user07.txt'
    arr = np.loadtxt(filepath)
    x = arr[10000:12000,[2]]
    PSD, freq, L = compute_fft(f)
    PSD2, freq2,L2 = compute_fft(x)
    fig, ax = plt.subplots(nrows=2, ncols=1)
    # ax[0].plot(freq[L], PSD[L])
    ax[1].plot(PSD2[L2])
    # ax[1].plot(freq2[L2], PSD2[L2])
    # plt.xlim(freq[L[0]],freq[L[-1]])
    plt.show()