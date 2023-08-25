import numpy as np
import matplotlib.pyplot as plt

# Generate a sample signal
sampling_rate = 1000  # Hz
duration = 1  # seconds
t = np.linspace(0, duration, sampling_rate * duration)
frequency1 = 60  # Hz
frequency2 = 120  # Hz
signal = np.sin(2 * np.pi * frequency1 * t) + 0.5 * np.sin(2 * np.pi * frequency2 * t)

# Compute FFT
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(fft_result), 1/sampling_rate)
magnitude = np.abs(fft_result)

# Plot the original signal and its FFT
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("Original Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(2, 1, 2)
plt.plot(frequencies, magnitude)
plt.title("FFT of Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

plt.tight_layout()
plt.show()
