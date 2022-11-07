import os
import datetime

print(os.path.getmtime("move.py"))
print(datetime.datetime.fromtimestamp(os.path.getmtime("move.py")))

a = os.path.getmtime("move.py")
b= os.path.getmtime("C:\\Users\\thoma\\OneDrive\\Python\\Datensicherung\\Sicherung Ziegeläcker.py")

print(a,b)

if a > b:
    print("a > b")

if a < b:
    print("a < b")

# > ist gleich neuer