# -*- coding: utf-8 -*-


"""gin.gin: provides entry point main()."""


__version__ = "0.0.4"


import sys
import os

from .parser import Parser

def main():
	
    parser = Parser()
    
    gin_src = sys.argv[1]
    
    ini_dst = sys.argv[1].replace(".gin", ".ini")

    if not os.path.isfile(gin_src):
        print 'File not found:', gin_src
        sys.exit(1)    

    parser.parse(gin_src, ini_dst)

