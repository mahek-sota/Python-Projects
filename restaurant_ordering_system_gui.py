from tkinter import*
total=0
num=0
service=0
root=Tk()
#...New window for the menu...
def create():
    window=Toplevel(root)
    window['background']='#76D7C4'
    label1=Label(window,text="MENU",font="algerian 22 bold",bg='#76D7C4')
    label1.place(x=620,y=5)
#................Starters.........................................
    label2=Label(window,text="Starters",font="algerian 14 bold", bg='#76D7C4')
    label2.place(x=120,y=45)
    b1=Button(window,text="Fries 100/-",font="georgia 12 ", bg='#C4EAC3')
    b1.place(x=120,y=88)
    b1.config(text="Fries 100/-", command=Fries)
    b2=Button(window,text="Paneer chilli 120/-",font="georgia 12 ", bg='#C4EAC3')
    b2.place(x=120,y=123)
    b2.config(text="Paneer chilli 120/-", command=PaneerChilli)
    b3=Button(window,text="Veg crispy 125/-",font="georgia 12 ", bg='#C4EAC3')
    b3.place(x=120,y=158)
    b3.config(text="Veg crispy 125/-", command=VegCrispy)
    b4=Button(window,text="Spring roll 150/-",font="georgia 12 ", bg='#C4EAC3')
    b4.place(x=120,y=193)
    b4.config(text="Spring roll 150/-", command=SpringRoll)
    b5=Button(window,text="Paneer tikka 180/-",font="georgia 12 ", bg='#C4EAC3')
    b5.place(x=120,y=228)
    b5.config(text="Paneer tikka 180/-", command=PaneerTikka)
    b6=Button(window,text="Dry manchurian 180/-",font="georgia 12 ", bg='#C4EAC3')
    b6.place(x=120,y=263)
    b6.config(text="Dry manchurian 180/-", command=DryMunchurian)
    b7=Button(window,text="Veg cutlets 80/-",font="georgia 12 ", bg='#C4EAC3')
    b7.place(x=120,y=298)
    b7.config(text="Veg cutlets 80/-", command=VegCutlets)
