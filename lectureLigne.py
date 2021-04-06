#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from LectureFichier import *
from ClassGene import *

nomFichier = sys.argv[0]

fichier = Files(nomFichier)
listeGene=[]
toutesLignes=fichier.Lecture()
for ligne in toutesLignes :
  position=ligne.split("\t")
  try :
    unGene= Gene(position[0],position[1],position[2],position[3],position[4],position[5],position[6],position[7])
    listeGene.append(unGene)
  except :
    ("pas cette ligne")
  for genes in listeGene:
    print (genes)
