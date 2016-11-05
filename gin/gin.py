# -*- coding: utf-8 -*-


"""gin.gin: provides entry point main()."""


__version__ = "0.0.3"


import sys

from .parser import Parser


def main():
	
    parser = Parser()
    
    gin_src = sys.argv[1]
    
    ini_dst = sys.argv[1].replace(".gin", ".ini")

    parser.parse(gin_src, ini_dst)

