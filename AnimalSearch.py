# -*- coding: utf-8 -*-
#S.Ardizzone
#FA2010
#Sample implementation of SearchBase ABC
import abc
import random
import linecache
from operator import itemgetter
from SearchBase import SearchBase

class AnimalSearch(SearchBase):
    results = None
    keywords = {}
    key_list = []
    orders_sorted = []		#True results sorted by keyword appearence rate
    list_results = []
    our_query = []    		#Results of users query + one of our keywords
    orig_results = [] 		#True results from users query
    glob_bool = False 		#Used to check if keywords were hit
    key_found = False 		#Used to see if a keyword was found in a title/description
    keyfound = None
    
    def search(self, query, rpp):
        self.orig_results = self.results = super(AnimalSearch, self).search(query, rpp)
	self.getKeywords()
	self.glob_bool = self.keychecker()
	#print self.glob_bool
	#If a keyword was hit by the user's query
	if self.glob_bool == True:
	    found = self.reorder()
	    if found == True:
		self.printResults()

	#The first query did not hit keywords
	elif self.glob_bool == False:
    
	    #Generate a random number to decide which of our best keywords to use
	    line_num = random.randint(0, 6)
	    line = linecache.getline('keywords.txt', line_num)
	    our_query = self.results = super(AnimalSearch, self).search(query + line, 25)
	    self.reorder()
	    i = 0
	    j = 0
	    count = 0
	
	    while count < rpp and j+2 < len(self.orig_results) and i+1 < len(self.orders_sorted):
		#Prints one injected result
		print self.orders_sorted[i][0].title
		print self.orders_sorted[i][0].desc
		print 
		i = i + 1
		
		#Prints the first real result
		print self.orig_results[j].title
		print self.orig_results[j].desc
		print
		j = j + 1
		
		#Prints the second real result
		print self.orig_results[j].title
		print self.orig_results[j].desc
		print
		j = j + 1
	    
	    #This never would break correctly
		#count = count + 3
		#print count
		#if count + 3 > rpp:
		  #break
		
	#This was going to add the extra to give us the correct number of results
	#j = j + 1
	#while count < rpp:
	  #print self.orig_results[0][j].title
	  #self.final_results.append(self.orders_sorted[j])
	  


        

    
    def printResults(self):
	i = 0
	#Orders Sorted is the list that has been weighted with our keywords on top
	for res in self.orders_sorted:
	    print res[0].title.encode('utf8')
	    print res[0].desc.encode('utf8')
	    if res[2] != None:
	        ran = random.randint(1,10)
		for key1 in self.key_list:
		    if key1[0] == res[2]:
			print key1[ran]
	    print
	    print
	

	   	    
		
    def initDictionary(self):
        key_file = open("keywords.txt",'r')
        count = 1
        for line in key_file:
            for word in line.split():
                self.keywords[word]=count
                count = count+1
	
    def reorder(self):
        self.initDictionary()
        value = 0
        orders = []
        pair = ()
        keyfound1 = 0
		#print "ORDERED"
        #search titles and descriptions for keywords
	
        for res in self.results:
	    
            tmpTitle = (res.title.encode('utf-8').lower().strip('().,:-\'\"')).split(" ")
            tmpDesc = (res.desc.encode('utf-8').lower().strip('().,:-\'\"')).split(" ")
            for key in self.keywords.keys():
                for t in tmpTitle:
                    if key == t:
                        value+=self.keywords[key]
                        self.key_found = True
			self.keyfound = key
			self.glob_bool = True
                for t in tmpDesc:
                    if key == t:
                        value+=self.keywords[key]
                        self.key_found = True
			self.keyfound = key
			self.glob_bool = True
            pair = res, value, self.keyfound
            orders.append(pair)
            pair = ()
            value = 0
	self.orders_sorted = sorted(orders, key=itemgetter(1), reverse=True) 


	return self.key_found
	
    def getKeywords( self ):
    #reads file keywordsFile.txt, imports into a dictionary each keyword and the advertisement string to promote our cause
 
	keywordsFile = open( "keywords_dictionary.txt" )
   
	for line in keywordsFile:
   
		defs = line.split( ':' ) #returns a list with  items (the key and the value)
		
		word = defs[0]
		def1 = defs[1]
		def2 = defs[2]
		def3 = defs[3]
		def4 = defs[4]
		def5 = defs[5]
		def6 = defs[6]
		def7 = defs[7]
		def8 = defs[8]
		def9 = defs[9]
		def10 = defs[10]
		#zipped = zip(word,def1,def2)
		#add key and value pair to keywords dictionary
		#print zipped
		self.key_list.append(defs)
		
	
	keywordsFile.close( )    
	#order results based on values
    def keychecker(self):
	thetext = ""
	for key in self.key_list: 
	    for res in self.results:
		thetext = res.title.encode('utf8')
		thetext += res.desc.encode('utf8')
		for word in thetext:
		    if word == key[0]:
			return True
	return False