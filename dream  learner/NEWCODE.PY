import csv
eligibilty=0
students = csv.DictReader(open("student details222.csv"))
requirement = csv.DictReader(open("requirement222.csv"))
s1 = []
r1 = []
sstudents=[]
srequirement=[]
for row in students:
    s1.append(BO(row['eligibility'])
for param in s1:
    if param == 'True':
        print("you are eligible")
    else:
        print("not")

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
