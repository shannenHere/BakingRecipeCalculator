#Module/program name: RecMain.py
#date created       : 31/10/2021
#created by         : Shannen
#ammended by        : 
#purpose            : Recipe Maintainance Interface
#libraries          : IngMain.py as M2
#                   : AddRecAmt.py as M3a
#                   : ModRecAmt.py as M3b
#File No.5

import IngMain as M2
import AddRecAmt as M3a
import ModRecAmt as M3b

#List of recipes
RecLst=["cookie001","cookie002","cookie003","cookie004"]
#Description
RecDesLst=["Chocolate Chip Cookie","Almond Cookie","Oatmeal Raisin Cookie","Vanilla Sugar Cookie"]
#Original Amount
RecAmt=[26,19,12,9]

def disM3():
    print("\n")
    print("\tList of recipes --->")
    for i in range(0,len(RecLst)):
        print("\t<%s> %s"%(i+1,RecLst[i]))
    print("\n")
    print("\tRecipe Maintainance Interface")
    print("\t"+"-"*60)
    print("\tRecipe\t\t\t\tDescription\tQty")
    print("\t"+"-"*60)
    print("\n")
    for i in range(0,len(RecLst)):
        print("\t%9s\t%25s\t%-20d"%(RecLst[i],RecDesLst[i],RecAmt[i]))
    print("\n")
    print("\t"+"-"*60)
    print("\t<A>dd recipe quantity")
    print("\t<M>odify recipe quantity")
    print("\t<C>lear recipes")
    print("\t<Q>uit")
    print(inpM3())

#ingredient required by each recipes
#Chocolate Chip Cookie
    #2.3g baking soda;128g butter;256g chocolate chips;2 egg;4.2g salt;256g sugar;8.4g vanilla extract
ingReq1=[0,2.3,128,256,2,0,0,0,4.2,256,8.4,0,0,0,0,0]
#Almond Cookie
    #75g almond;2.1g baking soda;170g butter;1 egg;120g flour;1.05g salt;150g sugar
ingReq2=[75,2.1,170,0,1,120,0,0,1.05,8.4,0,0,0,0,0,0]
#Oatmeal Cookie
    #2.1g baking soda;115g butter;1 egg;125g flour;150g oatmeal;1.05g salt;100g sugar;4.2g vanilla extract
ingReq3=[0,2.1,115,0,1,125,0,150,1.05,100,4.2,0,0,0,0,0]
#Vanilla Sugar Cookie
    #2.1g baking soda;250g butter;1 egg;400g flour;1.05g salt;180g sugar;4.2g vanilla extract;
ingReq4=[0,2.1,250,0,1,400,0,0,1.05,180,4.2,0,0,0,0,0]
#extra recipes
ingReq5=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ingReq6=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ingReq7=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ingReq8=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ingReq9=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ingReq10=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ingReqLst=[ingReq1]+[ingReq2]+[ingReq3]+[ingReq4]+[ingReq5]+[ingReq6]+[ingReq7]+[ingReq8]+[ingReq9]+[ingReq10]
    
def inpM3():
    inpM3=input("\tEnter option: ")
    if inpM3=="1":
        print("\tRequired ingredients for recipe cookie001:")
        print("\t"+"-"*60)
        print("\tIngredient\t\t\t\tUnit\tQty")
        print("\t"+"-"*60)
        for i in range(0,len(M2.ingLst)):
            print("\t%-20s\t %5s %20.2f"%(M2.ingLst[i],M2.ingUnitLst[i],ingReq1[i]))
        print("\t"+"-"*60)
        disM3()

    elif inpM3=="2":
        print("\tRequired ingredients for recipe cookie002:")
        print("\t"+"-"*60)
        print("\tIngredient\t\t\t\tUnit\tQty")
        print("\t"+"-"*60)
        for i in range(0,len(M2.ingLst)):
            print("\t%-20s\t %5s %20.2f"%(M2.ingLst[i],M2.ingUnitLst[i],ingReq2[i]))
        print("\t"+"-"*60)
        disM3()
            
    elif inpM3=="3":
        print("\tRequired ingredients for recipe cookie003:")
        print("\t"+"-"*60)
        print("\tIngredient\t\t\t\tUnit\tQty")
        print("\t"+"-"*60)
        for i in range(0,len(M2.ingLst)):
            print("\t%-20s\t %5s %20.2f"%(M2.ingLst[i],M2.ingUnitLst[i],ingReq3[i]))
        print("\t"+"-"*60)
        disM3()

    elif inpM3=="4":
        print("\tRequired ingredients for recipe cookie004:")
        print("\t"+"-"*60)
        print("\tIngredient\t\t\t\tUnit\tQty")
        print("\t"+"-"*60)
        for i in range(0,len(M2.ingLst)):
            print("\t%-20s\t %5s %20.2f"%(M2.ingLst[i],M2.ingUnitLst[i],ingReq4[i]))
        print("\t"+"-"*60)
        disM3()
            
    elif inpM3=="5":
        print("\tRequired ingredients for recipe %s:"%RecLst[4])
        print("\t"+"-"*60)
        print("\tIngredient\t\t\t\tUnit\tQty")
        print("\t"+"-"*60)
        for i in range(0,len(M2.ingLst)):
            print("\t%-20s\t %5s %20.2f"%(M2.ingLst[i],M2.ingUnitLst[i],ingReq5[i]))
        print("\t"+"-"*60)
        disM3()        
        
    elif inpM3.upper()=="A":
        print(M3a.disM3a())
    elif inpM3=="M":
        print(M3b.inpM3b())
    elif inpM3.upper()=="C":
        RecLst.clear()
        RecDesLst.clear()
        RecAmt.clear()
        print("\tRecipes cleared.")
        keyU4=input("\tEnter <U> to view updated list; <Q>uit: ")
        if keyU4.upper()=="U":
            print(disM3())
        elif keyU4.upper()=="Q":
            import BakingRecipeCal as MM
            MM.disMM()
    elif inpM3.upper()=="Q":
        import BakingRecipeCal as MM
        MM.disMM()
    else:
        print("\tInput incorrect!")
        keyM3=input("\tPress <C> key to continue...")
        if keyM3.upper()=="C":
            inpM3()
    
    
    
    
