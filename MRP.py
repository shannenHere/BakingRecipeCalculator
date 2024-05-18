#Module/program name: MRP.py
#date created       : 03/11/2021
#created by         : Shannen
#ammended by        :
#purpose            : Generate Material Requirement Plan (MRP) interface
#libraries          : datetime as dt
#                   : RecMain.py as M3
#                   : IngMain.py as M2
#                   : BakingRecipeCal.py as MM
#File No.8

import datetime as dt
dtNow=dt.date.today()

import IngMain as M2
import RecMain as M3

OrderIng=[]
for i in range(0,len(M3.ingReqLst)):
    OrderIng.append(M3.ingReqLst[i])

#Ingredient demand
dmdIng=[]
for i in range(0,len(OrderIng)):
    for j in range(0,15):
        dmdIng.append(int(OrderIng[i][j])*sum(M3.RecAmt))

#Ingredient shortfall
shrtIng=[]
for i in range(0,len(M2.ingAmtLst)):
        shrtIng.append(int(dmdIng[i])-M2.ingAmtLst[i])
    
def disM4():
    print("\n")
    print("\t"+"-"*70)
    print("\tG3 Bakery")
    print("\tMaterial Requirement Plan (MRP) (Date today:%s)"%dtNow)
    print("\t"+"-"*70)
    print("\tList of recipes --->")
    print()
    for i in range(0,len(M3.RecLst)):
        print("\t%9s\t%25s\t%-20d"%(M3.RecLst[i],M3.RecDesLst[i],M3.RecAmt[i]))
    print()
    print("\tIngredient Requirement List --->")
    print("\t"+"-"*70)
    print("\tIngredient\t\tUnit\tStock    Demand    \tShortfall")
    print("\t"+"-"*70)
    for i in range(0,len(shrtIng)):
        if shrtIng[i]<0:
            shrtIng[i]=0
    for i in range(0,len(M2.ingLst)):
        print("\t%-20s\t%1s\t%7.2f\t%10.2f\t%10.2f"%(M2.ingLst[i],M2.ingUnitLst[i],M2.ingAmtLst[i],dmdIng[i],shrtIng[i]))
    print("\n")
    print("\t"+"-"*70)
    inpTxt()


def inpTxt():
    inpTxt=input("\t<S>ave MRP; <Q>uit: ")
    if inpTxt.upper()=="S":
        print("\tMRP run results are saved in file named MRP.txt")
        f=open("MRP.txt","w")
        for i in range(0,len(M2.ingLst)):
            f.writelines("%20s %s %20.2f\n"%(M2.ingLst[i],M2.ingUnitLst[i],shrtIng[i]))
        f.close()
        inpQ6=input("\t<Q>uit:")
        if inpQ6.upper()=="Q":
            import BakingRecipeCal as MM
            MM.disMM()
    elif inpTxt.upper()=="Q":
            import BakingRecipeCal as MM
            MM.disMM()
    else:
        print("Input incorrect!")
        keyCM4=input("Enter <C> to continue...")
        if keyCM4.upper()=="C":
            print(disM4())
    

