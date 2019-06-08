#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
cli -- shortdesc

cli is a description

It defines classes_and_methods

@author:	 user_name

@copyright:  2019 organization_name. All rights reserved.

@license:	license

@contact:	user_email
@deffield	updated: Updated
'''
import sys
import os
from argparse import ArgumentParser
# __all__ = []
__version__ = "0.0.1"
# __date__ = '2019-06-07'
# __updated__ = '2019-06-07'
# class CLIError(Exception):
# 	'''Generic exception to raise and log different fatal errors.'''
# 	def __init__(self, message):
# 		super().__init__(message)
# 		self.message = "E: {}".format(message)
# 	def __repr__(self):
# 		return self.message  
def main(argv=None):
	parser = ArgumentParser(usage="inlinestyle2css [options] file|dir ...")
	parser.add_argument('-V', '--version', action='version', version='%(prog)s {}'.format(__version__))
	parser.add_argument("-v", "--verbose", dest="verbose", action="count", default=0, type=int, 
					help="set verbosity level [default: %(default)s]")
	parser.add_argument('-o', '--output-dir', action='store', type="str", help="Put output files in this directory")
	
	
	
	
	
	parser.add_argument("-r", "--recursive", dest="recurse", action="store_true", help="recurse into subfolders [default: %(default)s]")
	parser.add_argument("-i", "--include", dest="include", help="only include paths matching this regex pattern. Note: exclude is given preference over include. [default: %(default)s]", metavar="RE" )
	parser.add_argument("-e", "--exclude", dest="exclude", help="exclude paths matching this regex pattern. [default: %(default)s]", metavar="RE" )
	
	parser.add_argument(dest="paths", help="paths to folder(s) with source file(s) [default: %(default)s]", metavar="path", nargs='+')
	
	
	
	
	
	'''Command line options.
	>>> main(("/home",))
	/home
	0
	'''
	if argv is None:
		argv = sys.argv
	else:
		sys.argv.extend(argv)
	program_name = os.path.basename(sys.argv[0])
	program_version = "v{}".format(__version__)
	program_build_date = __updated__
	program_version_message = '%(prog)s {} ({})'.format(program_version, program_build_date)
	program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
	program_license = '''{}

  Created by user_name on {}.
  Copyright 2019 organization_name. All rights reserved.

  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
'''.format(program_shortdesc, __date__)
	try:
		parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
		parser.add_argument("-r", "--recursive", dest="recurse", action="store_true", help="recurse into subfolders [default: %(default)s]")
		parser.add_argument("-v", "--verbose", dest="verbose", action="count", help="set verbosity level [default: %(default)s]")
		parser.add_argument("-i", "--include", dest="include", help="only include paths matching this regex pattern. Note: exclude is given preference over include. [default: %(default)s]", metavar="RE" )
		parser.add_argument("-e", "--exclude", dest="exclude", help="exclude paths matching this regex pattern. [default: %(default)s]", metavar="RE" )
		parser.add_argument('-V', '--version', action='version', version=program_version_message)
		parser.add_argument(dest="paths", help="paths to folder(s) with source file(s) [default: %(default)s]", metavar="path", nargs='+')
		args = parser.parse_args()
		paths = args.paths
		verbose = args.verbose
		recurse = args.recurse
		inpat = args.include
		expat = args.exclude
		if verbose is not None:
			print("Verbose mode on")
			if recurse:
				print("Recursive mode on")
			else:
				print("Recursive mode off")
		if inpat and expat and inpat == expat:
			raise CLIError("include and exclude pattern are equal! Nothing will be processed.")
		for inpath in paths:
			print(inpath)
		return 0
	except KeyboardInterrupt:  # Ctrl + C。
		return 0
	except Exception as e:
		if DEBUG or TESTRUN:
			raise(e)
		indent = len(program_name) * " "
		sys.stderr.write("{}: {}\n".format(program_name, repr(e)))
		sys.stderr.write("{}  for help use --help\n".format(indent))
		return 2
