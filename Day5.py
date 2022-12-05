#!/usr/bin/env python
# coding: utf-8

# In[83]:


import re

stack1 = ['D','T','W','F','J','S','H','N']
stack2 = ['H','R','P','Q','T','N','B','G']
stack3 = ['L','Q','V']
stack4 = ['N','B','S','W','R','Q']
stack5 = ['N','D','F','T','V','M','B']
stack6 = ['M','D','B','V','H','T','R']
stack7 = ['D','B','Q','J']
stack8 = ['D','N','J','V','R','Z','H','Q']
stack9 = ['B','N','H','M','S']
instruc = [['move 3 from 1 to 2'],['move 1 from 7 to 1'],['move 1 from 6 to 5'],['move 5 from 5 to 9'],['move 2 from 5 to 2'],['move 1 from 6 to 8'],['move 1 from 5 to 7'],['move 5 from 4 to 6'],['move 1 from 7 to 6'],['move 1 from 2 to 4'],['move 5 from 2 to 6'],['move 2 from 1 to 5'],['move 2 from 1 to 9'],['move 16 from 6 to 4'],['move 6 from 8 to 3'],['move 7 from 2 to 4'],['move 5 from 9 to 3'],['move 1 from 1 to 4'],['move 1 from 1 to 3'],['move 3 from 7 to 4'],['move 2 from 5 to 4'],['move 31 from 4 to 8'],['move 22 from 8 to 4'],['move 9 from 3 to 6'],['move 7 from 9 to 5'],['move 4 from 5 to 6'],['move 6 from 3 to 2'],['move 2 from 6 to 7'],['move 5 from 2 to 7'],['move 1 from 2 to 4'],['move 1 from 7 to 5'],['move 4 from 5 to 4'],['move 2 from 6 to 9'],['move 2 from 4 to 6'],['move 7 from 6 to 4'],['move 2 from 6 to 1'],['move 1 from 6 to 8'],['move 8 from 8 to 1'],['move 1 from 7 to 6'],['move 4 from 1 to 5'],['move 9 from 4 to 8'],['move 4 from 1 to 7'],['move 3 from 5 to 3'],['move 2 from 1 to 9'],['move 1 from 3 to 2'],['move 1 from 9 to 8'],['move 1 from 2 to 1'],['move 1 from 1 to 8'],['move 1 from 5 to 1'],['move 2 from 3 to 1'],['move 2 from 6 to 9'],['move 19 from 4 to 1'],['move 4 from 4 to 2'],['move 6 from 1 to 4'],['move 1 from 2 to 4'],['move 4 from 4 to 3'],['move 7 from 7 to 3'],['move 7 from 8 to 2'],['move 2 from 7 to 4'],['move 3 from 2 to 1'],['move 8 from 8 to 2'],['move 3 from 9 to 1'],['move 2 from 9 to 1'],['move 10 from 2 to 7'],['move 4 from 3 to 1'],['move 1 from 8 to 3'],['move 1 from 4 to 5'],['move 1 from 3 to 6'],['move 1 from 2 to 1'],['move 10 from 1 to 3'],['move 1 from 4 to 7'],['move 1 from 6 to 4'],['move 7 from 3 to 2'],['move 5 from 2 to 8'],['move 11 from 7 to 2'],['move 3 from 4 to 3'],['move 1 from 4 to 3'],['move 5 from 8 to 9'],['move 17 from 2 to 4'],['move 11 from 1 to 5'],['move 4 from 1 to 3'],['move 5 from 9 to 2'],['move 4 from 2 to 1'],['move 3 from 5 to 7'],['move 6 from 5 to 3'],['move 1 from 5 to 8'],['move 6 from 1 to 8'],['move 3 from 8 to 5'],['move 1 from 1 to 4'],['move 1 from 7 to 2'],['move 15 from 3 to 4'],['move 1 from 1 to 3'],['move 10 from 3 to 9'],['move 2 from 7 to 4'],['move 1 from 2 to 8'],['move 21 from 4 to 9'],['move 1 from 2 to 3'],['move 1 from 8 to 1'],['move 9 from 4 to 2'],['move 1 from 1 to 5'],['move 5 from 2 to 7'],['move 2 from 8 to 5'],['move 1 from 8 to 1'],['move 2 from 2 to 8'],['move 2 from 4 to 9'],['move 24 from 9 to 5'],['move 3 from 4 to 1'],['move 2 from 2 to 5'],['move 12 from 5 to 1'],['move 10 from 1 to 5'],['move 23 from 5 to 6'],['move 8 from 9 to 1'],['move 3 from 8 to 1'],['move 1 from 1 to 2'],['move 1 from 3 to 7'],['move 11 from 6 to 1'],['move 1 from 2 to 4'],['move 6 from 6 to 8'],['move 4 from 6 to 7'],['move 1 from 7 to 3'],['move 1 from 3 to 4'],['move 23 from 1 to 8'],['move 1 from 4 to 2'],['move 1 from 2 to 1'],['move 1 from 6 to 7'],['move 6 from 5 to 3'],['move 1 from 7 to 8'],['move 1 from 1 to 8'],['move 1 from 9 to 3'],['move 6 from 7 to 2'],['move 3 from 5 to 9'],['move 5 from 2 to 3'],['move 28 from 8 to 3'],['move 4 from 1 to 9'],['move 5 from 9 to 5'],['move 2 from 8 to 5'],['move 1 from 9 to 4'],['move 2 from 7 to 5'],['move 1 from 4 to 2'],['move 1 from 4 to 8'],['move 2 from 8 to 3'],['move 6 from 5 to 2'],['move 1 from 7 to 2'],['move 39 from 3 to 2'],['move 2 from 3 to 8'],['move 1 from 9 to 6'],['move 2 from 2 to 9'],['move 2 from 9 to 6'],['move 1 from 8 to 1'],['move 1 from 1 to 6'],['move 5 from 6 to 9'],['move 2 from 5 to 8'],['move 20 from 2 to 4'],['move 2 from 4 to 8'],['move 2 from 8 to 3'],['move 3 from 3 to 1'],['move 22 from 2 to 5'],['move 2 from 9 to 1'],['move 3 from 1 to 7'],['move 1 from 2 to 6'],['move 1 from 2 to 9'],['move 1 from 1 to 8'],['move 2 from 7 to 9'],['move 1 from 6 to 8'],['move 1 from 2 to 7'],['move 1 from 1 to 3'],['move 1 from 9 to 8'],['move 1 from 8 to 5'],['move 3 from 8 to 7'],['move 3 from 7 to 8'],['move 15 from 4 to 1'],['move 1 from 4 to 3'],['move 10 from 1 to 6'],['move 3 from 8 to 1'],['move 5 from 9 to 4'],['move 7 from 5 to 1'],['move 4 from 6 to 3'],['move 15 from 5 to 2'],['move 4 from 6 to 4'],['move 7 from 2 to 1'],['move 6 from 4 to 6'],['move 1 from 5 to 9'],['move 1 from 5 to 7'],['move 1 from 3 to 5'],['move 11 from 1 to 8'],['move 3 from 4 to 6'],['move 4 from 1 to 5'],['move 1 from 2 to 5'],['move 2 from 8 to 3'],['move 11 from 6 to 1'],['move 1 from 3 to 7'],['move 1 from 9 to 8'],['move 6 from 5 to 8'],['move 3 from 8 to 4'],['move 1 from 4 to 5'],['move 3 from 3 to 1'],['move 9 from 8 to 2'],['move 2 from 1 to 5'],['move 11 from 2 to 5'],['move 1 from 3 to 6'],['move 2 from 8 to 5'],['move 3 from 4 to 6'],['move 1 from 8 to 3'],['move 2 from 1 to 9'],['move 1 from 3 to 8'],['move 16 from 5 to 7'],['move 3 from 1 to 6'],['move 1 from 3 to 5'],['move 1 from 6 to 7'],['move 1 from 9 to 4'],['move 1 from 5 to 4'],['move 1 from 3 to 2'],['move 1 from 1 to 2'],['move 3 from 4 to 9'],['move 1 from 2 to 7'],['move 2 from 8 to 3'],['move 6 from 2 to 8'],['move 11 from 1 to 3'],['move 6 from 3 to 1'],['move 4 from 3 to 2'],['move 2 from 3 to 1'],['move 1 from 1 to 3'],['move 4 from 8 to 4'],['move 4 from 8 to 2'],['move 11 from 7 to 2'],['move 9 from 7 to 5'],['move 1 from 7 to 3'],['move 4 from 5 to 7'],['move 14 from 2 to 3'],['move 17 from 3 to 7'],['move 2 from 5 to 2'],['move 1 from 5 to 7'],['move 1 from 5 to 6'],['move 4 from 6 to 7'],['move 8 from 1 to 2'],['move 2 from 6 to 4'],['move 1 from 6 to 8'],['move 6 from 4 to 1'],['move 1 from 8 to 5'],['move 6 from 7 to 8'],['move 5 from 8 to 3'],['move 12 from 2 to 1'],['move 1 from 8 to 4'],['move 4 from 3 to 1'],['move 4 from 2 to 4'],['move 3 from 9 to 3'],['move 3 from 3 to 2'],['move 1 from 3 to 2'],['move 3 from 4 to 1'],['move 2 from 5 to 7'],['move 22 from 1 to 8'],['move 17 from 8 to 6'],['move 21 from 7 to 6'],['move 3 from 2 to 8'],['move 3 from 1 to 5'],['move 3 from 5 to 2'],['move 2 from 4 to 6'],['move 7 from 6 to 5'],['move 1 from 9 to 4'],['move 14 from 6 to 4'],['move 5 from 8 to 3'],['move 1 from 6 to 3'],['move 3 from 3 to 9'],['move 2 from 9 to 1'],['move 2 from 7 to 1'],['move 16 from 6 to 8'],['move 2 from 6 to 7'],['move 1 from 2 to 7'],['move 1 from 3 to 8'],['move 7 from 4 to 1'],['move 2 from 7 to 2'],['move 4 from 4 to 7'],['move 5 from 2 to 4'],['move 1 from 7 to 3'],['move 3 from 5 to 8'],['move 1 from 7 to 5'],['move 12 from 1 to 6'],['move 3 from 7 to 2'],['move 7 from 4 to 2'],['move 3 from 3 to 2'],['move 1 from 4 to 2'],['move 1 from 9 to 8'],['move 8 from 6 to 8'],['move 12 from 2 to 4'],['move 5 from 5 to 2'],['move 11 from 4 to 9'],['move 3 from 6 to 3'],['move 2 from 4 to 2'],['move 4 from 2 to 6'],['move 5 from 2 to 8'],['move 12 from 8 to 4'],['move 20 from 8 to 5'],['move 13 from 5 to 3'],['move 1 from 8 to 5'],['move 5 from 5 to 9'],['move 16 from 9 to 1'],['move 9 from 4 to 5'],['move 12 from 3 to 9'],['move 5 from 6 to 5'],['move 9 from 9 to 7'],['move 14 from 1 to 4'],['move 14 from 4 to 1'],['move 15 from 5 to 7'],['move 4 from 8 to 2'],['move 3 from 4 to 3'],['move 3 from 1 to 8'],['move 1 from 5 to 9'],['move 1 from 5 to 3'],['move 3 from 9 to 8'],['move 4 from 3 to 4'],['move 1 from 4 to 6'],['move 20 from 7 to 2'],['move 2 from 3 to 8'],['move 3 from 7 to 2'],['move 4 from 2 to 1'],['move 1 from 6 to 7'],['move 3 from 4 to 2'],['move 2 from 2 to 3'],['move 4 from 3 to 4'],['move 1 from 8 to 1'],['move 3 from 8 to 1'],['move 2 from 7 to 8'],['move 1 from 4 to 5'],['move 14 from 2 to 5'],['move 6 from 1 to 5'],['move 1 from 4 to 3'],['move 15 from 1 to 4'],['move 1 from 8 to 2'],['move 1 from 9 to 5'],['move 4 from 8 to 7'],['move 13 from 5 to 6'],['move 1 from 8 to 1'],['move 2 from 7 to 9'],['move 12 from 6 to 4'],['move 1 from 3 to 6'],['move 1 from 1 to 6'],['move 4 from 5 to 2'],['move 5 from 5 to 6'],['move 2 from 6 to 2'],['move 1 from 7 to 5'],['move 2 from 6 to 9'],['move 1 from 5 to 9'],['move 16 from 2 to 5'],['move 17 from 4 to 1'],['move 3 from 1 to 3'],['move 1 from 2 to 6'],['move 2 from 6 to 1'],['move 3 from 3 to 1'],['move 14 from 1 to 8'],['move 3 from 5 to 2'],['move 4 from 8 to 2'],['move 3 from 4 to 5'],['move 15 from 5 to 3'],['move 1 from 7 to 6'],['move 3 from 1 to 8'],['move 2 from 3 to 7'],['move 1 from 1 to 2'],['move 1 from 7 to 6'],['move 4 from 2 to 8'],['move 2 from 6 to 2'],['move 1 from 7 to 6'],['move 3 from 8 to 2'],['move 12 from 8 to 6'],['move 1 from 5 to 6'],['move 3 from 2 to 5'],['move 2 from 2 to 5'],['move 4 from 6 to 5'],['move 4 from 3 to 5'],['move 1 from 8 to 4'],['move 11 from 6 to 4'],['move 6 from 3 to 1'],['move 2 from 9 to 8'],['move 20 from 4 to 5'],['move 1 from 4 to 9'],['move 2 from 3 to 8'],['move 1 from 3 to 8'],['move 17 from 5 to 8'],['move 5 from 5 to 9'],['move 9 from 5 to 1'],['move 2 from 6 to 7'],['move 23 from 8 to 2'],['move 2 from 7 to 5'],['move 3 from 9 to 4'],['move 16 from 2 to 4'],['move 11 from 1 to 8'],['move 4 from 5 to 8'],['move 11 from 2 to 6'],['move 2 from 6 to 1'],['move 5 from 9 to 5'],['move 5 from 5 to 6'],['move 5 from 8 to 6'],['move 1 from 6 to 7'],['move 7 from 8 to 1'],['move 12 from 1 to 2'],['move 1 from 9 to 5'],['move 1 from 1 to 3'],['move 1 from 1 to 4'],['move 1 from 5 to 3'],['move 1 from 3 to 6'],['move 1 from 8 to 2'],['move 18 from 6 to 2'],['move 1 from 6 to 2'],['move 2 from 8 to 3'],['move 3 from 3 to 8'],['move 18 from 4 to 9'],['move 11 from 9 to 2'],['move 2 from 9 to 6'],['move 2 from 4 to 1'],['move 1 from 1 to 5'],['move 1 from 5 to 4'],['move 1 from 4 to 8'],['move 42 from 2 to 1'],['move 3 from 9 to 3'],['move 1 from 8 to 1'],['move 1 from 3 to 4'],['move 3 from 8 to 7'],['move 1 from 4 to 1'],['move 2 from 3 to 2'],['move 17 from 1 to 6'],['move 15 from 6 to 3'],['move 2 from 9 to 7'],['move 1 from 3 to 6'],['move 2 from 7 to 6'],['move 2 from 2 to 4'],['move 1 from 2 to 3'],['move 1 from 4 to 9'],['move 1 from 4 to 1'],['move 1 from 6 to 3'],['move 20 from 1 to 9'],['move 6 from 1 to 9'],['move 7 from 9 to 3'],['move 20 from 9 to 1'],['move 1 from 6 to 7'],['move 2 from 6 to 7'],['move 1 from 6 to 5'],['move 1 from 6 to 8'],['move 4 from 7 to 3'],['move 3 from 7 to 2'],['move 1 from 6 to 4'],['move 1 from 2 to 1'],['move 1 from 4 to 9'],['move 21 from 3 to 2'],['move 5 from 3 to 8'],['move 1 from 5 to 1'],['move 2 from 8 to 7'],['move 4 from 8 to 3'],['move 4 from 2 to 5'],['move 19 from 2 to 3'],['move 1 from 9 to 2'],['move 23 from 3 to 2'],['move 2 from 7 to 4'],['move 3 from 5 to 9'],['move 16 from 2 to 1'],['move 1 from 5 to 4'],['move 1 from 9 to 3'],['move 2 from 3 to 8'],['move 3 from 4 to 6'],['move 1 from 6 to 2'],['move 1 from 8 to 6'],['move 5 from 2 to 6'],['move 7 from 6 to 5'],['move 4 from 2 to 6'],['move 6 from 5 to 9'],['move 1 from 8 to 4'],['move 18 from 1 to 9'],['move 1 from 5 to 2'],['move 9 from 9 to 4'],['move 5 from 6 to 3'],['move 9 from 4 to 1'],['move 4 from 9 to 2'],['move 1 from 4 to 8'],['move 1 from 8 to 3'],['move 7 from 1 to 8'],['move 6 from 3 to 2'],['move 10 from 2 to 9'],['move 21 from 1 to 8'],['move 1 from 2 to 8'],['move 19 from 8 to 4'],['move 1 from 8 to 3'],['move 16 from 4 to 8'],['move 1 from 4 to 2'],['move 2 from 1 to 5'],['move 1 from 2 to 3'],['move 1 from 4 to 5'],['move 1 from 4 to 8'],['move 2 from 1 to 3'],['move 3 from 3 to 2'],['move 5 from 9 to 1'],['move 1 from 3 to 4'],['move 4 from 9 to 4'],['move 2 from 1 to 9'],['move 2 from 2 to 5'],['move 1 from 2 to 7'],['move 3 from 1 to 7'],['move 10 from 8 to 6'],['move 4 from 8 to 5'],['move 3 from 4 to 3'],['move 3 from 3 to 4'],['move 1 from 9 to 8'],['move 2 from 7 to 2'],['move 1 from 2 to 1'],['move 4 from 9 to 3']]