#...............Main_course.......................................
    label3=Label(window,text="Main Course",font="algerian 14 bold",bg='#76D7C4')
    label3.place(x=600,y=45)
    label6=Label(window,text="*Dals",font="algerian 14 bold",bg='#76D7C4')
    label6.place(x=600,y=72)
    b8=Button(window,text="Dal Makhani 200/-",font="georgia 12 ", bg='#C4EAC3')
    b8.place(x=600,y=108)
    b8.config(text="Dal Makhani 200/-", command=DalM)
    b9=Button(window,text="Dal fry 120/-",font="georgia 12 ", bg='#C4EAC3')
    b9.place(x=600,y=143)
    b9.config(text="Dal fry 120/-", command=DalF)
    label7=Label(window,text="*Rotis",font="algerian 14 bold",bg='#76D7C4')
    label7.place(x=600,y=178)
    b10=Button(window,text="Phulka 10/-",font="georgia 12 ", bg='#C4EAC3')
    b10.place(x=600,y=213)
    b10.config(text="Phulka 10/-", command=Phulka)
    b11=Button(window,text="Butter naan 18/-",font="georgia 12 ", bg='#C4EAC3')
    b11.place(x=600,y=248)
    b11.config(text="Butter naan 18/-", command=ButterNaan)
    b12=Button(window,text="Kulcha 15/-",font="georgia 12 ", bg='#C4EAC3')
    b12.place(x=600,y=283)
    b12.config(text="Kulcha 15/-", command=Kulcha)
    b13=Button(window,text="Stuffed kulcha 50/-",font="georgia 12 ", bg='#C4EAC3')
    b13.place(x=600,y=318)
    b13.config(text="Stuffed kulcha 50/-", command=StuffedKulcha)
    b14=Button(window,text="Tandoori roti 12/-",font="georgia 12 ", bg='#C4EAC3')
    b14.place(x=600,y=353)
    b14.config(text="Tandoori roti 12/-", command=TandooriRoti)
    label8=Label(window,text="*Veggies",font="algerian 14 bold",bg='#76D7C4')
    label8.place(x=600,y=388)
    b15=Button(window,text="Kadhai panner 130/-",font="georgia 12 ", bg='#C4EAC3')
    b15.place(x=600,y=423)
    b15.config(text="Kadhai panner 130/-", command=KadhaiPaneer)
    b16=Button(window,text="Veg kolhapuri 120/-",font="georgia 12 ", bg='#C4EAC3')
    b16.place(x=600,y=458)
    b16.config(text="Veg kolhapuri 120/-", command=VegKolhapuri)
    b17=Button(window,text="Tawa paneer 150/-",font="georgia 12 ", bg='#C4EAC3')
    b17.place(x=600,y=493)
    b17.config(text="Tawa paneer 150/-", command=TawaPaneer)
    b18=Button(window,text="Malai kofta 180/-",font="georgia 12 ", bg='#C4EAC3')
    b18.place(x=600,y=528)
    b18.config(text="Malai kofta 180/-", command=MalaiKofta)
    label8=Label(window,text="*Italian",font="algerian 14 bold",bg='#76D7C4')
    label8.place(x=600,y=563)

    b19=Button(window,text="Pan pizza 250/-",font="georgia 12 ", bg='#C4EAC3')
    b19.place(x=600,y=598)
    b19.config(text="Pan pizza 250/-", command=PanPizza)
    b20=Button(window,text="White sauce pasta 150/-",font="georgia 12 ", bg='#C4EAC3')
    b20.place(x=600,y=633)
    b20.config(text="White sauce pasta 150/-", command=WhitePasta)
    b21=Button(window,text="Red sauce pasta 150/-",font="georgia 12 ", bg='#C4EAC3')
    b21.place(x=600,y=668)
    b21.config(text="Red sauce pasta 150/-", command=RedPasta)
#...............Dessert...........................................
    label4=Label(window,text="Dessert",font="algerian 14 bold",bg='#76D7C4')
    label4.place(x=1120,y=45)
    label9=Label(window,text="*Cupcakes",font="algerian 14 bold",bg='#76D7C4')
    label9.place(x=1120,y=72)
    b22=Button(window,text="Choco lava cupcake 150/-",font="georgia 12 ", bg='#C4EAC3')
    b22.place(x=1120,y=108)
    b22.config(text="Choco lava cupcake 150/-", command=ChocoLava)
    b23=Button(window,text="Red velvet cupcake 120/-",font="georgia 12 ", bg='#C4EAC3')
    b23.place(x=1120,y=143)
    b23.config(text="Red velvet cupcake 120/-", command=RedVelvet)
    b24=Button(window,text="Oreo cupcake 130/-",font="georgia 12 ", bg='#C4EAC3')
    b24.place(x=1120,y=178)
    b24.config(text="Oreo cupcake 130/-", command=Oreo)
    b25=Button(window,text="Strawberry cupcake 100/-",font="georgia 12 ", bg='#C4EAC3')
    b25.place(x=1120,y=213)
    b25.config(text="Strawberry cupcake 100/-", command=Strawberry)
    label10=Label(window,text="*Ice-cream",font="algerian 14 bold",bg='#76D7C4')
    label10.place(x=1120,y=248)
    b26=Button(window,text="Almond fudge 80/-",font="georgia 12 ", bg='#C4EAC3')
    b26.place(x=1120,y=283)
    b26.config(text="Almond fudge 80/-", command=AlmondF)
    b27=Button(window,text="Cherry chocolate 80/-",font="georgia 12 ", bg='#C4EAC3')
    b27.place(x=1120,y=318)
    b27.config(text="Cherry chocolate 80/-", command=Cherry)
    b28=Button(window,text="Cookie cream 80/-",font="georgia 12 ", bg='#C4EAC3')
    b28.place(x=1120,y=353)
    b28.config(text="Cookie cream 80/-", command=CookieCream)
    b29=Button(window,text="Strawberry blonde 80/-",font="georgia 12 ", bg='#C4EAC3')
    b29.place(x=1120,y=388)
    b29.config(text="Strawberry blonde 80/-", command=StrawberryB)
