#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from LectureFichier import *
from ClassGene import *
print ("on y passe")
nomFichier = sys.argv[1]
print (nomFichier)

fichier = Files(nomFichier)
listeGene=[]
toutesLignes=fichier.Lecture()
for ligne in toutesLignes :
  position=ligne.split("\t")
  print (position[2])
