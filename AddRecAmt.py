#Module/program name: AddRecAmt.py
#date created       : 02/11/2021
#created by         : Shannen
#ammended by        : 
#purpose            : Add Recipe Quantity Interface
#libraries          : RecMain.py as M3
#File No.6

import RecMain as M3

def disM3a():
    RecNew=input("\tEnter name of recipe          : ")
    RecAmtNew=input("\tEnter quantity of recipe added: ")
    if RecAmtNew.isdigit()=="False":
        print("\tIncorrect quantity entered!")
        disM3a()
    else:
        for i in range(0,len(M3.RecLst)):
            if RecNew in M3.RecLst:
                if RecNew==M3.RecLst[i]:
                    M3.RecAmt[0]+=int(RecAmtNew)
                    print("\tQuantity of %s has changed to %d"%(M3.RecLst[i],M3.RecAmt[i]))
            else:
                print("\tRecipe not found!")
                inpM3ab=input("\t<R>eturn to Add Recipe Interface; <Q>uit: ")
                if inpM3ab.upper()=="R":
                    print(disM3a())
                elif inpM3ab.upper()=="Q":
                    import BakingRecipeCal as MM
                    MM.disMM()
                else:
                    print("\tInput incorrect!")
                    print(disM3a())
        keyU1=input("\tEnter <U> to view updated list; <Q>uit: ")
        if keyU1.upper()=="U":
            print(M3.disM3())
        elif keyU1.upper()S=="Q":
            import BakingRecipeCal as MM
            MM.disMM()
        
