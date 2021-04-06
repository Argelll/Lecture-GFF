#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import LectureFichier.py
import ClassGene.py

nomFichier = sys.argv[0]

fichierLu = Files(nomFichier)
listeGene=[]
for lignes in fichierLu :
  position=lignes.split("\t")
  unGene= Gene(position[0],position[1],position[2],position[3],position[4],position[5],position[6],position[7])
  listeGene.append(unGene)
  
  
