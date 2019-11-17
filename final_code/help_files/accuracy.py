import csv
total=0
correct=0
wrong=0
d={'__label__NEUTRAL':1,'__label__NEGATIVE':0,'__label__POSITIVE':2}
c=0

with open('output_100.csv','rt')as f:

    data = csv.reader(f)
    for row in data:
        c+=1
        if c>1:
            k=row[2]
            st=k.find('_')
            end=k.find(',')
            total+=1
            print(row[2][st:end],row[1])
            print(row[2][st:end],row[1])
            if int(d[row[2][st:end-1]])==int(row[1]):

                correct+=1
            else:
                wrong+=1
print(total,correct,wrong)
print(correct/total)