import random
import time
import datetime
import tkinter.messagebox
from tkinter import *

root=Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant Management System")
root.configure(background= 'Cadet Blue')

Tops= Frame(root, bg='Cadet Blue', bd=20, pady =5, relief=RIDGE)
Tops.pack(side=TOP)

lblTitle =Label(Tops, font=('arial',58,'bold'),text='Restaurant Management System',bd=21,bg='Cadet Blue',fg='Cornsilk',justify=CENTER)
lblTitle.grid(row=0,column=0)

ReceiptCal_F= Frame(root, bg='Powder Blue', bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=6, relief=RIDGE)
Cal_F.pack(side=TOP)
Receipt_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=4, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame= Frame(root, bg='Cadet Blue', bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame, bg='Powder Blue', bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame, bg='Cadet Blue', bd=10)
Drinks_F.pack(side=TOP)

Drinks_F=Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
Drinks_F.pack(side=LEFT)
Maindish_F=Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
Maindish_F.pack(side=RIGHT)

#===========================================Variables==============================================

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder= StringVar()
Receipt_Ref= StringVar()
PaidTax= StringVar()
SubTotal= StringVar()
TotalCost= StringVar()
CostofDishes= StringVar()
CostofDrinks= StringVar()
ServiceCharge= StringVar()

text_Input= StringVar()
operator=""

E_thumsup=StringVar()
E_Redbull=StringVar()
E_Sevenup=StringVar()
E_Bira=StringVar()
E_Fanta=StringVar()
E_Coke=StringVar()
E_Sprite=StringVar()
E_AppyFiz=StringVar()

E_Pizza=StringVar()
E_PaneerMasala=StringVar()
E_Paasta=StringVar()
E_Momos=StringVar()
E_Hybiryani=StringVar()
E_MalaiChaap=StringVar()
E_ButterNaan=StringVar()
E_Chefspecial=StringVar()

E_thumsup.set("0")
E_Redbull.set("0")
E_Sevenup.set("0")
E_Bira.set("0")
E_Fanta.set("0")
E_Coke.set("0")
E_Sprite.set("0")
E_AppyFiz.set("0")

E_Pizza.set("0")
E_PaneerMasala.set("0")
E_Paasta.set("0")
E_Momos.set("0")
E_Hybiryani.set("0")
E_MalaiChaap.set("0")
E_ButterNaan.set("0")
E_Chefspecial.set("0")

DateofOrder.set(time.strftime("%d/%m/%Y"))

