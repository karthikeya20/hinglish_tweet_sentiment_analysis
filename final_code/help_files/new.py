import csv
d={'1':'__label__NEUTRAL','0':'__label__NEGATIVE','2':'__label__POSITIVE'}
l=[]
with open('train.csv','rt')as f:
    data = csv.reader(f)
    
    for row in data:
        l.append(row)
with open('actual_train.txt','a') as f:
    
    for i in range(len(l)):
        s=l[i][0]+' '+l[i][1]+'\n'
        f.write(s)
# l1=[]
# with open('test.csv','rt')as f:
#     data = csv.reader(f)
#     for row in data:
#         l1.append(row)
# with open('actual_test.txt','a') as f:
#     for i in range(len(l1)):
#         s=l1[i][1]+'\n'
#         f.write(s)

  