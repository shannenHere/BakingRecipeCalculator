#Module/program name: ModRecAmt.py
#date created       : 02/11/2021
#created by         : Shannen
#ammended by        : 
#purpose            : Modify Recipe Quantity Interface
#libraries          : IngMain.py as M2
#                   : RecMain.py as M3
#File No.7

import IngMain as M2
import RecMain as M3

def inpM3b():
    global Ing12new, Ing13new, Ing14new, Ing15new, Ing16new
    print("\tModify Recipe Quantity Interface")
    NewRec=input       ("\tEnter New Recipe                          : ")
    NewRecDes=input    ("\tEnter New Recipe Description              : ")
    NewRecAmt=int(input("\tEnter New Recipe Quantity                 : "))
    M3.RecLst.append(NewRec)
    M3.RecDesLst.append(NewRecDes)
    if NewRecAmt.isdigit()=="False":
        print("Incorrect quantity entered!")
        inpM3b()
    else:
        M3.RecAmt.append(NewRecAmt)
        for i in range(0,len(M2.ingLst)):
            IngNew=float(input("\tQuantity of %20s needed(%s): "%(M2.ingLst[i],M2.ingUnitLst[i])))
            if len(M3.RecLst)>4:
                for i in range(0,len(M2.ingLst)):
                    M3.ingReq5[i]+=IngNew
            elif len(M3.RecLst)>5:
                for i in range(0,len(M2.ingLst)):
                    M3.ingReq6[i]+=IngNew
            elif len(M3.RecLst)>6:
                for i in range(0,len(M2.ingLst)):
                    M3.ingReq7[i]+=IngNew
            elif len(M3.RecLst)>7:
                for i in range(0,len(M2.ingLst)):
                        M3.ingReq8[i]+=IngNew
            elif len(M3.RecLst)>8:
                for i in range(0,len(M2.ingLst)):
                        M3.ingReq9[i]+=IngNew
            elif len(M3.RecLst)>9:
                for i in range(0,len(M2.ingLst)):
                        M3.ingReq10[i]+=IngNew
            else:
                print("Ingredient out of list")
                inpM3b()
        print("\tIngredients required updated")
        inpU3=input("\tEnter <U> to view updated Recipe List; <Q>uit: ")
        if inpU3.upper()=="U":
            print(M3.disM3())
        elif inpU3.upper()=="Q":
            import BakingRecipeCal as MM
            MM.disMM()
        else:
            print("\tInput incorrect!")
            print(M3.disM3())
    
    
    
