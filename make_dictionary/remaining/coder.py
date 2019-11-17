from gtrans import translate_text
a=int(input())
f=open('lastsplit'+str(a)+'.txt','r')
data=f.readlines()[0].strip().split()
for i in data:
    print(i,translate_text(i, 'hi', 'en'))
