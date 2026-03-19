#Banner
print("#####################################")
print("             Dateiscanner            ")
print("Just type the Directory to your file ")
print("#####################################")

untersuchen = str(input("Enter the File Path: "))

print("\n")

#Extrahiert die ersten 2 bytes der datei
try:
    with open(untersuchen, 'rb') as datei:
        magic = datei.read(2)
except FileNotFoundError:
    print("File does not exist!")
    print("Check the File Path")
    exit()

zwei = 1

#findet die endung herus die der Nutzer sieht.
dateiname = untersuchen.split('/')[-1]
if '.' in dateiname:
    endungen = dateiname.split('.')[1:]
    endungv = endungen[-1] if endungen else ""
    print(f"Filename: {dateiname}")
    print(f"Found endings: {endungen}")
    if len(endungen) > 1:
        zwei = 2
else:
    print("The file has no extension!")
    endungen = []
    endungv = ""

#Bestimmt anhand des datei types und dem anzeige namen ob es potenziel gefährlich ist.
if magic == b'MZ':
    print("The File es a .exe file!")

    if endungv.lower() == "exe":
        print("But doesnt try to hide it!")
        print("Do YOU trust the source of your exe file?")
    else:
        print("       -        ")
        print("     -   -      ")
        print("    -  |  -     ")
        print("   -   |   -    ")
        print("  -    O    -   ")
        print(" - - - - - - -  ")

        print("The .exe file tries to hide his file type!")
        print(f"By changing its ending to", endungv, "!")
        print("You shouold not execute it!")

        if zwei == 2:
            print("The File also tries to hide by putting")
            print("a file type in the name of the file in the hope that")
            print("the user only sees the file type in the name and not the .exe")
            print("Be very careful with this file")
    
else:
    print("The file is not a .exe file")
    print("You should still be very conscious!")
    print("If the file is from a non trusted source!")
