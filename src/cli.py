import os
import numpy as np
import matplotlib.pyplot as plt

# 1. Tworzymy folder assets jeśli nie istnieje
assets_folder = os.path.join(os.path.dirname(__file__), '..', 'assets')
os.makedirs(assets_folder, exist_ok=True)

# 2. Generujemy przykładowy sygnał EEG
t = np.arange(0, 10, 0.01)  # 10 sekund, próbka co 0.01s
eeg_signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.random.randn(len(t))  # sine wave + szum

# 3. Rysujemy wykres
plt.figure(figsize=(10, 4))
plt.plot(t, eeg_signal)
plt.title("Przykładowy sygnał EEG")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.grid(True)

# 4. Zapisujemy wykres do folderu assets
output_file = os.path.join(assets_folder, "eeg_raw.png")
plt.savefig(output_file)
plt.close()

print(f"Wykres zapisany w {output_file}")