#===========================================Function Declaration======================================
class funcdeclare:
    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Exit", "Are you sure?")
        if iExit>0:
            root.destroy()
            return

    def Reset(self):
        E_thumsup.set("0")
        E_Redbull.set("0")
        E_Sevenup.set("0")
        E_Bira.set("0")
        E_Fanta.set("0")
        E_Coke.set("0")
        E_Sprite.set("0")
        E_AppyFiz.set("0")

        E_Pizza.set("0")
        E_PaneerMasala.set("0")
        E_Paasta.set("0")
        E_Momos.set("0")
        E_Hybiryani.set("0")
        E_MalaiChaap.set("0")
        E_ButterNaan.set("0")
        E_Chefspecial.set("0")

        CostofDishes.set("0")
        CostofDrinks.set("0")
        ServiceCharge.set("0")
        SubTotal.set("0")
        PaidTax.set("0")
        TotalCost.set("0")

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)

        txtthumsup.configure(state =DISABLED)
        txtRedbull.configure(state=DISABLED)
        txtSevenup.configure(state=DISABLED)
        txtBira.configure(state=DISABLED)
        txtFanta.configure(state=DISABLED)
        txtCoke.configure(state=DISABLED)
        txtSprite.configure(state=DISABLED)
        txtAppyFiz.configure(state=DISABLED)
        txtPizza.configure(state=DISABLED)
        txtPaneerMasala.configure(state=DISABLED)
        txtPaasta.configure(state=DISABLED)
        txtMomos.configure(state=DISABLED)
        txtHybiryani.configure(state=DISABLED)
        txtMalaiChaap.configure(state=DISABLED)
        txtButterNaan.configure(state=DISABLED)
        txtChefspecial.configure(state=DISABLED)

    def CostofItem(self):
        Item1=float(E_thumsup.get())
        Item2=float(E_Redbull.get())
        Item3=float(E_Sevenup.get())
        Item4=float(E_Bira.get())
        Item5=float(E_Fanta.get())
        Item6=float(E_Coke.get())
        Item7=float(E_Sprite.get())
        Item8=float(E_AppyFiz.get())

        Item9=float(E_Pizza.get())
        Item10=float(E_PaneerMasala.get())
        Item11=float(E_Paasta.get())
        Item12=float(E_Momos.get())
        Item13=float(E_Hybiryani.get())
        Item14=float(E_MalaiChaap.get())
        Item15=float(E_ButterNaan.get())
        Item16=float(E_Chefspecial.get())

        PriceofDrinks=((Item1 * 40 ) + (Item2 * 200) + (Item3 * 40) + (Item4 * 300)
                       + (Item5 * 700) + (Item6 * 400) + (Item7 * 700) + (Item8 * 300))
        PriceofDishes=((Item9 * 200) + (Item10 * 250) + (Item11 * 230) + (Item12 * 200)
                       + (Item13 * 300) + (Item14 * 280) + (Item15 * 200) + (Item16 * 400))

        DrinksPrice="Rs", str('%.2f'%(PriceofDrinks))
        DishesPrice="Rs", str('%.2f'%(PriceofDishes))
        CostofDishes.set(DishesPrice)
        CostofDrinks.set(DrinksPrice)
        SC="Rs", str('%.2f'%(2.5))
        ServiceCharge.set(SC)

        SubTotalofITEMS="Rs", str('%.2f'%(PriceofDrinks + PriceofDishes + 2.5))
        SubTotal.set(SubTotalofITEMS)

        Tax="Rs", str('%.2f'%((PriceofDrinks + PriceofDishes + 2.5)*0.5))
        PaidTax.set(Tax)
        TT=((PriceofDrinks + PriceofDishes + 2.5) * 0.5)
        TC="Rs", str('%.2f'%(PriceofDishes + PriceofDrinks + 2.5 + TT))
        TotalCost.set(TC)


    def chkthumsup(self):
        if(var1.get()==1):
            txtthumsup.configure(state= NORMAL)
            txtthumsup.focus()
            txtthumsup.delete('0', END)
            E_thumsup.set("")
        elif(var1.get()==0):
            txtthumsup.configure(state= DISABLED)
            E_thumsup.set("0")
    def chkRedbull(self):
        if(var2.get()==1):
            txtRedbull.configure(state= NORMAL)
            txtRedbull.focus()
            txtRedbull.delete('0', END)
            E_Redbull.set("")
        elif(var2.get()==0):
            txtRedbull.configure(state= DISABLED)
            E_Redbull.set("0")
    def chkSevenup(self):
        if(var3.get()==1):
            txtSevenup.configure(state= NORMAL)
            txtSevenup.focus()
            txtSevenup.delete('0', END)
            E_Sevenup.set("")
        elif(var3.get()==0):
            txtSevenup.configure(state= DISABLED)
            E_Sevenup.set("0")
    def chkBira(self):
        if(var4.get()==1):
            txtBira.configure(state= NORMAL)
            txtBira.focus()
            txtBira.delete('0', END)
            E_Bira.set("")
        elif(var4.get()==0):
            txtBira.configure(state= DISABLED)
            E_Bira.set("0")
    def chkFanta(self):
        if(var5.get()==1):
            txtFanta.configure(state= NORMAL)
            txtFanta.focus()
            txtFanta.delete('0', END)
            E_Fanta.set("")
        elif(var5.get()==0):
            txtFanta.configure(state= DISABLED)
            E_Fanta.set("0")
    def chkCoke(self):
        if(var6.get()==1):
            txtCoke.configure(state= NORMAL)
            txtCoke.focus()
            txtCoke.delete('0', END)
            E_Coke.set("")
        elif(var6.get()==0):
            txtCoke.configure(state= DISABLED)
            E_Coke.set("0")
    def chkSprite(self):
        if(var7.get()==1):
            txtSprite.configure(state= NORMAL)
            txtSprite.focus()
            txtSprite.delete('0', END)
            E_Sprite.set("")
        elif(var7.get()==0):
            txtSprite.configure(state= DISABLED)
            E_Sprite.set("0")
    def chkAppyFiz(self):
        if(var8.get()==1):
            txtAppyFiz.configure(state= NORMAL)
            txtAppyFiz.focus()
            txtAppyFiz.delete('0', END)
            E_AppyFiz.set("")
        elif(var8.get()==0):
            txtAppyFiz.configure(state= DISABLED)
            E_AppyFiz.set("0")
    def chkPizza(self):
        if(var9.get()==1):
            txtPizza.configure(state= NORMAL)
            txtPizza.focus()
            txtPizza.delete('0', END)
            E_Pizza.set("")
        elif(var9.get()==0):
            txtPizza.configure(state= DISABLED)
            E_Pizza.set("0")
    def chkPaneerMasala(self):
        if(var10.get()==1):
            txtPaneerMasala.configure(state= NORMAL)
            txtPaneerMasala.focus()
            txtPaneerMasala.delete('0', END)
            E_PaneerMasala.set("")
        elif(var10.get()==0):
            txtPaneerMasala.configure(state= DISABLED)
            E_PaneerMasala.set("0")
    def chkPaasta(self):
        if(var11.get()==1):
            txtPaasta.configure(state= NORMAL)
            txtPaasta.focus()
            txtPaasta.delete('0', END)
            E_Paasta.set("")
        elif(var11.get()==0):
            txtPaasta.configure(state= DISABLED)
            E_Paasta.set("0")
    def chkMomos(self):
        if(var12.get()==1):
            txtMomos.configure(state= NORMAL)
            txtMomos.focus()
            txtMomos.delete('0', END)
            E_Momos.set("")
        elif(var12.get()==0):
            txtMomos.configure(state= DISABLED)
            E_Momos.set("0")
    def chkHybiryani(self):
        if(var13.get()==1):
            txtHybiryani.configure(state= NORMAL)
            txtHybiryani.focus()
            txtHybiryani.delete('0', END)
            E_Hybiryani.set("")
        elif(var13.get()==0):
            txtHybiryani.configure(state= DISABLED)
            E_Hybiryani.set("0")
    def chkMalaiChaap(self):
        if(var14.get()==1):
            txtMalaiChaap.configure(state= NORMAL)
            txtMalaiChaap.focus()
            txtMalaiChaap.delete('0', END)
            E_MalaiChaap.set("")
        elif(var14.get()==0):
            txtMalaiChaap.configure(state= DISABLED)
            E_MalaiChaap.set("0")
    def chkButterNaan(self):
        if(var15.get()==1):
            txtButterNaan.configure(state= NORMAL)
            txtButterNaan.focus()
            txtButterNaan.delete('0', END)
            E_ButterNaan.set("")
        elif(var15.get()==0):
            txtButterNaan.configure(state= DISABLED)
            E_ButterNaan.set("0")
    def chkChefspecial(self):
        if(var16.get()==1):
            txtChefspecial.configure(state= NORMAL)
            txtChefspecial.focus()
            txtChefspecial.delete('0', END)
            E_Chefspecial.set("")
        elif(var16.get()==0):
            txtChefspecial.configure(state= DISABLED)
            E_Chefspecial.set("0")
    def Receipt(self):
        txtReceipt.delete("1.0",END)
        x= random.randint(10903, 609235)
        randomRef= str(x)
        Receipt_Ref.set("BILL" + randomRef)

        txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + Receipt_Ref.get() + "\t" + DateofOrder.get() + "\n")
        txtReceipt.insert(END, 'Item:\t\t\t' + "No of Items\n")
        txtReceipt.insert(END, 'thumsup: \t\t\t\t' + E_thumsup.get() + "\n")
        txtReceipt.insert(END, 'Red Bull: \t\t\t\t' + E_Redbull.get() + "\n")
        txtReceipt.insert(END, '7Up: \t\t\t\t' + E_Sevenup.get() + "\n")
        txtReceipt.insert(END, 'Bira: \t\t\t\t' + E_Bira.get() + "\n")
        txtReceipt.insert(END, 'Fanta: \t\t\t\t' + E_Fanta.get() + "\n")
        txtReceipt.insert(END, 'Coke: \t\t\t\t' + E_Coke.get() + "\n")
        txtReceipt.insert(END, 'Sprite: \t\t\t\t' + E_Sprite.get() + "\n")
        txtReceipt.insert(END, 'AppyFiz: \t\t\t\t' + E_AppyFiz.get() + "\n")
        txtReceipt.insert(END, 'Italian Pizza: \t\t\t\t' + E_Pizza.get() + "\n")
        txtReceipt.insert(END, 'Paneer Masala: \t\t\t\t' + E_PaneerMasala.get() + "\n")
        txtReceipt.insert(END, 'White Sauce Pasta: \t\t\t\t' + E_Paasta.get() + "\n")
        txtReceipt.insert(END, 'Steamy Hot Momos: \t\t\t\t' + E_Momos.get() + "\n")
        txtReceipt.insert(END, 'Veg Hyderabadi Biryani: \t\t\t\t' + E_Hybiryani.get() + "\n")
        txtReceipt.insert(END, 'Special Malai Chaap: \t\t\t\t' + E_MalaiChaap.get() + "\n")
        txtReceipt.insert(END, 'Butter Naan : \t\t\t\t' + E_ButterNaan.get() + "\n")
        txtReceipt.insert(END, 'Chef\'s special Biryani: \t\t\t\t' + E_Chefspecial.get() + "\n")

