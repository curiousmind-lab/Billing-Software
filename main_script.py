from tkinter import *
from tkinter import  messagebox
import os
bill=Tk()
bill.title("Billing Sowftware")
bill.geometry("1350x700+0+0")
bill.config(bg="lightgreen")
b_color="#585858"

title=Label(bill,text='BILLING SOFTWARE',font=("times new roman",28,"bold"),fg="white",bg=b_color,bd=5,relief="groove").pack(fill="x")

#------------- VARIABLES ----------------------

#-------- DRINKS VARIABLE ---------

maza=IntVar()
coke=IntVar()
limca=IntVar()
sprite=IntVar()
mojito=IntVar()
coffee=IntVar()
tea=IntVar()

#-------- SNACKS VARIABLE --------

momos=IntVar()
tikka=IntVar()
s_roll=IntVar()
noodles=IntVar()
pizza=IntVar()
pasta=IntVar()
burger=IntVar()

#------- MAIN COURSE VARIABLE ----

daal=IntVar()
veg=IntVar()
channa=IntVar()
paneer=IntVar()
rice=IntVar()
nan=IntVar()
roti=IntVar()

#------- BILL MENU VARIABLE ----

total_d_price=StringVar()
total_s_price=StringVar()
total_mc_price=StringVar()
d_tax=StringVar()
s_tax=StringVar()
mc_tax=StringVar()

#-----CUSTOMER DETAIL VARIABLE ----

c_name=StringVar()
c_contact=StringVar()
search_bill=StringVar()


#---------- Genrate Bill No.------
import random
global n
n=random.randint(1000,9999)
search_bill.set(n)

#----------- FUNCTION -------------

def total():
    #----- Drinks Amount And Tax ---
    d1 = int(maza.get())
    d2 = int(coke.get())
    d3 = int(limca.get())
    d4 = int(sprite.get())
    d5 = int(mojito.get())
    d6 = int(coffee.get())
    d7 = int(tea.get())

    global maza_p
    maza_p = d1*35

    global coke_p
    coke_p = d2*35

    global limca_p
    limca_p = d3*35

    global sprite_p
    sprite_p = d4*35

    global mojito_p
    mojito_p = d5*80

    global coffee_p
    coffee_p = d6*50

    global tea_p
    tea_p = d7*15

    global dtotal
    dtotal=float(maza_p + coke_p + limca_p + sprite_p + mojito_p + coffee_p + tea_p)
    total_d_price.set(str(dtotal))

    global dtax
    dtax=float(dtotal*18/100)
    d_tax.set(str(dtax))

    #----- Snacks Amount And Tax---
    s1=int(momos.get())
    s2=int(tikka.get())
    s3=int(s_roll.get())
    s4=int(noodles.get())
    s5=int(pizza.get())
    s6=int(pasta.get())
    s7=int(burger.get())

    global momos_p
    momos_p = s1*80

    global tikka_p
    tikka_p = s2*140

    global s_roll_p
    s_roll_p = s3*40

    global noodles_p
    noodles_p = s4*110

    global pizza_p
    pizza_p = s5*250

    global pasta_p
    pasta_p = s6*180

    global burger_p
    burger_p = s7*70

    global stotal
    stotal=float(momos_p + tikka_p + s_roll_p + noodles_p + pizza_p + pasta_p + burger_p)
    total_s_price.set(str(stotal))

    global stax
    stax=float(stotal*18/100)
    s_tax.set(str(stax))

    #----- MC Amount And Tax ----
    m1=int(daal.get())
    m2=int(veg.get())
    m3=int(channa.get())
    m4=int(paneer.get())
    m5=int(rice.get())
    m6=int(nan.get())
    m7=int(roti.get())

    global daal_p
    daal_p = m1*150

    global veg_p
    veg_p = m2*180

    global channa_p
    channa_p = m3*210

    global paneer_p
    paneer_p = m4*240

    global rice_p
    rice_p = m5*160

    global nan_p
    nan_p = m6*25

    global roti_p
    roti_p = m7*10

    global mctotal
    mctotal=float(daal_p + veg_p + channa_p + paneer_p + rice_p + nan_p + roti_p)
    total_mc_price.set(str(mctotal))

    global mctax
    mctax=float(mctotal*18/100)
    mc_tax.set(str(mctax))

