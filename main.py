
''' Author: Sanche
this will have the parser Logic for the functions '''

from File_mod import File_handler
import Parser.parser
from optparse import OptionParser
import fileinput 

def main():
	''' Usage , pattern and version are predefined atributes for OPtionParser'''
	opparser = OptionParser(usage="%prog -i file1 -f file2 -d file3  B1060550",version="%prog 1.0")
	''' Store is REGEXPR and -e , will store the value in regexpr If not given then default is false and help '''
	opparser.add_option('-i', action="store" ,help="Input file to read from ")
	opparser.add_option('-f', action="store",help="Input file to Write vowels ")
	opparser.add_option('-d', action="store" ,help="Input file to Write Non vowels  ")
	
	opt,args = opparser.parse_args()
	print opt.i , opt.f,opt.d
	
	
	List_of_lines = []
	'''Read the file and get a List for a Line '''
	fo = File_handler.FileHandler()
	fd_read = fo.file_open("test.txt","test2.txt","test3.txt")
	'''This file will return file handler for the Read out file '''
	
	
	for line in fd_read:
		'''Line will give the 1st line ended buy \n, add all the lines in a string array'''
		List_of_lines.append(line)
		Lineparser = Parser.parser.Parser()
		Lineparser.Check_Vowels(line)
		
		'''Write on the vowel file'''
		for vow in Lineparser.elements_Vowels:
			vow = vow + '\n'
			fo.file_name_1.write(vow)
		
		'''Write on the Inverted  file'''
		for vow in Lineparser.elements_Inverted:
			vow = vow + '\n'
			fo.file_name_2.write(vow)
			
			
		
	fo.close_all_files()
		



if __name__ == '__main__':
	main()
	