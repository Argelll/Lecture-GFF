#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from LectureFichier import *

nombreComptes=0
nombreAutres=0
typeElement="pseudogene"
nomFichier = sys.argv[1]
taille=0

fichier = Files(nomFichier)
toutesLignes=fichier.Lecture()
for ligne in toutesLignes :
  position=ligne.split("\t")
  try:
    if (position[2]==typeElement):
      nombreComptes=nombreComptes+1
      taille=int(position[4])-int(position[3])
      print(taille)
  except:
    pass
nombreTotal=nombreComptes+nombreAutres
print ("Il y a "+str(nombreComptes)+" "+str(typeElement)+"s")

