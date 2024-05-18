#Module/program name: ModIngAmt.py
#date created       : 31/10/2021
#created by         : Shannen
#ammended by        : HanQi
#purpose            : Modify ingredient interface
#libraries          : AddingAmt.py as AA
#                   : IngMain.py as M2
#File No.4

import IngMain as M2

#convert new ingredient unit to g
def newUnitCo():
    print("\tModify ingredient quantity --->")
    ingNew=input            ("\tEnter name of new ingredient                      :")
    ingNewUnit=input        ("\tEnter unit of new ingredient(tbsp,cup,g,kg,l,ml,-):")
    ingNewAmt=input("\tEnter quantity of new ingredient                  :")
    if ingNewAmt.isdigit()=="False":
            print("\tIncorrect quantity entered!")
            newUnitCo()
    else:
        #add new ingredient name to the ingLst(ingredient List)
        M2.ingLst.append(ingNew)
        global ingNewUnit, ingNewAmt
        if ingNewUnit=="tbsp":
            ingNewAmt*=4.2
            ingNewUnit="g"
            print("\tUnit converted to g")
            print("\tQuantity of %s: %.2f"%(ingNew,ingNewAmt))
        elif ingNewUnit=="cup":
            ingNewAmt*=128
            ingNewUnit="g"
            print("\tUnit converted to g")
            print("\tQuantity of %s: %.2f"%(ingNew,ingNewAmt))
        elif ingNewUnit=="g":
            pass
            print("\tUnit remained as g")
            print("\tQuantity of %s: %.2f"%(ingNew,ingNewAmt))
        elif ingNewUnit=="kg":
            ingNewAmt*=1000
            ingNewUnit="g"
            print("\tUnit converted to g")
            print("\tQuantity of %s: %.2f"%ingNew,ingNewAmt)
        elif ingNewUnit=="l":
            ingNewAmt*=1000
            ingNewUnit="g"
            print("\tUnit converted to g")
            print("\tQuantity of %s: %.2f"%(ingNew,ingNewAmt))
        elif ingNewUnit=="ml":
            ingNewUnit="g"
            print("\tUnit converted to g")
            print("Quantity of %s: %.2f"%(ingNew,ingNewAmt))
        elif ingNewUnit=="-":
            ingNewUnit="-"
            print("\tUnit remained as \'-\'")
            print("\tQuantity of %s: %.2f"%(ingNew,ingNewAmt))
        else:
            print("\tIncorrect ingredient unit!")
            print(M2.disM2)
newUnitCo()

#add unit to ingUnitLst
M2.ingUnitLst.append(ingNewUnit)

#add Amount to ingAmtLst
M2.ingAmtLst.append(ingNewAmt)

keyU2=input("\tEnter <U> to view updated ingredient list; <Q>uit:")
if keyU2.upper()=="U":
    M2.disM2()
if keyU2.upper()=="Q":
    import BakingRecipeCal as MM
    MM.disMM()