#...............Soups.............................................
    label5=Label(window,text="Soups",font="algerian 14 bold",bg='#76D7C4')
    label5.place(x=120,y=342)
    b30=Button(window,text="Tomato soup 100/-",font="georgia 12 ", bg='#C4EAC3')
    b30.place(x=120,y=381)
    b30.config(text="Tomato soup 100/-", command=Tomato)
    b31=Button(window,text="Manchow soup 180/-",font="georgia 12 ", bg='#C4EAC3')
    b31.place(x=120,y=416)
    b31.config(text="Manchow soup 180/-", command=Manchow)
    b32=Button(window,text="spiced lentil soup 200/-",font="georgia 12 ", bg='#C4EAC3')
    b32.place(x=120,y=451)
    b32.config(text="spiced lentil soup 200/-", command=Lentil)
    b33=Button(window,text="Sweet corn soup 150/-",font="georgia 12 ", bg='#C4EAC3')
    b33.place(x=120,y=486)
    b33.config(text="Sweet corn soup 150/-", command=SweetCorn)

    b34=Button(window,text="Spinach soup 120/-",font="georgia 12 ", bg='#C4EAC3')
    b34.place(x=120,y=521)
    b34.config(text="Spinach soup 120/-", command=Spinach)
    bill=Button(window, text="Bill", font="algerian 30 ", command=createnewWindow, bg='#ABADE5')
    bill.place(x=1160, y=500)
    cancel=Button(window, text="Cancel", font="algerian 30 ", command=window.destroy, bg='#ABADE5')
    cancel.place(x=1130, y=590)
#...............Functions for the buttons of second window.........................
#...Starters...
def Fries():
    global total
    total=total+100
    return total
def PaneerChilli():
    global total
    total=total+120
    return total
def VegCrispy():
    global total
    total=total+125
    return total
def SpringRoll():
    global total
    total=total+150
    return total
def PaneerTikka():
    global total
    total=total+180
    return total
def DryMunchurian():
    global total
    total=total+180
    return total
def VegCutlets():
    global total
    total=total+80
    return total
#...Dal...
def DalM():
    global total
    total=total+200
    return total
def DalF():
    global total
    total=total+120
    return total
#...roti...
def Phulka():
    global total
    total=total+10
    return total
def Kulcha():
    global total
    total=total+15
    return total
def ButterNaan():
    global total
    total=total+18
    return total
def StuffedKulcha():
    global total
    total=total+50
    return total
def TandooriRoti():
    global total
    total=total+12
    return total
#...Veggies...
def KadhaiPaneer():
    global total
    total=total+130
    return total
def VegKolhapuri():
    global total
    total=total+120
    return total
def TawaPaneer():
    global total
    total=total+180
    return total
def MalaiKofta():
    global total
    total=total+180
    return total
#...Italian...
def PanPizza():
    global total
    total=total+250
    return total
def WhitePasta():
    global total
    total=total+150
    return total
def RedPasta():
    global total
    total=total+150
    return total
#...Desert...cakes...
def ChocoLava():
    global total
    total=total+150
    return total
def RedVelvet():
    global total
    total=total+120
    return total
def Oreo():
    global total
    total=total+130
    return total
def Strawberry():
    global total
    total=total+100
    return total
#...Desert...icecreams...
def AlmondF():
    global total
    total=total+80
    return total
def Cherry():
    global total
    total=total+80
    return total
def CookieCream():
    global total
    total=total+80
    return total
def StrawberryB():
    global total
    total=total+80
    return total
#...Soup...
def Tomato():
    global total
    total=total+100
    return total
def Manchow():
    global total
    total=total+120
    return total
def Lentil():
    global total
    total=total+200
    return total
