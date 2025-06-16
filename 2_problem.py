marks1 = int(input("enter your marks1: "))
marks2 = int(input("enter your marks2: "))
marks3 = int(input("enter your marks3: "))

persantage = (100*(marks1 + marks2 + marks3))/300

if(persantage>40 and marks1>=22 and marks2>=22 and marks3>=22):
    print("you are pass here you total Persantage:",persantage)


else:
    print("you are failed fucked up",persantage)