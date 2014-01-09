'''Author : Sanche 
This module will handle the file I/O Operations and cretaion of new files 
'''

class FileHandler(object):
	'''Method for checking the file Authenticity'''
	def __init__(self):
		self.FileHandlerError = "No error"
		self.Intial_file_name = ""
		self.fd_read = ""
	'''Method for checking the file Authenticity'''
	def file_open(self,filename1,filename2,filename3):
		if filename1 == "":
			print "file for reading is not provided"
		else:
			self.Intial_file_name = filename1
			self.fd_read = open(self.Intial_file_name,'r')
			if fd_read == "":
				"got to throw an exceptrion while Opening"
				print "Not able to open the file "
			
	'''Method for Reading the file lien will return an List of the words'''
	def read_line(self):
			line= fd_read.readline()
			return line
		
