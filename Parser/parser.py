
''' Author: Sanche
this will have the parser Logic for the functions '''

import re

class Parser(object):
	def __init__(self):
		self.elements_Vowels = []
		self.elements_Inverted = []
		self.arrayofVowels = ['a','e','i','o','u']
		self.vowel_flag = 0
		
	def Check_Vowels(self,line):
		
		'''pattern_space = re.split("(?:(?:[^a-zA-Z]+')|(?:'[^a-zA-Z]+))|(?:[^a-zA-Z']+)", line)'''
		pattern_space = re.compile("([\w][\w]*'?\w?)").findall(line)
		if pattern_space:
			'''print 'found',pattern_space'''
			for word in pattern_space:
								
				for Vchck in self.arrayofVowels:
					if word[0] == Vchck:
							print 'Vowel=',word
							self.elements_Vowels.append(word)
							self.vowel_flag = 1
							
			
				if self.vowel_flag == 0:
					''' It works by doing [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string.It will form a new string by going to the -1,-2,-3 till length'''
					self.elements_Inverted.append(word[::-1])
					print "in parser=,", word
				
							
		else:
			print 'Not found'
		
	
		
