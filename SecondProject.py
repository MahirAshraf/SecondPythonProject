import csv
import re
fh = open('murder_total_deaths.csv')
lst = list()
death = list()
year = list()

count = 0
arfa = list()
print("Countries according to the total number of deaths within 1990-2016")
print("\n")
for la in fh:
    lb = la.rstrip()
    lc = lb.replace(' ', '')
    ld = lc.replace(',', ' ')
    le = ld.replace('"', '')
    lf = le.replace('Congo Dem.Rep.','CongoDemRep')
    lg = lf.replace('Congo Rep.', 'CongoRep')
    lh = lg.replace('Micronesia Fed.Sts.', 'MicronesiaFedSts')
    li = lh.split()


    #counting total deaths in each country
    total = 0
    for i in range(len(li)):
        if i>0:
            total = total + float(li[i])
    #print(li[0], total)

    #calculating ranking according to the number of highest deaths
    dataset = (int(total), li[0])
    death.append(dataset)
lst = sorted(death, reverse=True)
for i in lst:
    count = count + 1
    print(count,i)


eh = open('murder_total_deaths.csv')
next(eh)
print("\n")
print("Yearly total death")
print("\n")
for ba in eh:
    bb = ba.rstrip()
    bc = bb.replace(' ', '')
    bd = bc.replace(',', ' ')
    be = bd.replace('"', '')
    bf = be.replace('Congo Dem.Rep.', 'CongoDemRep')
    bg = bf.replace('Congo Rep.', 'CongoRep')
    bh = bg.replace('Micronesia Fed.Sts.', 'MicronesiaFedSts')
    bi = bh.split()
    bi.pop(0)

    #calculating the total number of deaths per year
    for i in range(0, len(bi)):
        bi[i] = float(bi[i])
    #print(bi)

    year.append(bi)

tot = [sum(i) for i in zip(*year)]
#print(tot)

#creating a loop for years
x = 1990
arfa = list()
while True:
    com = x
    x= x+1
    arfa.append(com)
    if x== 2017:
        break
#print(arfa)

for i in range(len(arfa)):
    print(arfa[i],tot[i])