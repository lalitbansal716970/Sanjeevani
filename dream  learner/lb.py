import csv
#eligibilty=0
students = csv.DictReader(open("studentdetails222.csv"))
requirement = csv.DictReader(open("requirement222.csv"))
s1 = []
r1 = []
el = []
i = 1
vl =[]
sstudents=[]
srequirement=[]
for row in students:
    s1.append(int(row['eligibility']))
    el.append(row['id'])
for param in s1:
    if param == 1:
        print("you are eligible")
       # el.append(int(param['email']))
        vl.append(i)
    else:
        print("not")
    i =i+1    
print(el)
print("list of id's of eligible students") 
print(vl)
for r1 in students:
    sstudents.append(vl["specialization"])
    

#sstudents = []
#rstudents= []
#for row in students:
 #   s1.append(int(row['specialization']))
#for row in requirement:
#    r1.append(int(row['specialization']))
#for param in s1:
#    if students.specialization==requirement.specialization:
#            print("matched")
#    else:
#        print("not mach")
