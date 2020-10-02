import os.path, shutil
from os import chdir
from typing import List
import fnmatch
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


print("\n\nPROGRAMME POUR LE TROMBINOSCOPE\n\
\t> Author  : Nathael\n\
\t> GitHub     : ?\n\
\t> Site    : https://www.nathaelb.fr\n\n\n\n\n\n")


def ListNames(files: str)->List[List]:
    with open("./photo/nom.txt", "r", encoding="utf-8")as f:
        l = f.read()
    t = l.split("\n")
    for i in range(len(t)):
        t[i] = t[i].split(" ")
        #[['Nom', 'Prénom'],['Nom', 'Prénom'],['Nom', 'Prénom'],['Nom', 'Prénom'],['Nom', 'Prénom']]
    return t


def Filter(repertoire: str)->List:
    lf =[]
    for f in os.listdir(repertoire):
        if f.split(".")[-1]=="jpg":
            lf.append(f)
    return lf



def RenamePhotos(repertoire:str, listNames:list, TargetFolder=str)->None:
    lf = Filter(repertoire)
    targetFolder = "./"+TargetFolder+"/"
    os.mkdir("./pdf_photo")
    for i in range(len(listNames)):
        shutil.copy(repertoire+lf[i], targetFolder+listNames[i][0]+"-"+listNames[i][1]+".jpg")
    #lfr = []
    # for f in range(len(listNames)):
    #     if f.split("0")[0]=="img":
    #         lfr.os.remove()
    return



def main():
    print(ListNames(List))
    RenamePhotos("photo/", ListNames(List), "pdf_photo");
if __name__ == '__main__':
    main()


























































#for j in range(len(t)):


#for i in range(len(photo_eleves)):
#    shutil.move("./" + photos_eleves[i], texte[i])


