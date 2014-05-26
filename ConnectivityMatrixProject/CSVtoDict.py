__author__ = 'mmlab'
import csv
import json
f =  open('supplementary table 3.csv', 'r')
#reader = csv.reader(f)

reader = csv.reader(f)

a = []
b = []
c = []
d = []
regions = []
ConnMat = {}
for row in reader:
    a.append(row)
    #print row
for i in a[0]:
    if not(i == '') :
        regions.append(i)
print regions
#for j in range(1,len(a)):

 #   for k in range(1,len(a[j])):
  #      b.append(a[j][k])
   # c.append(b)
    #b = []
#for l in c:
 #   print l
#for x in c:
 #   dict(zip(regions, dict(zip(regions,c)))

for i in range(1,len(regions)):
    ConnMat[a[i][0]] = dict(zip(regions, a[i][1:]))
#print ConnMat,



    #c.append(b)
#print c[0]
#print len(c[0])



#print regions
#print len(regions)



out = json.dumps( ConnMat, indent = 4 )
print out
#for i in out:
 #   print i
#print reader
#regions = []
#a = []
#b = []
#for row in reader:
 #   a.append(row)
  #  regions.append(row[''])

#for i in a:
 #   for j in i:
  #      b.append(i[j])
#print b
#print regions
#print len(regions)


