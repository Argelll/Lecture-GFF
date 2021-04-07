#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from LectureFichier import *
from ClassGene import *

nombrePseudogenes=0
typeElement="pseudogene"
nomFichier = sys.argv[1]

fichier = Files(nomFichier)
toutesLignes=fichier.Lecture()
for ligne in toutesLignes :
  position=ligne.split("\t")
  try:
    if (position[2]==typeElement):
      nombrePseudogenes=nombrePseudogenes+1
      print (position[2])
  except:
   print("")
print (nombrePseudogenes)