obj=funcdeclare()

#===========================================Drinks===================================================

thumsup=Checkbutton(Drinks_F, text='Thums Up', variable=var1, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= "Powder Blue", command=obj.chkthumsup).grid(row=0,sticky=W)
Redbull=Checkbutton(Drinks_F, text='Red Bull', variable=var2, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= "Powder Blue", command=obj.chkRedbull).grid(row=1,sticky=W)
Sevenup=Checkbutton(Drinks_F, text='7 Up', variable=var3, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= "Powder Blue", command=obj.chkSevenup).grid(row=2,sticky=W)
Bira=Checkbutton(Drinks_F, text='Bira', variable=var4, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= "Powder Blue", command=obj.chkBira).grid(row=3,sticky=W)
Fanta=Checkbutton(Drinks_F, text='Fanta', variable=var5, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= "Powder Blue", command=obj.chkFanta).grid(row=4,sticky=W)
Coke=Checkbutton(Drinks_F, text='Coke', variable=var6, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= "Powder Blue", command=obj.chkCoke).grid(row=5,sticky=W)
Sprite=Checkbutton(Drinks_F, text='Sprite', variable=var7, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= "Powder Blue", command=obj.chkSprite).grid(row=6,sticky=W)
AppyFiz=Checkbutton(Drinks_F, text='Appy Fizz', variable=var8, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= "Powder Blue", command=obj.chkAppyFiz).grid(row=7,sticky=W)