def welcome_bill():
    global n
    textarea.delete('1.0',END)
    textarea.insert(END,"\tWelcome Webcode Retail")
    textarea.insert(END, "\n\t------------------------")
    textarea.insert(END,f"\nBill No. : {n}")
    textarea.insert(END,f"\nCustomer Name : {c_name.get()}")
    textarea.insert(END,f"\nContact No. : {c_contact.get()}")
    textarea.insert(END,"\n=============================================")
    textarea.insert(END,"\nPRODUCT\t\t\tQTY\t\tPRICES")
    textarea.insert(END,"\n=============================================")

def bill_area():
    if c_name.get()=="" or c_contact.get()=="":
        messagebox.showerror("error","fill coustomer detail")

    else:
        welcome_bill()
        if maza.get()!=0:
            textarea.insert(END,f"\nMaza\t\t\t{maza.get()}\t\t{maza_p}")
        if coke.get()!=0:
            textarea.insert(END,f"\nCoke\t\t\t{coke.get()}\t\t{coke_p}")
        if limca.get()!=0:
            textarea.insert(END,f"\nLimca\t\t\t{limca.get()}\t\t{limca_p}")
        if sprite.get()!=0:
            textarea.insert(END,f"\nSprite\t\t\t{sprite.get()}\t\t{sprite_p}")
        if mojito.get()!=0:
            textarea.insert(END,f"\nMojito\t\t\t{mojito.get()}\t\t{mojito_p}")
        if coffee.get()!=0:
            textarea.insert(END,f"\nCoffee\t\t\t{coffee.get()}\t\t{coffee_p}")
        if tea.get()!=0:
            textarea.insert(END,f"\nTea\t\t\t{tea.get()}\t\t{tea_p}")


        if momos.get()!=0:
            textarea.insert(END,f"\nMomos\t\t\t{momos.get()}\t\t{momos_p}")
        if tikka.get()!=0:
            textarea.insert(END,f"\nTikka\t\t\t{tikka.get()}\t\t{tikka_p}")
        if s_roll.get()!=0:
            textarea.insert(END,f"\nSpring Roll\t\t\t{s_roll.get()}\t\t{s_roll_p}")
        if noodles.get()!=0:
            textarea.insert(END,f"\nNoodles\t\t\t{noodles.get()}\t\t{noodles_p}")
        if pizza.get()!=0:
            textarea.insert(END,f"\nPizza\t\t\t{pizza.get()}\t\t{pizza_p}")
        if pasta.get()!=0:
            textarea.insert(END,f"\nPasta\t\t\t{pasta.get()}\t\t{pasta_p}")
        if burger.get()!=0:
            textarea.insert(END,f"\nBurger\t\t\t{burger.get()}\t\t{burger_p}")


        if daal.get()!=0:
            textarea.insert(END,f"\nDaal Fry\t\t\t{daal.get()}\t\t{daal_p}")
        if veg.get()!=0:
            textarea.insert(END,f"\nMix  Veg\t\t\t{veg.get()}\t\t{veg_p}")
        if channa.get()!=0:
            textarea.insert(END,f"\nChanna Masala\t\t\t{channa.get()}\t\t{channa_p}")
        if paneer.get()!=0:
            textarea.insert(END,f"\nButter Paneer\t\t\t{paneer.get()}\t\t{paneer_p}")
        if rice.get()!=0:
            textarea.insert(END,f"\nFried Rice\t\t\t{rice.get()}\t\t{rice_p}")
        if nan.get()!=0:
            textarea.insert(END,f"\nButter Nan\t\t\t{nan.get()}\t\t{nan_p}")
        if roti.get()!=0 :
            textarea.insert(END,f"\nTawa Roti\t\t\t{roti.get()}\t\t{roti_p}")

        textarea.insert(END, "\n---------------------------------------------")
        textarea.insert(END, f"\nNet Amount     :\t\t\t{dtotal + stotal + mctotal}")
        textarea.insert(END, f"\nTax Amount     :\t\t\t{float(dtax + stax + mctax)}")
        textarea.insert(END, "\n---------------------------------------------")
        textarea.insert(END, f"\nNet Amount     :\t\t\t{round(dtotal + stotal + mctotal + dtax + stax + mctax)}")
        save_bill()


