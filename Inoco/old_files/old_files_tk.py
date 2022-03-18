from tkinter import *
import os
import datetime
import shutil


def dateien_verschieben():
    root_src_dir = input_field.get()
    year = input_field2.get()
    counter = 0
    alte_dateien = f"{root_src_dir}\\old_files"
    if not os.path.exists(alte_dateien):
        os.mkdir(alte_dateien)

    for src_dir, dirs, files in os.walk(root_src_dir):  # os.walkthrough
        filename = src_dir.split("\\")[-1]
        print(f"filename: {filename}")
        for file_ in files:
            date = os.path.getmtime(f"{src_dir}\\{file_}")
            v = datetime.datetime.fromtimestamp(date)
            x = v.strftime('%Y\\%m\\%d')
            if x < str(year):
                if os.path.samefile(f"{src_dir}\\{file_}", alte_dateien):
                    continue
                # print(f"File \"{file_}\" from {x}")

                shutil.copy(f"{src_dir}\\{file_}", alte_dateien)
                os.remove(f"{src_dir}\\{file_}")

                counter += 1

    print(counter)
    print("hey")


# Ein Fenster erstellen
fenster = Tk()
# Fenstertitel erstellen
fenster.title("Alte Dateien verschieben")

# Fenster stellen
my_label = Label(fenster, text="Bitte den Pfad eingecben", padx=120)
my_label2 = Label(fenster, text="Bitte das Jahr eingeben", padx=120)

# Hier macht der Benutzer seine Eingabe
input_field = Entry(fenster, bd=5, width=40)
input_field2 = Entry(fenster, bd=5, width=40)


excel_button = Button(fenster, text="Dateien verschieben", command=dateien_verschieben(), pady=5)
exit_button = Button(fenster, text="Close", command=fenster.quit, pady=5)

# Nun fügen wir die Komponenten unserem Fenster in der gewünschten Reihenfolge hinzu
my_label.pack()
input_field.pack()
my_label2.pack()
input_field2.pack()
excel_button.pack()
exit_button.pack()
fenster.bind('<Return>', dateien_verschieben())
excel_button.focus_set()

# In der Ereignissschleife auf Eingabe des Benutzers warten
fenster.mainloop()