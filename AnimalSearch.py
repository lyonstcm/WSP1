# -*- coding: utf-8 -*-
#S.Ardizzone
#FA2010
#Sample implementation of SearchBase ABC
import random
import abc
from SearchBase import SearchBase

class AnimalSearch(SearchBase):
    results = None
    keywords = {}
    key_list = []
    
    def search(self, query, rpp):
        self.results = super(AnimalSearch, self).search(query, rpp)
        self.printResults()

    
    def printResults(self):
	i = 0;
	for key in self.key_list:
		j = self.key_list[i][0]
		random1 = random.randint(1,4)
		k = self.key_list[i][random1]
		i+=1
		for res in self.results:
			tmpTitle = (res.title.encode('utf-8').lower().strip('().,:-\'\"')).split(" ")
			tmpDesc = (res.desc.encode('utf-8').lower().strip('().,:-\'\"')).split(" ")
			thetext = tmpTitle
			thetext+= " "
			thetext+=tmpDesc
			#print res.title.encode('utf8')
			#print res.desc.encode('utf8')
			#print
			#print
			#for word in thetext:
				#if j == word:
					#print "MATCH FOUND"
					#print word
					#print res.title.encode('utf8')
					#print k
			
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
		#print "ORDERED"
        #search titles and descriptions for keywords
        for res in self.results:
            tmpTitle = (res.title.encode('utf-8').lower().strip('().,:-\'\"')).split(" ")
            tmpDesc = (res.desc.encode('utf-8').lower().strip('().,:-\'\"')).split(" ")
            for key in self.keywords.keys():
                for t in tmpTitle:
                    if key == t:
                        value+=self.keywords[key]
                for t in tmpDesc:
                    if key == t:
                        value+=self.keywords[key]
            pair = res, value
            orders.append(pair)
            pair = ()
            value = 0
		
	for item in orders:
		print item
	
    def getKeywords( self ):
    #reads file keywordsFile.txt, imports into a dictionary each keyword and the advertisement string to promote our cause
 
	keywordsFile = open( "keywords_dictionary.txt" )
   
	for line in keywordsFile:
   
		triplet = line.split( ':' ) #returns a list with  items (the key and the value)
		
		word = triplet[0]
		def1 = triplet[1]
		def2 = triplet[2]
		#zipped = zip(word,def1,def2)
            #add key and value pair to keywords dictionary
		#print zipped
		self.key_list.append(triplet)
		
			#self.key_list
	
            #alternatively:
            #  self.keywords[ pair[0] ] =  pair[1].strip( )
            #  would get rid of both the \n and the space after the ':'
	
	keywordsFile.close( )    
		#order results based on values
    def cmpfun(a,b):
        return cmp(b[1],a[1])
        orders.sort(cmpfun)
        
        for i in orders:
            print i[0].title, "RANK = ", i[1]
            print i[0].desc
            print

		
