#!/usr/bin/env python
# coding:utf-8


from collections import  OrderedDict
from colorama import init, Fore

animal = OrderedDict()
def parse_file(file, id):
    animal_len = len(animal)
    animal[id] = {}
    file = file.split('\n')
    ct = 0
    for line in file:
        print line 
        if ct == 0:
            ct = 1
        else: 
            an = line.split()[0] 
            data = line.split()[1:]
            print '%s,len:%s' %(line,len(line.split()))
            # animal 和 2 个 data 则直接添加    
            if len(line.split()) == 3:
                print '== 3'
                animal[id][an] = data
            # 大于两个值需要做减法运算               
            elif len(line.split()) == 5:
                print '== 5'
                animal[id][an] = data 
                print "animal:",animal 
                # 判断数据是否正确
                for i,value in enumerate(animal):
                    if i == animal_len-1:
                        print "i==valuelue:",value
                        if animal[value][an][0] == int(animal[id][an][0]) and animal[value][an][1] == int(animal[id][an][1]):
                            animal[id][an][0] = int(animal[id][an][0]) + int(animal[id][an][2])
                            animal[id][an][1] = int(animal[id][an][1]) + int(animal[id][an][3])
                            del animal[id][an][3]
                            del animal[id][an][2]
                        else:
                            print Fore.RED + "Conflict found at ",id
                            return 
            else:
                print Fore.RED + "Conflict found at ",id
        print "end--->:",animal

if __name__ == '__main__':
    init(autoreset=True)
    id1 = 'a1' 
    id2 = 'a2' 
    id3 = 'a3'

    text1 = """"2016/09/02 22:30:46
    cat1 10 9"""
    
    text2 = """2016/09/02 22:30:52
    cat1 10 9 2 -1
    cat2 2 3"""
    
    text3 = """2016/09/02 22:31:02
    cat1 11 8 3 4
    """
    
    text4 = """2016/09/02 22:31:02
    cat1 12 8 3 4
    """


    parse_file(text1,id1)
    parse_file(text2,id2)
    parse_file(text4,id3)
    print "result:",animal[id2]

