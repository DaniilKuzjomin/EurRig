

Riigid = {}
file=open("rig.txt","r")
for line in file:
    k,v=line.strip().split(":")
    Riigid[k.strip()] = v.strip()


def new_stol_gos():

    fail=open("rig.txt","a")
    fail.write(rida+"\n")
    fail.close()


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
      new_gos_stol()  




def gos_stol(r:dict):
  global Riigid
  print("Enter capital/city")
  slovo=input("-> ")
  print(Riigid.get(slovo), "<-")

def new_gos_stol():
    global Riigid
    print("Enter the state you want to add")
    state = input("-> ")
    print("Enter the capital you want to add")
    capital = input("-> ")
    new_stol_gos()