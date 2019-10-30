import csv
weight = 0
cls = "Maintenance not needed"
req = csv.DictReader(open("requirement222.csv"))
std = csv.DictReader(open("studentdetails222.csv"))
wl = []
tl = []
sl = []
idd = []
vc = []
mx  =[]
tweights = []
rweights = []
for spl in std:
    if int(spl['eligibility'])==1:
        idd.append(spl['id'])
        sl.append(spl['specilization'])
        for sp in req:
            print("usefhuysehngusdngusn")
            if spl['specilization']==sp['specialization']:
                print("there is requirnment of a ",spl['specilization'])
                print("send info about location is to")
                print(spl['first_name'],spl['last_name'],spl['id'])
                print("E-mail id",spl['email'])
                print('location is',sp['location'])
                #break;
            
print(idd)
            
#for id,el in zip(idd,sl):
#    print("requirnment of doctors are")
#    print(id,el)
#for sp in req:
 #   vc.append(sp['vacancy'])
#for i in vc:
 #   if (i)>=(i):
  #      print('hgygugu')
   #     print(i)
#for i in range(0,len(vc)-1):
#    if vc[i]>vc[i+1]:
#        mx.append(vc[i])
#    else:
#        mx.append(vc[i+1])
    
 #   print("djeede")

#print(vc)
#print(mx)    

    
    #if int(sp['vacancy'])>=int(sp['vacancy'])
    
print('run ho rha h')
