#Module/program name: AddIngAmt.py
#date created       : 29/10/2021
#created by         : Shannen
#ammended by        : HanQi
#purpose            : Add ingredient amount interface
#libraries          : IngMain.py as M2
#File No.3

import IngMain as M2

def UnitCo():
    global ing,ingUnit,ingAmt
    print("\tAdd ingredient quantity --->")
    ing=input         ("\tEnter Ingredient                : ")
    ingUnit=input     ("\tEnter Unit(tbsp,cup,g,kg,l,ml,-): ")
    ingAmt=input      ("\tEnter quantity                  : ")
#unit conversion
    if ingUnit=="tbsp":
        ingAmt*=4.2
        print("\tUnit converted to g")
    elif ingUnit=="cup":
        ingAmt*=128
        print("\tUnit converted to g")
    elif ingUnit=="g":
        pass
        print("\tUnit remained as g")
    elif ingUnit=="kg":
        ingAmt*=1000
        print("\tUnit converted to g")
    elif ingUnit=="l":
        ingAmt*=1000
        print("\tUnit converted to g")
    elif ingUnit=="ml":
        pass
        print("\tUnit converted to g")
    elif ingUnit=="-":
        pass
        print("\tUnit remained as \'-\'")
    else:
        print("\tIncorrect ingredient unit!")
        UnitCo()
UnitCo()

def CalAmt():
    if ingAmt.isdigit()==False:
        print("\tIncorrect quantity entered!")
        UnitCo()
    else:
    #add entered amount into original amount
        for i in range(0,len(M2.ingLst)):
            if ing in M2.ingLst:
                if ing==M2.ingLst[i]:
                    M2.ingAmtLst[i]+=float(ingAmt)
                    print("\tQuantity of %s has changed to: %.2f"%(M2.ingLst[i],M2.ingAmtLst[i]))
            else:
                print("Ingredient not in list!")
                M2.disM2()
        keyU=input("\tEnter <U> to view updated ingredient list; <Q>uit: ")
        if keyU.upper()=="U":
            M2.disM2()
        if keyU.upper()=="B":
            import BakingRecipeCal as MM
            MM.disMM()
CalAmt()



        
    