# In[43]:


for x in instruc:
    currentstep = []
    currentstep.append([int(s) for s in re.findall(r'\b\d+\b', x[0])])
    for y in currentstep:
        for _ in range(y[0]):
            yeet = ''
            if y[1] == 1:
                yeet = stack1.pop()
            elif y[1] == 2:
                yeet = stack2.pop()
            elif y[1] == 3:
                yeet = stack3.pop()
            elif y[1] == 4:
                yeet = stack4.pop()
            elif y[1] == 5:
                yeet = stack5.pop()
            elif y[1] == 6:
                yeet = stack6.pop()
            elif y[1] == 7:
                yeet = stack7.pop()
            elif y[1] == 8:
                yeet = stack8.pop()
            elif y[1] == 9:
                yeet = stack9.pop()
                
            if y[2] == 1:
                stack1.append(yeet)
            elif y[2] == 2:
                stack2.append(yeet)
            elif y[2] == 3:
                stack3.append(yeet)
            elif y[2] == 4:
                stack4.append(yeet)
            elif y[2] == 5:
                stack5.append(yeet)
            elif y[2] == 6:
                stack6.append(yeet)
            elif y[2] == 7:
                stack7.append(yeet)
            elif y[2] == 8:
                stack8.append(yeet)
            elif y[2] == 9:
                stack9.append(yeet)
                
