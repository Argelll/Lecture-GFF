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
  for parties in position
    print (parties+";")
  try :
    #unGene= Gene(position[0],position[1],position[2],position[3],position[4],position[5],position[6],position[7])
    #listeGene.append(unGene)
  except :
    print ("pas cette ligne")
    
for genes in listeGene:
  print (genes)
