"""
Cololwiek
"""

DAWID = {'imie' : 'Dawid', 'wiek' : 22}
JAN = {'imie' : 'Dawid', 'wiek' : 22}

UCZESTNICY = [DAWID, JAN]

for UCZESTNIK in UCZESTNICY:
    for key, value in UCZESTNIK.items():
        print(key, value)