print(stack1.pop())
print(stack2.pop())
print(stack3.pop())
print(stack4.pop())
print(stack5.pop())
print(stack6.pop())
print(stack7.pop())
print(stack8.pop())
print(stack9.pop())


# In[84]:


for x in instruc:
    currentstep = []
    currentstep.append([int(s) for s in re.findall(r'\b\d+\b', x[0])])
    for y in currentstep:
        for _ in range(y[0]):
            yeet = ''
            if y[1] == 1:
                t.append(stack1.pop())
            elif y[1] == 2:
                t.append(stack2.pop())
            elif y[1] == 3:
                t.append(stack3.pop())
            elif y[1] == 4:
                t.append(stack4.pop())
            elif y[1] == 5:
                t.append(stack5.pop())
            elif y[1] == 6:
                t.append(stack6.pop())
            elif y[1] == 7:
                t.append(stack7.pop())
            elif y[1] == 8:
                t.append(stack8.pop())
            elif y[1] == 9:
                t.append(stack9.pop())
                         
        while(len(t) != 0):
            if y[2] == 1:
                stack1.append(t.pop())
            elif y[2] == 2:
                stack2.append(t.pop())
            elif y[2] == 3:
                stack3.append(t.pop())
            elif y[2] == 4:
                stack4.append(t.pop())
            elif y[2] == 5:
                stack5.append(t.pop())
            elif y[2] == 6:
                stack6.append(t.pop())
            elif y[2] == 7:
                stack7.append(t.pop())
            elif y[2] == 8:
                stack8.append(t.pop())
            elif y[2] == 9:
                stack9.append(t.pop())
print(stack1.pop())
print(stack2.pop())
print(stack3.pop())
print(stack4.pop())
print(stack5.pop())
print(stack6.pop())
print(stack7.pop())
print(stack8.pop())
print(stack9.pop())

