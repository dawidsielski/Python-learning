import os

script_path = os.path.dirname(os.path.abspath(__file__))

filename = "baza.txt"


# możesz dać w to bedzie write czyli nadpisze przy każdym odpaleniu wszystko
# możesz dać a to wtedy bedzie dodawać do końca pliku
with open(os.path.join(script_path, filename), "a") as f:
    f.writelines("wpisz do pliku\n")
    f.writelines("wpisz do pliku\n")
    f.writelines("wpisz do pliku\n")
