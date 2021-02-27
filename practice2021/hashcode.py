#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:23:14 2021

@author: tapli
"""

f = open("c_many_ingredients.in", "r")
content = f.read()
content_list = content.splitlines()
f.close()

t = content_list[0]
t = t.split()

total_pizza=int(t[0])
t2=int(t[1])
t3=int(t[2])
t4=int(t[3])

no_of_ing=[]
ing=[]
ind=[]
tot_ing=[]

for i in range(1,len(content_list)):
    z=content_list[i].split()
    no_of_ing.append(int(z[0]))
    ing.append(sorted(z[1:]))
    for k in z[1:]:
        if k not in tot_ing:
            tot_ing.append(k)
    ind.append(i-1)
    
import pandas as pd
l=[tuple(i) for i in ing]
df2 = pd.DataFrame(list(zip(no_of_ing,l,ind)),columns=['no of ingredients','ingredients','pizza no'])
df2 = df2.sort_values(by=['no of ingredients'])
df1 = df2.groupby('ingredients')['pizza no'].apply(list).reset_index(name='pizza nos')
df1['no of ingredients'] = [len(x) for x in df1['ingredients']]
df1 = df1.sort_values(by=['no of ingredients'])
df1['frequency'] = [len(x) for x in df1['pizza nos']]
df1=df1.reset_index()
df=df1.copy()

d=t2+t3+t4
p=2*t2+3*t3+4*t4

import math
def wont_get_pizza(total_pizza,t2,t3,t4,p):
    if total_pizza<p:
        t=total_pizza-p
        t=abs(t)
        if t>4*t4:
            t=t-4*t4
            t4=0
            t3=math.floor((3*t3-t)/3)
        else:
            t4=math.floor((4*t4-t)/4)
    return t2,t3,t4

t2,t3,t4=wont_get_pizza(total_pizza,t2,t3,t4,p)

def delivery(t2,t3,t4,df):
    team=[]
    s=0
    i=0
    j=len(df)-1
    while(t2!=0):
        l=[]
        l.append(2)
        if len(df['pizza nos'][i])>0:
            l.append(df['pizza nos'][i].pop())
        else:
            i=i+1
            l.append(df['pizza nos'][i].pop())
        
        if len(df['pizza nos'][j])>0:
            l.append(df['pizza nos'][j].pop())
        else:
            j=j-1
            l.append(df['pizza nos'][j].pop())
        x=list(df['ingredients'][i])
        y=list(df['ingredients'][j])
        x.extend(y)
        x=set(x)
        x=len(x)
        #l.append(x**2)
        s=s+x**2
        team.append(l)
        t2=t2-1
    k=i+1   
    while(t3!=0):
        l=[]
        l.append(3)
        if len(df['pizza nos'][i])>0:
            l.append(df['pizza nos'][i].pop())
        else:
            i=i+1
            while(len(df['pizza nos'][i])==0):
                i=i+1
            l.append(df['pizza nos'][i].pop())
        
        if len(df['pizza nos'][k])>0:
            l.append(df['pizza nos'][k].pop())
        else:
            k=k+1
            while(len(df['pizza nos'][k])==0):
                k=k+1
            l.append(df['pizza nos'][k].pop())
        
        if len(df['pizza nos'][j])>0:
            l.append(df['pizza nos'][j].pop())
        else:
            j=j-1
            l.append(df['pizza nos'][j].pop())
        x=list(df['ingredients'][i])
        z=list(df['ingredients'][k])
        y=list(df['ingredients'][j])
        z.extend(y)
        x.extend(z)
        x=set(x)
        x=len(x)
        #l.append(x**2)
        s=s+x**2
        team.append(l)
        t3=t3-1
    gg=j-1
    while(t4!=0):
        l=[]
        l.append(4)
        if len(df['pizza nos'][i])>0:
            l.append(df['pizza nos'][i].pop())
        else:
            i=i+1
            while(len(df['pizza nos'][i])==0):
                i=i+1
            l.append(df['pizza nos'][i].pop())
        
        if len(df['pizza nos'][k])>0:
            l.append(df['pizza nos'][k].pop())
        else:
            k=k+1
            while(len(df['pizza nos'][k])==0):
                k=k+1
            l.append(df['pizza nos'][k].pop())
            
        if len(df['pizza nos'][j])>0:
            l.append(df['pizza nos'][j].pop())
        else:
            j=j-1
            while(len(df['pizza nos'][j])==0):
                j=j-1
            l.append(df['pizza nos'][j].pop())
            
        if len(df['pizza nos'][gg])>0:
            l.append(df['pizza nos'][gg].pop())
        else:
            gg=gg-1
            while(len(df['pizza nos'][gg])==0):
                gg=gg-1
            l.append(df['pizza nos'][gg].pop())
        x=list(df['ingredients'][i])
        z=list(df['ingredients'][k])
        zz=list(df['ingredients'][j])
        y=list(df['ingredients'][gg])
        z.extend(y)
        x.extend(zz)
        x.extend(z)
        x=set(x)
        x=len(x)
        #l.append(x**2)
        s=s+x**2
        team.append(l)
        t4=t4-1
    return team, s   
                
deliveries=[]
score=0
deliveries,score=delivery(t2,t3,t4,df)    