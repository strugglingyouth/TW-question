#!/usr/bin/env python
# coding:utf-8


from collections import  OrderedDict
from colorama import init, Fore


animal = OrderedDict()
def parse_file(file, id1):
    id = ''
    #animal_len = len(animal)
    file = file.split('\n')
    flag = 0
    for line in file:
        if len(line.split()) == 1:
            flag = 1
            id = line.strip()
            # 将前一个 key，value 值赋值为当前的
            if len(animal):
                for i,value in enumerate(animal):
                    if i == len(animal) - 1:
                        #print Fore.GREEN + '============'
                        #print animal[value]
                        animal[id] = animal[value]
                        #print animal[id]
            else:
                animal[id] = {}
        elif len(line.split()) == 2 and flag == 1:
            pass
        elif len(line.split()) == 3 and flag == 1:
            #print '== 3'
            an = line.split()[0]
            data = line.split()[1:]
            data1 = []
            for i in data:
                data1.append(int(i))
            #print '%s,len:%s' %(line,len(line.split()))
            # animal 和 2 个 data 则直接添加
            animal[id][an] = data1
            #print "data1:",data1
        # 大于两个值需要做减法运算
        elif len(line.split()) == 5 and flag == 1:
            #print '== 5'
            an = line.split()[0]
            data = line.split()[1:]
            data1 = []
            for i in data:
                data1.append(int(i))
            animal[id][an] = data1
            #print "animal:",animal
            # 判断数据是否正确
            for i,value in enumerate(animal):
                if i == len(animal)-2:
                   # print Fore.GREEN + "i==valuelue:",value
                    if animal[value][an][0] == animal[id][an][0] and animal[value][an][1] == animal[id][an][1]:
                    #    print Fore.GREEN + 'sum'
                     #   print animal[value][an][0],animal[id][an][0]
                        #print animal[id][an]
                        animal[id][an][0] = int(animal[id][an][0]) + int(animal[id][an][2])
                        animal[id][an][1] = int(animal[id][an][1]) + int(animal[id][an][3])
                        del animal[id][an][3]
                        del animal[id][an][2]
                    else:
                        print Fore.RED + "Conflict found at ",id
                        return
        elif len(line.split()) == 0:
            flag = 0
        else:
            print Fore.RED + "Conflict found at ",id
        #print "end--->:",animal
    s = ''
    for key1,value1 in animal[id].items():
        print key1,
        s =s + key1 + ' '
        for i in value1:
            print i,
            s += str(i)
            s += ' '
        s = s.rstrip(' ')
        print
        s += '\n'
    s = s.rstrip('\n')
    s = s.rstrip(' ')
    return s
if __name__ == '__main__':
    init(autoreset=True)
    id1 = 'a1'
    id2 = 'a2'
    id3 = 'a3'

    text = """e4e87cb2-8e9a-4749-abb6-26c59344dfee
    2016/09/02 22:30:46
    cat1 10 9

    351055db-33e6-4f9b-bfe1-16f1ac446ac1
    2016/09/02 22:30:52
    cat1 10 9 2 -1
    cat2 2 3

    dcfa0c7a-5855-4ed2-bc8c-4accae8bd155
    2016/09/02 22:31:02
    cat1 12 8 3 4"""

    id = "dcfa0c7a-5855-4ed2-bc8c-4accae8bd155"
    parse_file(text,id)

