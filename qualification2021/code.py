f = open("b.txt", "r")
content = f.read()
content_list = content.splitlines()
f.close()

t = content_list[0]
t = t.split()

duration=int(t[0])
intersection=int(t[1])
streets=int(t[2])
cars=int(t[3])
bonus=int(t[4])

starting=[]
ending=[]
name=[]
L=[]

for i in range(1,streets):
    z=content_list[i].split()
    starting.append(int(z[0]))
    ending.append(int(z[1]))
    name.append((z[2]))
    L.append(z[3])
    
import pandas as pd
end = pd.DataFrame(list(zip(ending,name)),columns=['end','name'])
end = end.groupby('end')['name'].apply(list).reset_index(name='names')
end['frequency'] = [len(x) for x in end['names']]
end = end.sort_values(by=['frequency'])

def schedule(end):
    fin=[]
    for i in range(len(end)):
        ints=[]
        ints.append(end['end'][i])
        
        for j in range(len(end['names'][i])):
            ints.append(end['names'][i][j])
            ints.append(str(1))
        fin.append(ints)
    return fin

fin=schedule(end)
fin