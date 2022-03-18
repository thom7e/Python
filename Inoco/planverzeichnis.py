from tkinter import *
import os
import datetime
import xlsxwriter


def create_excel():
    root_src_dir = input_field.get()
    ###Excel###
    workbook = xlsxwriter.Workbook(f"{root_src_dir}\\List of Files.xlsx")
    worksheet = workbook.add_worksheet("Index of Content")
    cell_format = workbook.add_format({'bold': True})
    cell_format2 = workbook.add_format({'bold': True, 'font_size': '14'})
    worksheet.write(f'B1', "Description", cell_format2)
    worksheet.write(f'C1', "Archiving Date", cell_format2)
    n = 2
    m = 2
    counter = 0
    for src_dir, dirs, files in os.walk(root_src_dir):  # os.walkthrough
        filename = src_dir.split("\\")[-1]
        print(f"filename: {filename}")
        worksheet.write(f'A{n}', f'{filename}', cell_format)
        n += 1
        m += 1
        for file_ in files:
            date = os.path.getmtime(f"{src_dir}\\{file_}")
            v = datetime.datetime.fromtimestamp(date)
            x = v.strftime('%Y\\%m\\%d')
            print(f"File \"{file_}\" from {x}")
            worksheet.write(f'B{n}', f'{file_}')
            n += 1
            worksheet.write(f'C{m}', f'{x}')
            m += 1
            counter += 1
    #worksheet.write(f"Sum of Files: {counter}")
    workbook.close()



def create_txt():
    root_src_dir = input_field.get()
    counter = 0
    with open(f"{root_src_dir}\\index_of_contents.txt", "w") as file:
        for src_dir, dirs, files in os.walk(root_src_dir):  # os.walkthrough
            filename = src_dir.split("\\")[-1]
            file.write(f"Directory: {filename}\n\n")
            print(f"Dir: {filename}")
            for file_ in files:
                date = os.path.getmtime(f"{src_dir}\\{file_}")
                v = datetime.datetime.fromtimestamp(date)
                x = v.strftime('%Y\\%m\\%d')
                # src_file = os.path.join(src_dir, file_)
                file.write(f"File \"{file_}\" from {x} \n")
                print(f"File \"{file_}\" from {x}")
                counter += 1
            file.write("\n\n")
        file.write(f"Sum of Files: {counter}")

# Ein Fenster erstellen
fenster = Tk()
# Fenstertitel erstellen
fenster.title("InoCo - Index of Contents")

# Fenster stellen
my_label = Label(fenster, text="Copy the Path in here", padx=120)

# Hier macht der Benutzer seine Eingabe
input_field = Entry(fenster, bd=5, width=40)

excel_button = Button(fenster, text="Create Excel-file", command=create_excel, pady=5)
txt_button = Button(fenster, text="Create Text-file", command=create_txt, pady=5)
exit_button = Button(fenster, text="Close", command=fenster.quit, pady=5)

# Nun fügen wir die Komponenten unserem Fenster in der gewünschten Reihenfolge hinzu
my_label.pack()
input_field.pack()
txt_button.pack()
excel_button.pack()

exit_button.pack()
fenster.bind('<Return>', create_excel)
fenster.bind('<Return>', create_txt)
excel_button.focus_set()

# In der Ereignissschleife auf Eingabe des Benutzers warten
fenster.mainloop()