def SweetCorn():
    global total
    total=total+150
    return total
def Spinach():
    global total
    total=total+120
    return total
tot=total
def GST():
    global total
    global num
    num=0.03*total    
    return num
def Service():
    global service
    global total
    service=0.01*total    
    return service
def grand():
    global total
    global tot
    g=GST()
    s=Service()
    tot=total+g+s
    return tot
#...Window for Invoice...
def createnewWindow():
    newWindow=Toplevel(root)
    newWindow['background']='#76D7C4'
    title=Label(newWindow, text='INVOICE',justify=CENTER,bg='#76D7C4', fg='#000000', font=('courier new',65), padx=20, pady=10, bd=2 )
    title.place(x=525,y=5)
    val1=Text(newWindow,font=('georgia',30), bg='#76D7C4')
    val1.place(x=280, y=150)
    val1.insert(END,'Total amount= Rs '+ str(total)+"/-")
    val1.config(width=35, height=2, state="disabled")
    grand()
    val2=Text(newWindow,font=('georgia',30), bg='#76D7C4')
    val2.place(x=280, y=200)
    val2.insert(END,'GST= Rs '+ str(num)+"/-")
    val2.config(width=35, height=2, state="disabled")
    val3=Text(newWindow,font=('georgia',30), bg='#76D7C4')
    val3.place(x=280, y=250)
    val3.insert(END,'Service Tax= Rs '+ str(service)+"/-")
    val3.config(width=35, height=2, state="disabled")
    val4=Text(newWindow,font=('georgia',30), bg='#76D7C4')
    val4.place(x=280, y=300)
    val4.insert(END,'Grand Total= Rs '+ str(tot)+"/-")
    val4.config(width=35, height=1, state="disabled")
root.title('Restaurant Ordering System')
root.geometry("1350x750+0+0")
root['background']='#DA9A8B'
l11=Label(root, text='   ',bg='#DA9A8B')
l12=Label(root, text='   ',bg='#DA9A8B')
l13=Label(root, text='   ',bg='#DA9A8B')
l14=Label(root, text='   ',bg='#DA9A8B')
l15=Label(root, text='   ',bg='#DA9A8B')
l11.grid()
l12.grid()
l13.grid()
l14.grid()
l15.grid()
l1=Label(root, text='Welcome to Springwood 101 Restaurant ',justify='center',bg='#DA9A8B', fg='#ffffff', font=('Times',55,'bold'), padx=20, pady=10, bd=1)
l3=Label(root, text='   ',bg='#DA9A8B')
l17=Label(root, text='   ',bg='#DA9A8B')
l18=Label(root, text='   ',bg='#DA9A8B')
l19=Label(root, text='Ordering System by C23-111 (Mahek Sota) and C23-112 (Nidhi Sureka)',justify='center', bg='#DA9A8B',fg='#000000',font=('courier new',25,'bold'), pady=10, padx=20)
l1.grid()
l3.grid()
l17.grid()
l18.grid()
l19.grid()
l4=Label(root, text='   ',bg='#DA9A8B')
l5=Label(root, text='   ',bg='#DA9A8B')
l6=Label(root, text='   ',bg='#DA9A8B')
l7=Label(root, text='   ',bg='#DA9A8B')
l8=Label(root, text='   ',bg='#DA9A8B')
l9=Label(root, text='   ',bg='#DA9A8B')
l10=Label(root, text='   ',bg='#DA9A8B')
l4.grid()
l5.grid()
l6.grid()
l7.grid()
l8.grid()
l9.grid()
l10.grid()
b1=Button(root, text='Order now', justify='center', bg='#ffffff',fg='#000000',pady=10, padx=20, font=('courier new',25,'bold'), bd=1, command=create)
b2=Button(root, text='Cancel', justify='center', bg='#ffffff',fg='#000000',pady=10, padx=20, font=('courier new',25,'bold'), bd=1, command=root.destroy)
b1.grid()
b2.grid()
root.mainloop()
