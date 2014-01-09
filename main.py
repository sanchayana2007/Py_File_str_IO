
''' Author: Sanche
this will have the parser Logic for the functions '''

from File_mod import File_handler
import parser

if __name__ == '__main__':
	List_of_lines = []
	'''Read the file and get a List for a Line '''
	fo = File_handler.FileHandler()
	fd_read = fo.file_open("test.txt","test2.txt","test3.txt")
	for line in fd_read:
		print line
		List_of_lines.append(line)
	fo.close_all_files()
		