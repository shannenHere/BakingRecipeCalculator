#Module/program name: BakingRecipeCal.py
#date created       : 28/10/2021
#created by         : Shannen
#ammended by        : HanQi
#purpose            : Main menu interface
#libraries          : datetime as dt
#                   : IngMain.py as M2
#                   : RecMain.py as M3
#                   : ModRecAmt.py as M3b
#                   : MRP.py as M4
#File No.1 

import datetime as dt
dtNow=dt.date.today()

import IngMain as M2
import RecMain as M3
import ModRecAmt as M3b
import MRP as M4

#main menu

def disMM():
    print("\n")
    print("\t"+"-"*60)
    print("\tG3 Bakery")
    print("\tBakery Recipe Calculator (Date today:%s)"%dtNow)
    print("\t"+"-"*60)
    print("\t<1> Ingredient Maintainance")
    print("\t<2> Recipe Maintainance")
    print("\t<3> Order Creation/Update")
    print("\t<4> Generate Material Requirement Plan (MRP)")
    print("\t<Q>uit")
    print("\t"+"-"*60)
    inpMM=input("\tEnter option: ")
    if inpMM.upper()=="Q":
        exit()
    elif inpMM.upper()=="1":
            M2.disM2()
    elif inpMM.upper()=="2":
            M3.disM3()
    elif inpMM.upper()=="3":
            M3b.inpM3b()
    elif inpMM.upper()=="4":
            M4.disM4()
    else:
        print("\tInput incorrect!")
        key=input("\tPress <C> key to continue...")
        if key.upper=="C":
            print(disMM())
        
disMM()
