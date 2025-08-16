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

## 📂 Struktura repozytorium
EEG-BCI-from-Zero/
├── data/ # przykładowe pliki EEG (.edf)
├── notebooks/ # Jupyter Notebook z analizą danych
├── src/ # kod źródłowy
│ ├── preprocess.py # obróbka sygnału
│ ├── features.py # ekstrakcja cech
│ ├── classifier.py # trenowanie i ewaluacja
│ └── cli.py # prosty interfejs wiersza poleceń
├── requirements.txt # wymagane biblioteki
└── README.md # dokumentacja projektu

---

## ⚙️ Instalacja i uruchomienie

### 1. Klonowanie repozytorium
```bash
git clone https://github.com/<Twoj-Login>/eeg-bci-from-zero.git
cd eeg-bci-from-zero
![EEG raw signal](assets/eeg_raw.png)
