# -*- coding: utf-8 -*-


"""gin.parser: stuff module within the bootstrap package."""

##
import os

##
class Parser(object):
    
    ##
    def parse(__self__, gin_src, ini_dst):

	## read gin source content 
        content = open(gin_src, 'r').read()

        ## replace environment variables
        for name in os.environ:
            print (name+": "+os.environ[name]) 
            content = content.replace('{{$'+name+'}}', os.environ[name].replace('\\','/'))

	## write new ini file
        open(ini_dst, "w").write(content)	

	