def save_bill():
    if os.path.exists("E:/BILLS"):
        ms=messagebox.askyesno("Save Bill","do you want to save the bill")
        if ms>0:
            bill_data=textarea.get("1.0",END)
            f1=open("E:/BILLS/"+str(n)+".txt","w")
            f1.write(bill_data)
            f1.close()
        else:
            return
    else:
        os.mkdir("E://BILLS")
        ms = messagebox.askyesno("Save Bill", "do you want to save the bill")
        if ms > 0:
            bill_data = textarea.get("1.0", END)
            f1 = open("E:/BILLS/" + str(n) + ".txt", "w")
            f1.write(bill_data)
            f1.close()
        else:
            return





def clr():
    search_bill.set(0)
    # customer detail update
    c_name.set(str(" "))
    c_contact.set(str(" "))

    # drinks value update
    maza.set(int(0))
    coke.set(int(0))
    limca.set(int(0))
    sprite.set(int(0))
    mojito.set(int(0))
    coffee.set(int(0))
    tea.set(int(0))

    # snacks value update
    momos.set(int(0))
    tikka.set(int(0))
    s_roll.set(int(0))
    noodles.set(int(0))
    pizza.set(int(0))
    pasta.set(int(0))
    burger.set(int(0))

    # main course value update
    daal.set(int(0))
    veg.set(int(0))
    channa.set(int(0))
    paneer.set(int(0))
    rice.set(int(0))
    nan.set(int(0))
    roti.set(int(0))

    # total and tax value update
    total_d_price.set(int(0))
    d_tax.set(int(0))

    total_s_price.set(int(0))
    s_tax.set(int(0))

    total_mc_price.set(int(0))
    mc_tax.set(int(0))
    textarea.delete("1.0",END)

    import random
    global n
    n = random.randint(1000, 9999)
    search_bill.set(n)


def exit():
    bill.destroy()



#------------- CUSTOMER DETAIL --------------------

F1=LabelFrame(bill,text="Customer Detail",font=("times new roman",15,"bold"),fg="gold",bg=b_color,bd=5,relief="groove")
F1.place(x=0,y=60,relwidth=1)

cname_lable=Label(F1,text="Customer Name",font=("times new roman",18,"bold"),fg="white",bg=b_color).grid(row=0,column=0,padx=20,pady=5)
cname_entry=Entry(F1,textvariable=c_name,width=30,bd=3).grid(row=0,column=1,padx=20,pady=5)

phone_lable=Label(F1,text="Contact No.",font=("times new roman",18,"bold"),fg="white",bg=b_color).grid(row=0,column=2,padx=20,pady=5)
phone_entry=Entry(F1,textvariable=c_contact,width=30,bd=3).grid(row=0,column=3,padx=20,pady=5)

bill_no_lable=Label(F1,text="Bill No.",font=("times new roman",18,"bold"),fg="white",bg=b_color).grid(row=0,column=4,padx=20,pady=5)
bill_no_entry=Entry(F1,textvariable=search_bill,width=30,bd=3).grid(row=0,column=5,padx=20,pady=5)

#search_btn=Button(F1,text="Search",bd=2,font=("bold"),fg="white",bg=b_color).grid(row=0,column=6,padx=70,pady=5)


#------------- Drinks ----------------------------

F2=LabelFrame(bill,text="Drinks",font=("times new roman",13,"bold"),fg="gold",bg=b_color,bd=5,relief="groove")
F2.place(x=5,y=140,width=300,height=370)

maza_lable=Label(F2,text="Maza",font=("times new roman",15,"bold"),fg="white",bg=b_color)
maza_lable.grid(row=0,column=0,padx=5,pady=10)
maza_entry=Entry(F2,textvariable=maza,width=20,bd=5).grid(row=0,column=2,padx=12,pady=5)


coke_lable=Label(F2,text="Coke",font=("times new roman",15,"bold"),fg="white",bg=b_color)
coke_lable.grid(row=1,column=0,padx=20,pady=10)
coke_entry=Entry(F2,textvariable=coke,width=20,bd=3).grid(row=1,column=2,padx=12,pady=5)


limca_lable=Label(F2,text="Limca",font=("times new roman",15,"bold"),fg="white",bg=b_color)
limca_lable.grid(row=2,column=0,padx=20,pady=10)
limca_entry=Entry(F2,textvariable=limca,width=20,bd=3).grid(row=2,column=2,padx=12,pady=5)


