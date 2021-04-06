#!/usr/bin/env python
# -*- coding:utf-8 -*-

import gzip
import logging

#Files hérite de la classe object
class Files(object):
  def __init__(self, File):
    self.File = File
    
  def __iter__(self):
    try:
      if self.File.lower().endswith(('.gz', '.gzip')):
        fp = gzip.open(self.File)
    except:
      printf("un des fichiers proposés n'es pas en .gz ou .gzip")    
    
    for line in enumerate(fp):
      line = line.decode()
      return line
    fp.close()
  
