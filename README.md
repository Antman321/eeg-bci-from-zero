# EEG-BCI-from-zero

Projekt edukacyjny pokazujący podstawy pracy z danymi EEG.  
Celem jest stworzenie prostego programu, który może rozpoznawać czynności na podstawie sygnałów EEG, np. podniesienie prawej ręki.

---

## Struktura projektu

EEG-BCI-from-zero/
├── assets/ # folder na wykresy EEG i pliki graficzne
├── src/
│ └── cli.py # przykładowy skrypt generujący wykresy EEG
├── requirements.txt # lista bibliotek Python
└── README.md

yaml
Kopiuj
Edytuj

---

## Instalacja

1. Sklonuj repozytorium:

```bash
git clone https://github.com/TWOJ_LOGIN/EEG-BCI-from-zero.git
cd EEG-BCI-from-zero
Utwórz i aktywuj wirtualne środowisko:

bash
Kopiuj
Edytuj
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
Zainstaluj zależności:

bash
Kopiuj
Edytuj
pip install -r requirements.txt
Uruchomienie przykładowego skryptu
Skrypt src/cli.py generuje przykładowy wykres EEG i zapisuje go do folderu assets/.

bash
Kopiuj
Edytuj
python src/cli.py
Po uruchomieniu w folderze assets/ pojawi się plik eeg_raw.png.
Obrazek można użyć w README lub do dalszej analizy.

Przykładowe użycie w README
markdown
Kopiuj
Edytuj
![EEG raw signal](assets/eeg_raw.png)
Biblioteki
numpy

matplotlib

mne

scikit-learn (opcjonalnie do dalszych eksperymentów)

Cel projektu
Nauka obsługi danych EEG w Pythonie.

Tworzenie prostych wizualizacji sygnałów.

Budowanie portfolio projektów do GitHub.

yaml
Kopiuj
Edytuj
