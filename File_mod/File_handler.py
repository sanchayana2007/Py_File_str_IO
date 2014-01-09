'''Author : Sanche 
This module will handle the file I/O Operations and cretaion of new files 
'''

class FileHandler(object):
	'''Method for checking the file Authenticity'''
	def __init__(self):
		self.FileHandlerError = "No error"
		self.Intial_file_name = ""
		self.fd_read = ""
		self.file_name_1 = ""
		self.file_name_2 = ""
		
		
	'''Method for checking the file Authenticity'''
	def file_open(self,filename1,filename2,filename3):
		if filename1 == "":
			print "file for reading is not provided"
		else:
			self.Intial_file_name = filename1
			self.fd_read = open(self.Intial_file_name,'r')
			if self.fd_read == "":
				"got to throw an exception while Opening"
				print "Not able to open the file "
			else:
				self.file_name_1 = open(filename2,'w+')
				self.file_name_2 = open(filename3,'w+')
				return self.fd_read
			
						
			
	'''Method for Reading the file lien will return an List of the words'''
	def read_line(self):
			line= fd_read.readline()
			return line
		
	def close_all_files(self):
		self.fd_read.close()
		self.file_name_1.close()
		self.file_name_2.close()
		