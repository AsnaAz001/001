sub1=int(input("Maths : "))
sub2=int(input("Islamiat : "))
sub3=int(input("English : "))
sub4=int(input("Science : "))
sub5=int(input("Computer : "))
Total =(sub1+sub2+sub3+sub4+sub5)      
print("Total;" ,Total)
percentage=(Total/500*100)
print("percentage;",percentage,"%;",)

if percentage <=100 and percentage >=80:
     print("this is your grade :A+")
elif  percentage <=80 and percentage >=70:
     print("this is your grade :A") 
    
elif  percentage <=70 and percentage >=65:
     print("this is your grade :B+")  

elif  percentage <=64 and percentage >=60:
     print("this is your grade :B") 
elif  percentage <=59 and percentage >=50:
     print("this is your grade :C+") 
elif  percentage <=49 and percentage >=40:
     print("this is your grade :D+")
elif  percentage <=39 and percentage >=30:
     print("this is your grade :D") 
elif percentage <100 or percentage <0:
     print("this is not valid")       
else:
     print("failed")