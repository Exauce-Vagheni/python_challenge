nbs = []
pexec = "oui"
while pexec == "oui":
    nb = int(input("entre votre nombre: "))
    nbs.append(nb)
    pexec=input("voulez vous saisir un autre nombre ? oui ou non: ")
print("Question 1.")
for i in nbs:    
    print(i)
for i in range(0,len(nbs)):
    sommme=sum(nbs)   
print("Question 2.")   
print(f"la somme de toutes ces nombres est:{sommme}")
len_liste=len(nbs)
moyene=sum(nbs)/len_liste
print("Question 3.")
print(f"la moyenne de toutes ces nombres est:{moyene}")
print("Question 4.")
for i in nbs:
   if(i<moyene):
      continue
print(i)
print("Question 5.")
for nbr in range(0,len(nbs)):
    modulo=nbs[nbr]%2
    if(modulo!=0):
        continue
    print(nbs[nbr])







# nbs = []
# pexec = True
# while pexec == True:
#     nb = int(input("entre votre nombre"))
#     if nb != 0:
#         nbs.append(nb)
#     elif nb==0:
#      pexec = False

#     len_liste=len(nbs)
#     moyene=sum(nbs)/len_liste
# print(f"la moyenne de toutes ces nombres est:{moyene}")

# nbs = []
# pexec = "oui"
# while pexec == "oui":
#     nb = int(input("entre votre nombre"))
#     if nb != 0:
#         nbs.append(nb)
#     elif nb==0:
#      pexec = False

#     len_liste=len(nbs)
#     moyene=sum(nbs)/len_liste
#     for i  in nbs:
#        if(i<moyene):
#           continue
#     print(i)
       
# print(f"la moyenne de toutes ces nombres est:{moyene}")