sprite_lable=Label(F2,text="Sprite",font=("times new roman",15,"bold"),fg="white",bg=b_color)
sprite_lable.grid(row=3,column=0,padx=20,pady=10)
sprite_entry=Entry(F2,textvariable=sprite,width=20,bd=3).grid(row=3,column=2,padx=12,pady=5)


mojito_lable=Label(F2,text="Mojito",font=("times new roman",15,"bold"),fg="white",bg=b_color)
mojito_lable.grid(row=4,column=0,padx=20,pady=10)
mojito_entry=Entry(F2,textvariable=mojito,width=20,bd=3).grid(row=4,column=2,padx=12,pady=5)



coffee_lable=Label(F2,text="Coffee",font=("times new roman",15,"bold"),fg="white",bg=b_color)
coffee_lable.grid(row=5,column=0,padx=20,pady=10)
coffee_entry=Entry(F2,textvariable=coffee,width=20,bd=3).grid(row=5,column=2,padx=12,pady=5)


tea_lable=Label(F2,text="Tea",font=("times new roman",15,"bold"),fg="white",bg=b_color)
tea_lable.grid(row=6,column=0,padx=20,pady=10)
tea_entry=Entry(F2,textvariable=tea,width=20,bd=3).grid(row=6,column=2,padx=12,pady=5)

#----------- Snack -----------------

F3=LabelFrame(bill,text="Snacks",font=("times new roman",13,"bold"),fg="gold",bg=b_color,bd=5,relief="groove")
F3.place(x=310,y=140,width=300,height=370)

momos_lable=Label(F3,text="Momos",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=0,column=0,padx=20,pady=10)
momos_entry=Entry(F3,textvariable=momos,width=20,bd=3).grid(row=0,column=2,padx=12,pady=5)


tikka_lable=Label(F3,text="Tikka",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=1,column=0,padx=20,pady=10)
tikka_entry=Entry(F3,textvariable=tikka,width=20,bd=3).grid(row=1,column=2,padx=12,pady=5)


roll_lable=Label(F3,text="Spring Roll",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=2,column=0,padx=20,pady=10)
roll_entry=Entry(F3,textvariable=s_roll,width=20,bd=3).grid(row=2,column=2,padx=12,pady=10)


noodle_lable=Label(F3,text="Noodles",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=3,column=0,padx=20,pady=10)
noodle_entry=Entry(F3,textvariable=noodles,width=20,bd=3).grid(row=3,column=2,padx=12,pady=5)


pizza_lable=Label(F3,text="Pizza",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=4,column=0,padx=20,pady=10)
pizza_entry=Entry(F3,textvariable=pizza,width=20,bd=3).grid(row=4,column=2,padx=12,pady=5)


pasta_lable=Label(F3,text="Pasta",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=5,column=0,padx=20,pady=10)
pasta_entry=Entry(F3,textvariable=pasta,width=20,bd=3).grid(row=5,column=2,padx=12,pady=5)


burger_lable=Label(F3,text="Burger",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=6,column=0,padx=20,pady=10)
burger_entry=Entry(F3,textvariable=burger,width=20,bd=3).grid(row=6,column=2,padx=12,pady=5)

#------------- Main course ----------

F4=LabelFrame(bill,text="Main Course",font=("times new roman",13,"bold"),fg="gold",bg=b_color,bd=5,relief="groove")
F4.place(x=620,y=140,width=320,height=370)

daal_lable=Label(F4,text="Daal Fry",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=0,column=0,padx=20,pady=10)
daal_entry=Entry(F4,textvariable=daal,width=18,bd=3).grid(row=0,column=2,padx=12,pady=5)


veg_lable=Label(F4,text="Mix Veg.",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=1,column=0,padx=20,pady=10)
veg_entry=Entry(F4,textvariable=veg,width=18,bd=3).grid(row=1,column=2,padx=12,pady=5)


channa_lable=Label(F4,text="Channa Masala",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=2,column=0,padx=20,pady=10)
channa_entry=Entry(F4,textvariable=channa,width=18,bd=3).grid(row=2,column=2,padx=12,pady=5)


paneer_lable=Label(F4,text="Butter Panner",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=3,column=0,padx=20,pady=10)
paneer_entry=Entry(F4,textvariable=paneer,width=18,bd=3).grid(row=3,column=2,padx=12,pady=5)


rice_lable=Label(F4,text="Fried Rice",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=4,column=0,padx=20,pady=10)
rice_entry=Entry(F4,textvariable=rice,width=18,bd=3).grid(row=4,column=2,padx=12,pady=5)


