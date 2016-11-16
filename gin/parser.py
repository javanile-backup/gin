# -*- coding: utf-8 -*-


"""gin.parser: stuff module within the bootstrap package."""

##
import os

##
class Parser(object):
    
    ##
    def parse(__self__, gin_src, ini_dst):
    
        ##
        with open(gin_src, 'r') as cin, open(ini_dst, "w") as cout:
		
            ##
            content = cin.read()

        	## replace environment variables
            for name in os.environ:
		        content = content.replace('{{$'+name+'}}', os.environ[name].replace('\\','/'))

		    ## write new ini file
            cout.write(content)

	