#===========================================Entry Box for Drinks===========================================================

txtthumsup= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_thumsup)
txtthumsup.grid(row=0,column=1)

txtRedbull= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Redbull)
txtRedbull.grid(row=1,column=1)

txtSevenup= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Sevenup)
txtSevenup.grid(row=2,column=1)

txtBira= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Bira)
txtBira.grid(row=3,column=1)

txtFanta= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Fanta)
txtFanta.grid(row=4,column=1)

txtCoke= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Coke)
txtCoke.grid(row=5,column=1)

txtSprite= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Sprite)
txtSprite.grid(row=6,column=1)

txtAppyFiz= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_AppyFiz)
txtAppyFiz.grid(row=7,column=1)


#===========================================Main Course Dishes=================================================================

Pizza=Checkbutton(Maindish_F, text='Italian Pizza', variable=var9, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkPizza).grid(row=0,sticky=W)
PaneerMasala=Checkbutton(Maindish_F, text='Paneer Masala', variable=var10, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkPaneerMasala).grid(row=1,sticky=W)
Paasta=Checkbutton(Maindish_F, text='White Sauce Pasta', variable=var11, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue",command=obj.chkPaasta).grid(row=2,sticky=W)
Momos=Checkbutton(Maindish_F, text='Steamy Hot Momos', variable=var12, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkMomos).grid(row=3,sticky=W)
Hybiryani=Checkbutton(Maindish_F, text='Veg Hyderabadi Biryani', variable=var13, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkHybiryani).grid(row=4,sticky=W)
MalaiChaap=Checkbutton(Maindish_F, text='Special Malai Chaap', variable=var14, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkMalaiChaap).grid(row=5,sticky=W)
ButterNaan=Checkbutton(Maindish_F, text='Butter Naan', variable=var15, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkButterNaan).grid(row=6,sticky=W)
Chefspecial=Checkbutton(Maindish_F, text='Chef\'s Special ', variable=var16, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkChefspecial).grid(row=7,sticky=W)


#===========================================Entry Box for Main Course Dishes===================================================

txtPizza= Entry(Maindish_F,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_Pizza)
txtPizza.grid(row=0,column=1)
txtPaneerMasala= Entry(Maindish_F,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_PaneerMasala)
txtPaneerMasala.grid(row=1,column=1)
txtPaasta= Entry(Maindish_F,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_Paasta)
txtPaasta.grid(row=2,column=1)
txtMomos= Entry(Maindish_F,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_Momos)
txtMomos.grid(row=3,column=1)
txtHybiryani= Entry(Maindish_F,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_Hybiryani)
txtHybiryani.grid(row=4,column=1)
txtMalaiChaap= Entry(Maindish_F,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_MalaiChaap)
txtMalaiChaap.grid(row=5,column=1)
txtButterNaan= Entry(Maindish_F,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_ButterNaan)
txtButterNaan.grid(row=6,column=1)
txtChefspecial= Entry(Maindish_F,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_Chefspecial)
txtChefspecial.grid(row=7,column=1)

#=======================================================Total Cost=========================================================
lblCostofDrinks =Label(Cost_F, font=('arial',14,'bold'),text='Cost of Drinks\t',bg='Powder Blue',fg='black')
lblCostofDrinks.grid(row=0,column=0, sticky=W)
txtCostofDrinks= Entry(Cost_F, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0, column=1)

lblCostofDishes =Label(Cost_F, font=('arial',14,'bold'),text='Cost of Dishes\t',bg='Powder Blue',fg='black')
lblCostofDishes.grid(row=1,column=0, sticky=W)
txtCostofDishes= Entry(Cost_F, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=CostofDishes)
txtCostofDishes.grid(row=1, column=1)

lblServiceCharge =Label(Cost_F, font=('arial',14,'bold'),text='Service Charge\t',bg='Powder Blue',fg='black')
lblServiceCharge.grid(row=2,column=0, sticky=W)
lblServiceCharge= Entry(Cost_F, bg='white',width=40, bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=ServiceCharge)
lblServiceCharge.grid(row=2, column=1)

#=======================================================Payment Information================================================
lblPaidTax =Label(Cost_F, font=('arial',14,'bold'),text='\tPaid Tax',bg='Powder Blue',fg='black')
lblPaidTax.grid(row=0,column=2, sticky=W)
txtPaidTax= Entry(Cost_F, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=PaidTax)
txtPaidTax.grid(row=0, column=3)

lblSubTotal =Label(Cost_F, font=('arial',14,'bold'),text='\tSub Total',bg='Powder Blue',fg='black')
lblSubTotal.grid(row=1,column=2, sticky=W)
txtSubTotal= Entry(Cost_F, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=SubTotal)
txtSubTotal.grid(row=1, column=3)

lblTotalCost =Label(Cost_F, font=('arial',14,'bold'),text='\tTotal Cost',bg='Powder Blue',fg='black')
lblTotalCost.grid(row=2,column=2, sticky=W)
txtTotalCost= Entry(Cost_F, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=TotalCost)
txtTotalCost.grid(row=2, column=3)


#=======================================================Receipt============================================================

txtReceipt= Text(Receipt_F, width=46, height=12, bg='white', bd=4, font=('arial',12,'bold'))
txtReceipt.grid(row=0, column=0)

#=======================================================Buttons============================================================

btnTotal=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="Total", bg="Powder Blue", command=obj.CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="Receipt", bg="Powder Blue", command=obj.Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="Reset", bg="Powder Blue", command=obj.Reset).grid(row=0,column=2)
btnExit=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="Exit", bg="Powder Blue", command=obj.iExit).grid(row=0,column=3)

