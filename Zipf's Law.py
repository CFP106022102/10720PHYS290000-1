#!/usr/bin/env python
# coding: utf-8

# In[ ]:


fp = open('Alice.txt','r',encoding='UTF-8')
from collections import Counter

line = fp.readline()
lists = line.split() 

while line:
    line = fp.readline()
    lists =  lists+line.split() 

dir1s = Counter(lists)
print(dir1s)

fp.close()


# In[ ]:


fp = open('Alice.txt','r',encoding='UTF-8')
import matplotlib.pyplot as plt

line = fp.readline()
my_dict = {}

while line:
    s = line.split() 
    for x in s:
        if x not in my_dict:
            my_dict[x] = 1
        else:
            my_dict[x] += 1
    line = fp.readline()


fp.close()

num=[]

for key in my_dict:
    num.append(my_dict[key])
    
print(len(num))
num.sort()
num.reverse()

plt.loglog(range(len(num)),num)
plt.xlable('Rank of the words')
plt.ylable('Number of the occurance')

