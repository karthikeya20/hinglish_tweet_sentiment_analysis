fil=open('test_data.txt','r')
fil3=open('test_changed_swag.txt','a')
l=fil.readlines()
le=len(l)
c=1
for i in range(370,le):
	q=l[i].strip().split()
	s=str(c)+'\t'+' '.join(q[1:-1])+'\t'+q[-1]
	print(s)
	fil3.write(s+'\n')
	c+=1
fil3.close()