bread_lable=Label(F4,text="Butter Nan",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=5,column=0,padx=20,pady=10)
bread_entry=Entry(F4,textvariable=nan,width=18,bd=3).grid(row=5,column=2,padx=12,pady=5)


roti_lable=Label(F4,text="Tawa Roti",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=6,column=0,padx=20,pady=10)
roti_entry=Entry(F4,textvariable=roti,width=18,bd=3).grid(row=6,column=2,padx=12,pady=5)

#----------- Bill Area -------------

F5=Frame(bill,bg="#E6E6E6",bd=5,relief="groove")
F5.place(x=950, y=140, width=395, height=370)

b_area=Label(F5,text="BILL AREA",font=("times new roman",15,"bold"),fg="black",bg="#E6E6E6",bd=5,relief="groove",anchor="center").pack(fill="x")

scroll=Scrollbar(F5,orient="vertical")
scroll.pack(side="right",fill="y")
textarea=Text(F5,yscrollcommand=scroll.set)
textarea.pack(fill="both",expand="1")
scroll.config(command=textarea.yview)

#-------- Bill Menu --------------

F6=LabelFrame(bill,text="Bill Menu",font=("times new roman",13,"bold"),fg="gold",bg=b_color,bd=5,relief="groove")
F6.place(x=0,y=520,relwidth=1)

d_price_lable=Label(F6,text="Total Drinks Price",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=0,column=0,padx=20,pady=10)
d_price_entry=Entry(F6,textvariable=total_d_price,width=15,bd=5).grid(row=0,column=1,padx=5,pady=10)


s_price_lable=Label(F6,text="Total Snacks Price",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=1,column=0,padx=20,pady=10)
s_price_entry=Entry(F6,textvariable=total_s_price,width=15,bd=3).grid(row=1,column=1,padx=5,pady=10)


m_price_lable=Label(F6,text="Total Main Course Price",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=2,column=0,padx=20,pady=10)
m_price_entry=Entry(F6,textvariable=total_mc_price,width=15,bd=3).grid(row=2,column=1,padx=5,pady=10)


dtax_price_lable=Label(F6,text="Drinks Tax",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=0,column=2,padx=20,pady=10)
dtax_price_entry=Entry(F6,textvariable=d_tax,width=15,bd=3).grid(row=0,column=3,padx=5,pady=10)


stax_price_lable=Label(F6,text="Snacks Tax",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=1,column=2,padx=20,pady=10)
stax_price_entry=Entry(F6,textvariable=s_tax,width=15,bd=3).grid(row=1,column=3,padx=5,pady=10)


maintax_price_lable=Label(F6,text="Main Course Tax",font=("times new roman",15,"bold"),fg="white",bg=b_color).grid(row=2,column=2,padx=20,pady=10)
maintax_price_entry=Entry(F6,textvariable=mc_tax,width=15,bd=3).grid(row=2,column=3,padx=5,pady=10)


F7=Frame(F6,bg="#FAFAFA",bd=5,relief="groove")
F7.place(x=690,y=13,height=120,width=570)



total_bill_btn=Button(F7,text="Total",font=("times new roman",15,"bold"),fg="black",bg="#E6E6E6",bd=5,relief="groove",anchor="center",height=2,width=9,command=total).grid(row=0,column=0,padx=6,pady=20)

genrate_bill_btn=Button(F7,text="Genrate Bill",font=("times new roman",15,"bold"),fg="black",bg="#E6E6E6",bd=5,relief="groove",anchor="center",height=2,width=9,command=bill_area).grid(row=0,column=1,padx=20,pady=20)

clr_bill_btn=Button(F7,text="Clear",font=("times new roman",15,"bold"),fg="black",bg="#E6E6E6",bd=5,relief="groove",anchor="center",height=2,width=9,command=clr).grid(row=0,column=2,padx=6,pady=20)

exit_bill_btn=Button(F7,text="Exit",font=("times new roman",15,"bold"),fg="black",bg="#E6E6E6",bd=5,relief="groove",anchor="center",height=2,width=8,command=exit).grid(row=0,column=3,padx=6,pady=20)


#-------------- Thank you -------------

end_title=Label(bill,text='THANK YOU',font=("times new roman",30,"bold"),fg="white",bg=b_color,bd=5,relief="groove").place(x=0,y=680,relwidth=1)

bill.mainloop()
