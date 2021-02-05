print ("Welcome to GPA Calculator v1.0 \n\n")

def GPCalc(Grade,CR):
    Scale = {"A+":4.2,"A":4.0,"A-":3.7,"B+":3.3,"B":3.0,"B-":2.7,"C+":2.3,"C":2.0,"C-":1.5,"D":1.0,"F":0.0}
    #Combacts invlaid inputs - eg: a, 5, etc.
    try:
        GP = Scale[Grade]*CR
    except KeyError:
        print("Invalid Grade")
        GP = 0
    return GP

def Input():
    print ("\n to continue adding grades enter 1, to end enter 0 \n")
    #Combacts non integer inputs
    try:
        contn = int(input("Would you like to add another grade:"))
    except ValueError:
        contn = 0
    print("\n")
    if contn == 1:
        contn = True
    else:
        print ("\n Are you sure you have added all the subjects? Yes = 1, No = 0")
        contn = int(input("Your Answer:"))
        if contn == 1:
            contn = False
        else:
            contn = True
            print("\n")
    return contn

def GPACalc():
    TCR, CGP = 0, 0
    contn = True
    while contn == True:
        Grade = input("Enter Your Grade:")
        #Combacts invlaid inputs
        try:
            CR = float(input("Input Your Credits for the Grade:"))
        except ValueError:
            print ("\n Invalid Value - Expected an Integer/Float")
            CR = float(input("Input Your Credits for the Grade:"))
        GP = GPCalc(Grade,CR)
        #Combacts invlaid inputs
        if GP == 0:
            contn = Input()
            continue
        TCR = TCR + CR
        CGP = CGP + GP
        contn = Input()
    GPA = CGP/TCR
    GPA = round(GPA,2)
    return GPA
        
        

print("\n\n", "Your GPA = ",GPACalc())

print("\n\n (c) Suharda Silva - 2020")


Exit = input("\n\n Press Enter to Exit:")
exit()
