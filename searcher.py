# -*- coding: utf-8 -*-
import linecache
import random
from AnimalSearch import AnimalSearch
test = AnimalSearch()
test.getKeywords()
test.search("dog", 25)
found = test.reorder()
if found == True:
    test.printResults()
    



#else
#    line_num = random.randint(0, 6)
#    line = linecache.getline('keywords.txt', line_num)
#    test.search("dog" + line, 25)
#    test.reorder()

