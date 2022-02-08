import random

Riigid = {}
file=open("rig.txt","r")
for line in file:
    k,v=line.strip().split(":")
    Riigid[k.strip()] = v.strip()



def main():
  global Riigid
  print("Welcome!")
  print("Select an action:")
  print()
  print(" 1 - Find the state/capital \n 2 - Add a new state and capital to the list \n 3 - Correct an error in the dictionary \n 4 - Check the knowledge of capitals and states.")
  vibor=int(input("-> "))
  if vibor not in [1,2,3,4]:
     print("Error,please enter a number from 1 to 4.")
  else:
    if vibor==1:
      gos_stol(Riigid)
    if vibor==2:
      new_stol_gos()
    if vibor==3:
      gos_stol_correction()
    else:
        gos_stol_test()




def gos_stol(r:dict):
  global Riigid
  print("Enter capital/city")
  slovo=input("-> ")
  print(Riigid.get(slovo), "<-")

def new_stol_gos():
 b=""
 c=""
 global Riigid
 print("Enter the state you want to add")
 state =str(input("-> "))
 print("Enter the capital you want to add")
 capital = str(input("-> "))
 b += str(state) + ":" + str(capital)
 c += str(capital) + ":" + str(state)
 file=open("rig.txt","a")
 file.write(b+"\n")
 file.write(c+"\n")
 print("...")
 print("Successfully saved!")

def gos_stol_correction():
    b=""
    c=""
    print("enter the state written uncorrectally")
    a=str(input("-> "))
    print("enter the capital written uncorrectally")
    b=str(input("-> "))
    if a not in Riigid and b not in Riigid:
        print("There is no written capital and state in the list")
    else:
        print("Write the state correctly")
        state=str(input("-> "))
        print("Write the capital correctly")
        capital=str(input("-> "))
        b += str(state) + ":" + str(capital)
        c += str(capital) + ":" + str(state)
        file=open("rig.txt","a")
        file.write(b+"\n")
        file.write(c+"\n")

def gos_stol_test():
    s = 0
    l=[]
    for el in Riigid.keys():
        l.append(el)
    for i in range(12):
        r_el = random.sample(l,1)[0]
        print(r_el)
        t_write = input("-> ")
        i += 1
        if t_write == Riigid[r_el]:
            print("Correct answer!")
            s = s+1
        else:
            print("Your answer is wrong =(")
    print("Do you want to know your result?")
    print("1 - Yes \n 2 - No")
    a=int(input("-> "))
    if a not in [1,2]:
        print("Error,please enter a number from 1 to 2.")
    else:
        if a==1:
            sr=((s/12)*100)
            print("You earn ",sr,"%")
        else:
            print("Have a good day!")
            




