import csv
import re
fh = open('murder_total_deaths.csv')
lst = list()
death = list()
count = 0
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
    print(li[0], total)

    #calculating country with higest number of deaths
    dataset = (int(total), li[0])
    death.append(dataset)
lst = sorted(death, reverse=True)
print("Highest number of death is:", lst[0])
