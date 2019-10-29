first_name=input("Enter your first name:")
last_name=input("Enter your last name:")
ID=int(input("Enter your ID:"))
print("Your name is %s %s and your ID is %d" %(first_name,last_name,ID))

Stop_Program=False
while Stop_Program==False:
    richter=float(input("Enter a Richter scale value:"))
    if richter>=8:
        print ("most structures fall")
        break
    elif richter <8 and richter>=7:
        print("many buildings destroyed")
        break
    elif richter <7 and richter>=6:
        print("many buildings considerbly damaged, some collapse")
        break
    elif richter<6 and richter>=4.5:
        print ("damage to poorly constructed buildings")
        break
    elif richter < 4.5 and richter>=0:
        print ("no destruction of buildings")
        break
    elif richter < 0 and richter!=-99:
        print("Negative value. Please insert a real number.")
    elif richter==-99:
        print("You have stopped the program!")
        break
