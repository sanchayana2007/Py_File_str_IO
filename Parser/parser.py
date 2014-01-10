
''' Author: Sanche
this will have the parser Logic for the functions '''

import re

class Parser(object):
	def __init__(self):
		self.elements_Vowels = []
		self.elements_Inverted = []
		self.arrayofVowels = ['a','e','i','o','u']
		
	def Check_Vowels(self,line):
		'''pattern_space = re.split("(?:(?:[^a-zA-Z]+')|(?:'[^a-zA-Z]+))|(?:[^a-zA-Z']+)", line)'''
		pattern_space = re.compile("([\w][\w]*'?\w?)").findall(line)
		if pattern_space:
			'''print 'found',pattern_space'''
			for word in pattern_space:
				
				print word[0]
				for Vchck in self.arrayofVowels:
					if word[0] == Vchck:
							print 'Vowel'
							self.elements_Vowels.append(word)
					else:
						self.elements_Inverted = word[0]
							
		else:
			print 'Not found'
		
	
		
