# -*- coding: utf-8 -*-
#S.Ardizzone
#FA2010
#Sample implementation of SearchBase ABC

import abc
from SearchBase import SearchBase

class AnimalSearch(SearchBase):
    results = None
    keywords = {}
    
    def search(self, query, rpp):
        self.results = super(AnimalSearch, self).search(query, rpp)
        self.printResults()

    def printResults(self):
        for res in self.results:
            print res.title#.encode("utf8")
            print res.desc#.encode("utf8")
            print res.url#.encode("utf8")
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
    
	def getKeywords( self ):
        """reads file keywordsFile.txt, imports into a dictionary each keyword and the advertisement string to promote our cause"""
 
        keywordsFile = open( "keywords.txt" )
   
        for line in keywordsFile:
   
            pair = line.split( ':' ) #returns a list with two items (the key and the value)
 
            #add key and value pair to keywords dictionary
            self.keywords[ pair[0] ] =  pair[1].strip( '\n' )
 
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

        

