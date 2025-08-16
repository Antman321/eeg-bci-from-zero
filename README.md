# 🧠 EEG-BCI from Zero

Prosty projekt **Brain-Computer Interface (BCI)**, który wykorzystuje prawdziwe dane EEG do rozpoznawania wyobrażonych ruchów (np. podniesienie prawej/lewej ręki).  
Projekt powstał w celu nauki pracy z sygnałami biologicznymi oraz budowy portfolio.

---

## ✨ Funkcje
- Wczytywanie prawdziwych danych EEG z plików **.edf** (dataset z PhysioNet).
- Podstawowe przetwarzanie sygnału przy pomocy biblioteki [MNE](https://mne.tools).
- Ekstrakcja prostych cech (średnia, wariancja, pasma fal mózgowych).
- Klasyfikacja z użyciem **scikit-learn** (np. Logistic Regression).
- Prosta wizualizacja sygnałów EEG.
- Struktura repozytorium przygotowana pod rozwój (łatwo można rozbudować o GUI w Streamlit).

---

## 📊 Przykładowe wizualizacje

### Surowy sygnał EEG
![EEG raw signal](assets/eeg_raw.png)

### Wykres widma mocy (Power Spectral Density)
![EEG power spectrum](assets/eeg_psd.png)

### Macierz pomyłek klasyfikatora
![Confusion matrix](assets/confusion_matrix.png)

---

## 📂 Struktura repozytorium
