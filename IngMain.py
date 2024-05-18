#Module/program name: IngMain.py
#date created       : 28/10/2021
#created by         : Shannen
#ammended by        : HanQi
#purpose            : Ingredient Maintainance interface
#libraries          : AddingAmt.py as AA
#File No.2

#ingredient list
ingLst=["almond","baking soda","butter","chocolate chips","egg","flour","milk","oatmeal","salt","sugar","vanilla extract"]

#ingredient unit list
ingUnitLst=["g","g","g","g","-","g","g","g","g","g","g"]

#original ingredient amount list
ingAmtLst=[378.87,624.56,253.48,643.20,4.00,56.90,87.20,34.86,456.00,354.7,54.00]


def disM2():
    print("\n")
    print("\tIngredient Maintainance Interface")
    print("\t"+"-"*60)
    print("\tIngredient \t\tUnit \t\t\tQty")
    print("\t"+"-"*60)
    print("\n")
    #ingredient (in stock) list
    for i in range(0,len(ingLst)):
        print("\t%-20s\t %5s %20.2f"%(ingLst[i],ingUnitLst[i],ingAmtLst[i]))
    print("\n")
    print("\t"+"-"*60)
    print("\t<A>dd ingredient quantity")
    print("\t<M>odify ingredient quantity")
    print("\t<Q>uit")
    print(inp2())

def inp2():
    inp2=input("\tEnter option: ")
    if inp2.upper()=="Q":
        import BakingRecipeCal as MM
        MM.disMM()
    elif inp2.upper()=="A":
        print("\tAdd ingredient quantity interface:")
        import AddingAmt as AA
    elif inp2.upper()=="M":
        print("\tModify ingredient quantity interface:")
        import ModIngAmt as MA
    else:
        print("\tInput incorrect!")
        print(disM2())
