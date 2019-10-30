import csv
data = csv.DictReader(open("Population_of_TownsVillages_of_SagarDistrict.csv"))
i=0
tp =[]
pp=[]
m=[]
vp=[]
j=0
b=0
mean=0
pmean=0
av=0
pov=[]
for dt in data:
    if dt['Type']=='Town':
        tp.append(dt['Population'])
        i=i+1
    if dt['Type']=='Village':
        vp.append(dt['Population'])
        j=j+1
print(i)
#print(tp)
a=0
for p in tp:
    pp.append(int(p))    
for pop in pp:
    a=a+pop
#here a is total [population of Town]
    
for vpp in vp:
    pov.append(int(vpp))
for v in pov:
    b=b+v
#here b is totall population of village
    #print("list of population of vilages is",pov)
av=b/j
#print("sum of population of all towns is",a)
mean=float(a/i)
#print("mean of population of town is",mean)
#print("mean of population of village is",av)
pmean=(mean+av)/2
#print(pmean)
upp=int(input("enter you idea about population"))
if upp<=pmean:
    print("80% chance that it is a village")
else:
    print("80% chances that it is a Town")


