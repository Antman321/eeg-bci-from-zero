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

---

## Instalacja

1. Sklonuj repozytorium:

```bash
git clone https://github.com/TWOJ_LOGIN/EEG-BCI-from-zero.git
cd EEG-BCI-from-zero

2. Utwórz i aktywuj wirtualne środowisko:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

3. Zainstaluj zależności:

pip install -r requirements.txt

