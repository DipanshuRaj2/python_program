sub1=int(input("enter the first marks of subject"))
sub2=int(input("enter the second marks of subject"))
sub3=int(input("enter the third marks of subject"))
sub4=int(input("enter the fourth marks of subject"))
percentage=(sub1+sub2+sub3+sub4)/400
result=percentage*100
if(result>75):
    print("distinction")
elif(result>=60 and result<=75):
    print("1st division")
elif(result>=50 and result<=59.9):
    print("second divsion")
elif(result>=40 and result<=49.9):
    print("third division")
else:
    print("fail")