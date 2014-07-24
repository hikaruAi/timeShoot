import os
o=input("1-Ui\n2-Recursos:\n")
if o=="1":
    while True:
        nombre=input("Nombre de archivo ui:\n")
        os.system("pyuic4 "+nombre+".ui -o "+nombre+".py -x")
elif o=="2":
    while True:
        nombre=input("Nombre de archivo de recursos:\n")
        os.system("pyrcc4 "+nombre+".qrc -o "+nombre+".py -py3")