#=======================================================Calculator Display=================================================

class calcfunc:
    def btnClick(self,numbers):
        global operator
        operator= operator + str(numbers)
        text_Input.set(operator)

    def btnClear(self):
        global operator
        operator = ""
        text_Input.set("")

    def btnEquals(self):
        global operator
        sumup = str(eval(operator))
        text_Input.set(sumup)
        operator = ""

    txtDisplay= Entry(Cal_F, width=45, bg='white', bd=4, font=('arial',12,'bold'), justify=RIGHT, textvariable= text_Input)
    txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
    txtDisplay.insert(0,"0")

obj1=calcfunc()

#=======================================================Calculator Buttons=================================================

btn7=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="7", bg="Powder Blue", command=lambda:obj1.btnClick(7)).grid(row=2,column=0)
btn8=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="8", bg="Powder Blue", command=lambda:obj1.btnClick(8)).grid(row=2,column=1)
btn9=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="9", bg="Powder Blue", command=lambda:obj1.btnClick(9)).grid(row=2,column=2)
btnAdd=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="+", bg="Powder Blue", command=lambda:obj1.btnClick("+")).grid(row=2,column=3)

#=======================================================Calculator Buttons=================================================

btn4=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="4", bg="Powder Blue", command=lambda:obj1.btnClick(4)).grid(row=3,column=0)
btn5=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="5", bg="Powder Blue", command=lambda:obj1.btnClick(5)).grid(row=3,column=1)
btn6=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="6", bg="Powder Blue", command=lambda:obj1.btnClick(6)).grid(row=3,column=2)
btnSub=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="-", bg="Powder Blue", command=lambda:obj1.btnClick("-")).grid(row=3,column=3)

#=======================================================Calculator Buttons=================================================

btn1=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="1", bg="Powder Blue", command=lambda:obj1.btnClick(1)).grid(row=4,column=0)
btn2=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="2", bg="Powder Blue", command=lambda:obj1.btnClick(2)).grid(row=4,column=1)
btn3=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="3", bg="Powder Blue", command=lambda:obj1.btnClick(3)).grid(row=4,column=2)
btnMulti=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="*", bg="Powder Blue", command=lambda:obj1.btnClick("*")).grid(row=4,column=3)

#=======================================================Calculator Buttons=================================================

btn0=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="0", bg="Powder Blue", command=lambda:obj1.btnClick(0)).grid(row=5,column=0)
btnClear=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="C", bg="Powder Blue", command=obj1.btnClear).grid(row=5,column=1)
btnEquals=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="=", bg="Powder Blue", command=obj1.btnEquals).grid(row=5,column=2)
btnDiv=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="/", bg="Powder Blue", command=lambda:obj1.btnClick("/")).grid(row=5,column=3)


root.mainloop()
