f=open('a.txt','r')
data=f.readlines()
words=[]
for i in data:
    words.append(i.strip())
le=len(words)
files=[[] for i in range(20)]
for i in range(le):
   files[i%20].append(words[i])
for i in files:
    print(len(i))
for i in range(20):
    with open('./remaining/lastsplit'+str(i+1)+'.txt','w') as writ:
        writ.write(' '.join(files[i]))
