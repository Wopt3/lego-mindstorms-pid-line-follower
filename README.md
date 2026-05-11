# LEGO Mindstorms PID Line Follower

Projekt przedstawiający robota mobilnego LEGO Mindstorms, który podąża za wyznaczoną trasą z wykorzystaniem regulatora PID oraz czujnika koloru.

## Cel projektu

Celem projektu było stworzenie robota, który potrafi samodzielnie poruszać się po trasie, analizując odcień powierzchni za pomocą czujnika koloru.

## Zasada działania

Robot odczytuje wartości z czujnika koloru, porównuje je z wartością zadaną, a następnie oblicza błąd regulacji. Na podstawie tego błędu regulator PID wyznacza korektę prędkości silników, dzięki czemu robot może skręcać w odpowiednią stronę i utrzymywać się na wyznaczonej trasie.


## Funkcjonalności

- odczyt danych z czujnika koloru,
- analiza odcienia powierzchni,
- obliczanie błędu regulacji,
- sterowanie silnikami robota,
- implementacja regulatora PID,
- dostrajanie parametrów Kp, Ki i Kd.

## Technologie

- Python
- LEGO Mindstorms
- czujnik koloru
- regulator PID

