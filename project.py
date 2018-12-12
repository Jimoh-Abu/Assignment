
import sys
print("ADMISSION CHECKER")
print("KNOW YOUR ADMISSION STATUS")
a = input("Full name: ")
b = input("Jamb registration number:")
print("Which Faculty do you want to go to?")
facultylist = ["A-Faculty of Basic medical sciences", "B-Faculty of Engineering", "C-Pharmacy", "D-Faculty of Law"]
j = 1
while(j < 5):
    for i in facultylist:
        print(j,i)
        j+=1
fac = input()

# Values for each grade
grade = {"A1":4,"B2":3.6,"B3":3.2,"C4":2.8, "C5":2.4, "C6":2.0, "D7":1.6, "E8":1.2, "F9":1.0}
if(fac=="A" or fac.lower()== "a"):
    print("Enter your grades")
    c = grade[input("English Language:")]
    d = grade[input("Mathematics:")]
    e = grade[input("Biology:")]
    f = grade[input("Chemistry:")]
    g = grade[input("Physics:")]
    total = c + d + e + f + g
    #print("total score /20: ", total)
elif(fac=="B" or fac.lower()=="b"):
    print("Enter your grades")
    c = grade[input("English Language:")]
    d = grade[input("Mathematics:")]
    f = grade[input("Chemistry:")]
    g = grade[input("Physics:")]
    h = grade[input("Futher mathematics")]
    total = c + d + h + f + g
    #print("total score /20: ", totale)
elif(fac=="C" or fac.lower()=="c"):
    print("Enter your grades")
    c = grade[input("English Language:")]
    d = grade[input("Mathematics:")]
    f = grade[input("Chemistry:")]
    g = grade[input("Physics:")]
    e = grade[input("Biology:")]
    total = c + d + e + f + g
    #print("total score /20: ", totalp)
elif(fac=="D" or fac.lower()=="d"):
    print("Enter your grades")
    c = grade[input("English Language:")]
    d = grade[input("Mathematics:")]
    i = grade[input("Lit-in-English:")]
    j = grade[input("IRK/CRK:")]
    k = grade[input("Economics:")]
    total = c + d + i + j + k
    #print("total score /20: ", totall)
#total = c*A1 + d*B2 + e*B3 + f*C4 + g*C5 + h*C6 + i*D7 + j*E8 + k*F9  #calculate average for ssce based on the grades
print("total score /20: ", total)
#collect jamb score
jamb = int(input("Jamb score/400: "))
#comfirm if jamb sore is correct
if(jamb>400):
    print("Not possible")
    sys.exit()
# make sure candidate is eligible to write post utme
if(jamb<180):
    print(a.upper(), "You cant even be allowed to write post utme. Try again next year")
    sys.exit()
jamav = jamb/8
print("Jamb average/50:",jamav)
putme = int(input("Post utme score"))
#comfirm if score is valid
if(putme>30):
    print("error")
    sys.exit()
if(putme<12):
    print("You have score more than 40% to be eligible for admission")
    sys.exit()
aggregate = total + jamav + putme# aggregate score
print("Aggregate score/ Overall score: ", aggregate)
sa = "You have been admitted into faculty of "
go = "You are not admitted"
# Check if candidate is admitted
if(fac=="A" or fac.lower()=="a" and aggregate>=80):
    print(a.upper(),sa, "Basic medical Sciences.")
elif(fac=="A" or fac.lower()=="a" and aggregate<80):
    print(a.upper(), go)
    sys.exit()
elif(fac=="B" or fac.lower()=="b" and aggregate>=79):
    print(a.upper(),sa, "Engineering")
elif(fac=="B" or fac.lower()=="b" and aggregate<79):
    print(a.upper(), go)
    sys.exit()
elif(fac=="C" or fac.lower()=="c" and aggregate>=75):
    print(a.upper(), sa, "Pharmacy")
elif(fac=="C" or fac.lower()=="c" and aggregate<75):
    print(a.upper(),go)
    sys.exit()
elif(fac=="D" or fac.lower()=="d" and aggregate>=78):
    print(a.upper(),sa,"Law")
elif(fac=="D" or fac.lower()=="d" and aggregate<78):
    print(a.upper(),go)
    sys.exit()
print("If you have been admitted kindly start your registraion.")
