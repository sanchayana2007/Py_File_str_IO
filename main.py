
''' Author: Sanche
this will have the parser Logic for the functions '''

from File_mod import File_handler
import Parser.parser
from optparse import OptionParser
import fileinput 

def main():
	''' Usage , pattern and version are predefined atributes for OPtionParser'''
	opparser = OptionParser(usage="%prog -e PATTREN",version="%prog 1.0")
	''' Store is REGEXPR and -e , will store the value in regexpr If not given then default is false and help '''
	opparser.add_option("-e","--regexpr",dest="regexpr",action="store", default=False ,help="pattern expresion for match ")
	opt,args = opparser.parse_args()
	
	List_of_lines = []
	'''Read the file and get a List for a Line '''
	fo = File_handler.FileHandler()
	fd_read = fo.file_open("test.txt","test2.txt","test3.txt")
	for line in fd_read:
		'''print line'''
		List_of_lines.append(line)
		Lineparser = Parser.parser.Parser()
		Lineparser.Check_Vowels(line)
		
		
	fo.close_all_files()
		



if __name__ == '__main__':
	main()
	