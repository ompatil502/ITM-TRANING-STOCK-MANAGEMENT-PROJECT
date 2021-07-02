from datetime import datetime
from tkinter import *
from tkinter import font
from tkinter.font import Font
from tkinter import ttk     
from PIL import Image,ImageTk
import mysql.connector
from newsapi import NewsApiClient
import json
import requests
from requests.api import request
import webbrowser
import time
import datetime
from bs4 import BeautifulSoup

mydb = mysql.connector.connect(host='localhost',user='root',password='1234',database='stock')
print(mydb.connection_id)
cur=mydb.cursor()

class Stocks:

    def __init__(self,root):
        self.root = root
        self.root.title('STOCK MANAGEMENT SYSTEM')
        self.root.geometry('1550x800+0+0')
        self.root.configure(background = "light green")
        
        img = Image.open(r"E:\vs code\tk\1.png")
        img = img.resize((700,140),Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)


        labelimg = Label(self.root,image=self.photoimage,bd = 4 , relief=RIDGE)
        labelimg.place(x=0,y=0,width=1550,height=150)  

        home = Button(self.root , text = "HOME" ,font="cursive 20 bold" ,bg='silver',command=self.main,width = 15 ,bd=5,relief=RIDGE)
        home.place(x = 30 , y = 40 )

        quit1 = Button(self.root , text = "QUIT" ,bg='silver', font="cursive 20 bold",width = 15 ,bd=5,relief=RIDGE)
        quit1.place(x = 1200 , y = 40)
        quit1.bind("<Double-1>",quit)
        

        label_title =  Label(self.root ,text = 'STOCK MANAGEMENT',font="cursive 40 bold" , bg = "black",fg = 'gold' , bd = 4 ,relief=RIDGE)
        label_title.place(x = 0 , y = 140 , width=1550 , height=50)


        self.main_frame = Frame(self.root , bd = 4 ,relief=RIDGE)
        self.main_frame.place(x = 0 , y = 190 ,width=1550,height=620)

        label_menu =Label(self.main_frame ,text = 'MENU',font="cursive 20 bold" , bg = "black",fg = 'gold' , bd = 4 ,relief=RIDGE)
        label_menu.place(x = 0 , y = 0 , width=230 )


        but_frame = Frame(self.main_frame ,bg = 'light blue', bd = 4 ,relief=RIDGE)
        but_frame.place(x = 0 , y = 35 ,width=228,height=285)

        but_frame2 = Frame(self.main_frame ,bg= 'light blue',bd = 4 ,relief=RIDGE)
        but_frame2.place(x = 0 , y = 310 ,width=228,height=280)

        img3 = Image.open(r'E:\vs code\tk\stock1.jpg')
        img3 = img3.resize((228,280),Image.ANTIALIAS)
        self.img3 = ImageTk.PhotoImage(img3)

        label_image3 = Label(but_frame2,image=self.img3,bd=4,relief=RIDGE)
        label_image3.place(x = 0 , y  =0,width=228,height=280)

        btn =Button(but_frame , text='LIVE STOCKS',width=18 ,command=self.charts, bg = 'grey',font="cursive 15 bold",fg = 'black',cursor='hand1')
        btn.grid(row=1,column=1,pady=2)
        
        btn =Button(but_frame , text='PIVOT LINE',width=18 , command=self.CPR_Logic,bg = 'grey',font="cursive 15 bold",fg = 'black',cursor='hand1')
        btn.grid(row=2,column=1,pady=2)

        btn =Button(but_frame , text='BUDGET',width=18 , command=self.budget1, bg = 'grey',font="cursive 15 bold",fg = 'black',cursor='hand1')
        btn.grid(row=3,column=1,pady=2)

        btn =Button(but_frame , text='LIVE NEWS',width=18 , command=self.livenews , bg = 'grey',font="cursive 15 bold" ,fg = 'black',cursor='hand1')
        btn.grid(row=4,column=1,pady=2)

        btn =Button(but_frame , text='LEARNING',width=18 , bg = 'grey',font="cursive 15 bold",fg = 'black',cursor='hand1')
        btn.grid(row=5,column=1,pady=2)

        btn =Button(but_frame , text='LOGOUT',width=18 , bg = 'grey',font="cursive 15 bold",fg = 'black',cursor='hand1')
        btn.grid(row=6,column=1,pady=2)
        btn.bind("<Double-1>",quit)

        img2 = Image.open(r'E:\vs code\tk\stock2.jpg')
        img2 = img2.resize((1310,590),Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(img2)

        label_image = Label(self.main_frame,image=self.img2,bd=4,relief=RIDGE)
        label_image.place(x = 225 , y  =0,width=1310,height=590)

    def main(self):

        self.main_frame = Frame(self.root , bd = 4 ,relief=RIDGE)
        self.main_frame.place(x = 0 , y = 190 ,width=1550,height=620)

        label_menu =Label(self.main_frame ,text = 'MENU',font="cursive 20 bold" , bg = "black",fg = 'gold' , bd = 4 ,relief=RIDGE)
        label_menu.place(x = 0 , y = 0 , width=230 )


        but_frame = Frame(self.main_frame ,bg= 'light blue',bd = 4 ,relief=RIDGE)
        but_frame.place(x = 0 , y = 35 ,width=228,height=285)

        but_frame2 = Frame(self.main_frame ,bg= 'light blue',bd = 4 ,relief=RIDGE)
        but_frame2.place(x = 0 , y = 310 ,width=228,height=280)

        img3 = Image.open(r'E:\vs code\tk\stock1.jpg')
        img3 = img3.resize((228,280),Image.ANTIALIAS)
        self.img3 = ImageTk.PhotoImage(img3)

        label_image3 = Label(but_frame2,image=self.img3,bd=4,relief=RIDGE)
        label_image3.place(x = 0 , y  =0,width=228,height=280)

        btn =Button(but_frame , text='LIVE STOCKS',width=18 , command=self.charts,bg = 'grey',font="cursive 15 bold",fg = 'black',cursor='hand1')
        btn.grid(row=1,column=1,pady=2)
        
        btn =Button(but_frame , text='PIVOT LINE',width=18 , command=self.CPR_Logic,bg = 'grey',font="cursive 15 bold",fg = 'black',cursor='hand1')
        btn.grid(row=2,column=1,pady=2)

        btn =Button(but_frame , text='BUDGET',width=18 ,command=self.budget1,bg = 'grey',font="cursive 15 bold",fg = 'black',cursor='hand1')
        btn.grid(row=3,column=1,pady=2)

        btn =Button(but_frame , text='LIVE NEWS',width=18 ,bg = 'grey',command=self.livenews,font="cursive 15 bold" ,fg = 'black',cursor='hand1')
        btn.grid(row=4,column=1,pady=2)

        btn =Button(but_frame , text='LEARNING',width=18 ,bg = 'grey',font="cursive 15 bold",fg = 'black',cursor='hand1')
        btn.grid(row=5,column=1,pady=2)

        btn =Button(but_frame , text='LOGOUT',width=18 ,bg = 'grey',font="cursive 15 bold",fg = 'black',cursor='hand1')
        btn.grid(row=6,column=1,pady=2)
        btn.bind("<Double-1>",quit)

        img2 = Image.open(r'E:\vs code\tk\stock2.jpg')
        img2 = img2.resize((1310,590),Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(img2)

        label_image = Label(self.main_frame,image=self.img2,bd=4,relief=RIDGE)
        label_image.place(x = 225 , y  =0,width=1310,height=590)
    
    def rel(self):
        return(webbrowser.open_new('https://www.ril.com/getattachment/299caec5-2e8a-43b7-8f70-d633a150d07e/AnnualReport_2019-20.aspx'))
 
    def charts(self):
        self.main_frame.destroy()
        self.f10 = Frame(self.root ,bg='black' ,relief=RIDGE,padx = 150 ,pady=80)
        self.f10.place(x = 0 , y = 200 , width=1550, height=590)

        refresh  = Button(self.root , text='REFRESH' , bg='white' , command=self.charts,fg = 'black' ,font="cursive 15 bold" )
        refresh.place(x  =20 , y = 200, width=100,height=40 )
        
        #  RELIANCE

        url = 'https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI'
        r = requests.get(url)
        content  = BeautifulSoup(r.text , 'lxml')
        content = content.find('div',{'class':'inprice1 nsecp'}).text
        live_time = datetime.datetime.now()

        name = Label(self.f10 , text='RELIANCE' ,font="cursive 15 bold",bg = 'black',bd = 10 , fg = 'gold')
        name.grid(row= 1 ,column=2 )
        price = Label(self.f10 , text=content ,font="cursive 15 bold",bg = 'black',bd = 10 , fg = 'gold')
        price.grid(row= 1 ,column=4 ,padx=20)  
        annual_report = Button(self.f10 , text="VIEW ANNUAL REPORT" ,command=self.rel, bg = 'gold' , fg = 'black',font="cursive 10 bold" , bd = 2)
        annual_report.grid(row=1 , column=5  ,padx= 20)

        #    BANK NIFTY 

        url = 'https://www.moneycontrol.com/indian-indices/bank-nifty-23.html'
        r = requests.get(url)
        print(r)
        content  = BeautifulSoup(r.text , 'lxml')
        # content = content.find('div',{"class":'tab-content'})
        content = content.find('div',{'class':'inprice1'})
        content = content.find('input')
        content = content['value']
        live_time = datetime.datetime.now()

        name = Label(self.f10 , text='BANKNIFTY' ,font="cursive 15 bold",bg = 'black',bd = 10 , fg = 'gold')
        name.grid(row= 2 ,column=2)
        price = Label(self.f10 , text=content ,font="cursive 15 bold",bg = 'black',bd = 10 , fg = 'gold')
        price.grid(row= 2,column=4)  
        annual_report = Button(self.f10 , text="VIEW ANNUAL REPORT" , bg = 'gold' , fg = 'black',font="cursive 10 bold" , bd = 2)
        annual_report.grid(row=2, column=5  ,padx= 20)

        #  NIFTY 50

        url = 'https://www.moneycontrol.com/indian-indices/cnx-nifty-9.html'
        r = requests.get(url)
        print(r)
        content  = BeautifulSoup(r.text , 'lxml')
        content = content.find('div',{'class':'inprice1'})
        content = content.find('input')
        content = content['value']
        live_time = datetime.datetime.now()

        name = Label(self.f10 , text='NIFTY50' ,font="cursive 15 bold",bg = 'black',bd = 10 , fg = 'gold')
        name.grid(row= 3 ,column=2)
        price = Label(self.f10 , text=content ,font="cursive 15 bold",bg = 'black',bd = 10 , fg = 'gold')
        price.grid(row= 3,column=4)  
        annual_report = Button(self.f10 , text="VIEW ANNUAL REPORT" , bg = 'gold' , fg = 'black',font="cursive 10 bold" , bd = 2)
        annual_report.grid(row=3 , column=5  ,padx= 20)

        # M&M

        url = 'https://in.finance.yahoo.com/quote/M%26M.NS?p=M%26M.NS&.tsrc=fin-srch'
        r = requests.get(url)
        print(r)
        content  = BeautifulSoup(r.text , 'lxml')
        content = content.find('div',{'class':'D(ib) Mend(20px)'})
        content = content.find('span').text
        # content = content['value']
        live_time = datetime.datetime.now()

        name = Label(self.f10 , text='Mahindra and Mahindra Ltd.' ,font="cursive 15 bold",bg = 'black',bd = 10 , fg = 'gold')
        name.grid(row= 4 ,column=2)
        price = Label(self.f10 , text=content ,font="cursive 15 bold",bg = 'black',bd = 10 , fg = 'gold')
        price.grid(row= 4,column=4)
        annual_report = Button(self.f10 , text="VIEW ANNUAL REPORT" , bg = 'gold' , fg = 'black',font="cursive 10 bold" , bd = 2)
        annual_report.grid(row=4 , column=5  ,padx= 20)  

        # adanient
        url = 'https://in.finance.yahoo.com/quote/ADANIENT.NS?p=ADANIENT.NS&.tsrc=fin-srch'
        r = requests.get(url)
        print(r)
        content2  = BeautifulSoup(r.text , 'lxml')
        content2 = content2.find('div',{'class':'D(ib) Mend(20px)'})
        content2 = content2.find('span').text
        # content2 = content2['value']
        live_time = datetime.datetime.now()

        name = Label(self.f10 , text='ADANIENT' ,font="cursive 15 bold",bg = 'black',bd = 10 , fg = 'gold')
        name.grid(row= 5 ,column=2)
        price = Label(self.f10 , text=content2 ,font="cursive 15 bold",bg = 'black',bd = 10 , fg = 'gold')
        price.grid(row= 5,column=4)  
        annual_report = Button(self.f10 , text="VIEW ANNUAL REPORT" , bg = 'gold' , fg = 'black',font="cursive 10 bold" , bd = 2)
        annual_report.grid(row=5 , column=5  ,padx= 20)

        #  Larsen & Toubro Ltd.

        url = 'https://in.finance.yahoo.com/quote/LT.NS?p=LT.NS&.tsrc=fin-srch'
        r = requests.get(url)
        print(r)
        content  = BeautifulSoup(r.text , 'lxml')
        content = content.find('div',{'class':'D(ib) Mend(20px)'})
        content = content.find('span').text
        # content = content['value']
        live_time = datetime.datetime.now()

        name = Label(self.f10 , text='Larsen & Toubro Ltd.' ,font="cursive 15 bold",bg = 'black',bd = 10 , fg = 'gold')
        name.grid(row= 6 ,column=2)
        price = Label(self.f10 , text=content ,font="cursive 15 bold",bg = 'black',bd = 10 , fg = 'gold')
        price.grid(row= 6,column=4)  
        annual_report = Button(self.f10 , text="VIEW ANNUAL REPORT" , bg = 'gold' , fg = 'black',font="cursive 10 bold" , bd = 2)
        annual_report.grid(row=6 , column=5  ,padx= 20)

        # HDFC
        url = 'https://in.finance.yahoo.com/quote/HDFCBANK.NS?p=HDFCBANK.NS&.tsrc=fin-srch'
        r = requests.get(url)
        print(r)
        content  = BeautifulSoup(r.text , 'lxml')
        content = content.find('div',{'class':'D(ib) Mend(20px)'})
        content = content.find('span').text
        # content = content['value']
        live_time = datetime.datetime.now()

        name = Label(self.f10 , text='HDFC Bank Ltd.' ,font="cursive 15 bold",bg = 'black',bd = 10 , fg = 'gold')
        name.grid(row= 7 ,column=2)
        price = Label(self.f10 , text=content ,font="cursive 15 bold",bg = 'black',bd = 10 , fg = 'gold')
        price.grid(row= 7,column=4)  
        annual_report = Button(self.f10 , text="VIEW ANNUAL REPORT" , bg = 'gold' , fg = 'black',font="cursive 10 bold" , bd = 2)
        annual_report.grid(row=7 , column=5  ,padx= 20)

        # SBIN
        url = 'https://in.finance.yahoo.com/quote/SBIN.NS?p=SBIN.NS&.tsrc=fin-srch'
        r = requests.get(url)
        print(r)
        content  = BeautifulSoup(r.text , 'lxml')
        content = content.find('div',{'class':'D(ib) Mend(20px)'})
        content = content.find('span').text
        # content = content['value']
        live_time = datetime.datetime.now()

        name = Label(self.f10 , text='State Bank of India' ,font="cursive 15 bold",bg = 'black',bd = 10 , fg = 'gold')
        name.grid(row= 8 ,column=2)
        price = Label(self.f10 , text=content ,font="cursive 15 bold",bg = 'black',bd = 10 , fg = 'gold')
        price.grid(row= 8,column=4) 
        annual_report = Button(self.f10 , text="VIEW ANNUAL REPORT" , bg = 'gold' , fg = 'black',font="cursive 10 bold" , bd = 2)
        annual_report.grid(row=8 , column=5  ,padx= 20) 

    def livenews(self):
        self.main_frame.destroy()

        self.root.configure(background = "black")

        self.f10 = Frame(self.root ,bg='black' ,relief=RIDGE,padx = 30 ,pady=30)
        self.f10.place(x = 0 , y = 200 , width=1550, height=590)

        refresh  = Button(self.root , text='REFRESH' , bg='white' , command=self.livenews,fg = 'black' ,font="cursive 15 bold" )
        refresh.place(x  =20 , y = 200, width=100,height=40 )

        
        heading  = Button(self.root , text='LIVE NEWS SECTION (HOURLY UPDATES)' , width=60,bg='gold' , command=self.livenews,fg = 'black' ,font="cursive 15 bold" )
        heading.place(x  =400 , y = 200,height=40 )

        # self.f11 = Frame(self.f10 ,bg='black', bd =0)
        # self.f11.place(x = 150 , y = 50 , width=1200, height=490)
        # q=stock&
        get1 ='https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=d8b0c7823f59476dae19d11bc4c7df97'
        high = requests.get(get1)
        low = json.loads(high.content)
        scrollbar = Scrollbar(self.f10)
        scrollbar.pack(side=RIGHT,fill=Y)
        scrollbar1 = Scrollbar(self.f10,orient = HORIZONTAL)
        scrollbar1.pack(side=BOTTOM,fill=X)

        list = Listbox(self.f10 ,bg='black',fg='white', xscrollcommand=scrollbar.set,yscrollcommand=scrollbar.set,font="cursive 15",width=900 , height=400)

        # def weblink(self):
        #     webbrowser.open_new(self.second)

        for i in range (10):
            first = low['articles'][i]['title']
            second = low['articles'][i]['url']
            third =low['articles'][i]['description']
            list.insert(END , 'TITLE :',first )
            list.insert(END , ' ')
            list.insert(END , 'DESCRIPTION :\n', third)
            list.insert(END , ' ')
            list.insert(END , 'URL  :'+second)
            list.insert(END , ' ')

            # list.pack(pady=10)
            # lab = Label(self.f10 , text = first ).grid(row = i,column=1)
            # lab1 = Label(self.f10 , text = second ).grid(row = i+1,column=1)

        list.pack()
        scrollbar.configure(command=list.yview)
        scrollbar1.configure(command=list.xview)
       

        # list.bind("<<Button-1>>",weblink(self.second))

    def get_budget(self):

        self.f3 = Frame(self.menu1 , bd = 5 , relief=RIDGE)
        self.f3.place(x = 800 , y = 10 , width = 750 , height = 550)
    
        input = Label(self.f3 , text="BEST POSSIBLE WAYS TO INVEST IN OPTIONS" , bg = "silver",  fg = "black",font="cursive 20 bold",bd = 4 , relief=RIDGE)
        input.place(x = 5 , y = 5 , width=715 , height=60)

        self.f4 = Frame(self.f3 , bd = 5 ,relief=RIDGE)
        self.f4.place(x = 10 , y = 70 , width=700 , height=470)

       
        output = Label(self.f4 , text="FOR YOUR BUDGET WE HAVE ISSUED SOME STOCKS \n WITH NO. OF LOTS THAT YOU CAN BUY\SELL",fg = "black",font="cursive 15 bold")
        output.grid(row= 1 ,column=1,columnspan=10 , padx=60 , pady= 10)

        self.f5= Frame(self.f4 , bd = 5 )
        self.f5.place(x = 0 , y=65  ,width=700 ,height=400)

        self.main_price =self.main_price.get()
        self.loss = self.loss.get()

        niftylot= 75
        niftyprice = self.main_price/75
        niftystoploss = (self.main_price - self.loss)/75

        bankniftylot= 25
        bankniftyprice = self.main_price/25
        bankniftystoploss = (self.main_price - self.loss)/25

        reliancelot= 250
        relianceprice = self.main_price/250
        reliancestoploss = (self.main_price - self.loss)/250

        hdfclot= 550
        hdfcprice = self.main_price/550
        hdfcstoploss = (self.main_price - self.loss)/550

        sbinlot= 1500
        sbinprice = self.main_price/1500
        sbinstoploss = (self.main_price - self.loss)/1500

        mandmlot= 700
        mandmprice = self.main_price/700
        mandmstoploss = (self.main_price - self.loss)/700

        adanientlot= 1000
        adanientprice = self.main_price/1000
        adanientstoploss = (self.main_price - self.loss)/1000

        tcslot= 300
        tcsprice = self.main_price/300
        tcsstoploss = (self.main_price - self.loss)/300

        ltlot= 575
        ltprice = self.main_price/575
        ltstoploss = (self.main_price - self.loss)/575

        idealot= 70000
        ideaprice = self.main_price/70000
        ideastoploss = (self.main_price - self.loss)/70000

        name = Label(self.f5 , text="NAME", fg = "black",font="cursive 10 bold").grid(row=1,column = 1,columnspan=2,padx=50)
        name1 = Label(self.f5 , text="LOTS", fg = "black",font="cursive 10 bold").grid(row=1,column = 3,columnspan=2,padx=50)
        name2 = Label(self.f5 , text="PRICE", fg = "black",font="cursive 10 bold").grid(row=1,column = 5,columnspan=2,padx=50)
        name3 = Label(self.f5 , text="STOPLOSS/SHARE", fg = "black",font="cursive 10 bold").grid(row=1,column = 7,columnspan=2,padx=50)

        display1 = Label(self.f5 ,text='NIFTY50',fg = 'red' ,font="cursive 10 bold" ).grid(row = 2 ,column = 1,pady=2)
        display2 = Label(self.f5 ,text=niftylot,fg = 'red' ,font="cursive 10 bold" ).grid(row = 2 ,column = 3,pady=5)
        display3 = Label(self.f5 ,text=niftyprice,fg = 'red' ,font="cursive 10 bold" ).grid(row = 2 ,column = 5,pady=5)
        display4 = Label(self.f5 ,text=niftystoploss,fg = 'red' ,font="cursive 10 bold" ).grid(row = 2 ,column = 7,pady=5)

        display5 = Label(self.f5 ,text='BANKNIFTY',fg = 'red' ,font="cursive 10 bold" ).grid(row = 3 ,column = 1,pady=5)
        display6 = Label(self.f5 ,text=bankniftylot,fg = 'red' ,font="cursive 10 bold" ).grid(row = 3 ,column = 3,pady=5)
        display7 = Label(self.f5 ,text=bankniftyprice,fg = 'red' ,font="cursive 10 bold" ).grid(row = 3 ,column = 5,pady=5)
        display8 = Label(self.f5 ,text=bankniftystoploss,fg = 'red' ,font="cursive 10 bold" ).grid(row = 3 ,column = 7,pady=5)


        display9 = Label(self.f5 ,text='RELIANCE',fg = 'red' ,font="cursive 10 bold" ).grid(row = 4 ,column = 1,pady = 5)
        display10 = Label(self.f5 ,text=reliancelot,fg = 'red' ,font="cursive 10 bold" ).grid(row = 4 ,column = 3,pady = 5)
        display11 = Label(self.f5 ,text=relianceprice,fg = 'red' ,font="cursive 10 bold" ).grid(row = 4 ,column = 5,pady = 5)
        display12 = Label(self.f5 ,text=reliancestoploss,fg = 'red' ,font="cursive 10 bold" ).grid(row = 4 ,column = 7,pady = 5)

        display13 = Label(self.f5 ,text='HDFCBANK',fg = 'red' ,font="cursive 10 bold" ).grid(row = 5 ,column = 1,pady = 5)
        display14 = Label(self.f5 ,text=hdfclot,fg = 'red' ,font="cursive 10 bold" ).grid(row = 5 ,column = 3,pady = 5)
        display15 = Label(self.f5 ,text=hdfcprice,fg = 'red' ,font="cursive 10 bold" ).grid(row = 5 ,column = 5,pady = 5)
        display16 = Label(self.f5 ,text=hdfcstoploss,fg = 'red' ,font="cursive 10 bold" ).grid(row = 5 ,column = 7,pady = 5)

        display17 = Label(self.f5 ,text='SBIN',fg = 'red' ,font="cursive 10 bold" ).grid(row = 6 ,column = 1,pady = 5)
        display18 = Label(self.f5 ,text=sbinlot,fg = 'red' ,font="cursive 10 bold" ).grid(row = 6 ,column = 3,pady = 5)
        display19 = Label(self.f5 ,text=sbinprice,fg = 'red' ,font="cursive 10 bold" ).grid(row = 6 ,column = 5,pady = 5)
        display20 = Label(self.f5 ,text=sbinstoploss,fg = 'red' ,font="cursive 10 bold" ).grid(row = 6 ,column = 7,pady = 5)

        display21 = Label(self.f5 ,text='M&M',fg = 'red' ,font="cursive 10 bold" ).grid(row = 7 ,column = 1,pady = 5)
        display22 = Label(self.f5 ,text=mandmlot,fg = 'red' ,font="cursive 10 bold" ).grid(row = 7 ,column = 3,pady = 5)
        display23 = Label(self.f5 ,text=mandmprice,fg = 'red' ,font="cursive 10 bold" ).grid(row = 7 ,column = 5,pady = 5)
        display24 = Label(self.f5 ,text=mandmstoploss,fg = 'red' ,font="cursive 10 bold" ).grid(row = 7 ,column = 7,pady = 5)

        display25 = Label(self.f5 ,text='ADANIENT',fg = 'red' ,font="cursive 10 bold" ).grid(row = 8 ,column = 1,pady = 5)
        display26 = Label(self.f5 ,text=adanientlot,fg = 'red' ,font="cursive 10 bold" ).grid(row = 8 ,column = 3,pady = 5)
        display27 = Label(self.f5 ,text=adanientprice,fg = 'red' ,font="cursive 10 bold" ).grid(row = 8 ,column = 5,pady = 5)
        display28 = Label(self.f5 ,text=adanientstoploss,fg = 'red' ,font="cursive 10 bold" ).grid(row = 8 ,column = 7,pady = 5)

        display29 = Label(self.f5 ,text='TCS',fg = 'red' ,font="cursive 10 bold" ).grid(row = 9 ,column = 1,pady = 5)
        display30 = Label(self.f5 ,text=tcslot,fg = 'red' ,font="cursive 10 bold" ).grid(row = 9 ,column = 3,pady = 5)
        display31 = Label(self.f5 ,text=tcsprice,fg = 'red' ,font="cursive 10 bold" ).grid(row = 9 ,column = 5,pady = 5)
        display32 = Label(self.f5 ,text=tcsstoploss,fg = 'red' ,font="cursive 10 bold" ).grid(row = 9 ,column = 7,pady = 5)

        display33 = Label(self.f5 ,text='LT',fg = 'red' ,font="cursive 10 bold" ).grid(row = 10 ,column = 1,pady = 5)
        display34 = Label(self.f5 ,text=ltlot,fg = 'red' ,font="cursive 10 bold" ).grid(row = 10 ,column = 3,pady = 5)
        display35 = Label(self.f5 ,text=ltprice,fg = 'red' ,font="cursive 10 bold" ).grid(row = 10 ,column = 5,pady = 5)
        display36 = Label(self.f5 ,text=ltstoploss,fg = 'red' ,font="cursive 10 bold" ).grid(row = 10 ,column = 7,pady = 5)

        display37 = Label(self.f5 ,text='IDEA',fg = 'red' ,font="cursive 10 bold" ).grid(row = 11 ,column = 1,pady = 5)
        display38 = Label(self.f5 ,text=idealot,fg = 'red' ,font="cursive 10 bold" ).grid(row = 11 ,column = 3,pady = 5)
        display39 = Label(self.f5 ,text=ideaprice,fg = 'red' ,font="cursive 10 bold" ).grid(row = 11 ,column = 5,pady = 5)
        display40 = Label(self.f5 ,text=ideastoploss,fg = 'red' ,font="cursive 10 bold" ).grid(row = 11 ,column = 7,pady = 5)


        # variable = f'''THIS IS A BUDGET PANEL \n 
        # INVESTMENT IS SUBJECT TO MARKET RISK \n
        # HERE YOU WILL GET THE EXPECTED NO. OF LOTS FOR \n 
        # FOR ONLY SOME OF THE POPULAR STOCKS ONLY \n
        # ****** GIVE OF STOCKS THEY WILL BE ADDED SOON ***** \n
        # '''

        # text1 =Text(self.f4 , text= variable ,fg = "black",font="cursive 10 bold")
        # text1.grid(row=1 , column=1 , columnspan=5 ,rowspan=5)

    def budget1(self):

        self.main_frame.destroy()
        self.root.title('STOCK MANAGEMENT SYSTEM')
        self.root.geometry('1550x800+0+0')

        self.main_price = IntVar()
        self.loss  = IntVar()

        self.menu1 = Frame(self.root ,bg = 'black', bd = 5 , relief=RIDGE)
        self.menu1.place(x = 0 , y = 200 ,width=1550,height=590)

        self.f2  = Frame(self.menu1 ,bg = 'black', bd = 5 , relief=RIDGE)
        self.f2.place(x = 20 , y = 10 , width = 770 , height = 550)
    
        input = Label(self.f2 , text="BUDGET INPUTS" , bg = "black",  fg = "white",font="cursive 25 bold",bd = 4 , relief=RIDGE)
        input.place(x = 0 , y = 5 , width=760 , height=60)

        self.f3 = Frame(self.f2 ,bg = 'black', bd = 5 , relief=RIDGE)
        self.f3.place(x =5 , y = 70 ,width=720 , height=490)

        budget_label = Label(self.f3 , text= "  ENTER YOUR BUDGET", bg = "black",  fg = "white",font="cursive 20")
        budget_label.grid(row = 1 , column= 1 , padx=30 )
        
        budget_entry =  Entry(self.f3 ,textvariable=self.main_price,width=25,font="cursive 15" )
        budget_entry.grid(row = 1 , column=3 , pady = 60)

        loss_label = Label(self.f3 , text= "ACCEPTABLE LOSS", bg = "black",  fg = "white",font="cursive 20")
        loss_label.grid(row = 2 , column= 1 , padx=30 )
        
        loss_entry =  Entry(self.f3  ,textvariable=self.loss,width=25,font="cursive 15")
        loss_entry.grid(row = 2 , column=3, pady = 30)

        submit = Button(self.f3 , width=20 ,text = "GET MY BUDGET", bg = "black",  fg = "white",command=self.get_budget ,font="cursive 10")
        submit.grid(row = 3 , column= 3 ,pady= 30)

    def get_levels(self):
        self.f2  = Frame(self.menu ,bg = "chocolate1" , relief=RIDGE )
        self.f2.place(x = 775 , y = 0 , width = 750 , height = 550)

        head = Label(self.f2 ,text="CHECK THE LEVELS" ,bg = "silver",  fg = "black",font="cursive 20 bold",relief=RIDGE)
        head.place(x = 0 ,y = 0 ,width=750,height=60)

        self.extra = Frame(self.f2 ,bg = 'pale green', relief=RIDGE)
        self.extra.place(x = 10 , y = 70 ,width=720 , height=470 )

        pivot = (self.high.get() + self.low.get() + self.close.get())/3

        bc = (self.high.get() + self.low.get())/ 2

        tc =(pivot - bc) + pivot

        r1 = (2*pivot)-self.low.get()

        s1 = (2*pivot) - self.high.get()

        r2 = pivot + (r1-s1)

        s2 = pivot - (r1 - s1)

        top = f" TOP PIVOT LINE  =  {tc}"
        central = f" PIVOT LINE  =  {pivot}"
        bottom = f" BOTTOM PIVOT LINE  =  {bc}"
        res1 = f" RESISTANCE 1 =  {r1}"
        res2 = f" RESISTANCE 2  =  {r2}"
        sup1 = f" SUPPORT 1  =  {s1}"
        sup2 = f" SUPPORT 2  =  {s2}"

        top_label = Label(self.extra  ,height=1, font="Helvetica 10",bg = 'pale green',padx = 220)
        top_label.grid(row = 0 ,column=2,pady = 10)

        top_label = Label(self.extra ,text=top ,height=1,bg = 'pale green', font="Helvetica 12",padx = 220)
        top_label.grid(row = 1 ,column=2 ,pady = 10  )

        bottom_label = Label(self.extra , text= central ,height=1,bg = 'pale green', font="Helvetica 12",padx = 220)
        bottom_label.grid(row =2 ,column=2,pady = 10)

        top_label = Label(self.extra , text= bottom ,height=1,bg = 'pale green', font="Helvetica 12",padx = 220)
        top_label.grid(row = 3 ,column=2,pady= 10)
    
        r1_label = Label(self.extra , text= res1 ,height=1,bg = 'pale green', font="Helvetica 12",padx =220)
        r1_label.grid(row = 4 ,column=2,pady = 10)

        r2_label = Label(self.extra , text= res2 ,height=1,bg = 'pale green', font="Helvetica 12",padx = 220)
        r2_label.grid(row = 5 ,column=2,pady = 10)

        s1_label = Label(self.extra , text= sup1 ,height=1,bg = 'pale green', font="Helvetica 12",padx = 220)
        s1_label.grid(row = 6 ,column=2,pady = 10)

        s2_label = Label(self.extra , text= sup2 ,height=1,bg = 'pale green', font="Helvetica 12",padx = 220)
        s2_label.grid(row = 7 ,column=2,pady = 10)

        back = Button(self.extra , text = 'GO BACK' , command =self.main ,width=30)
        back.grid(row = 8 ,column=2,pady=25)

    def CPR_Logic(self):

        # self.top_level = Toplevel(self.root)
        # self.app = CPR(self.top_level)
        self.main_frame.destroy()
        self.root.title('STOCK MANAGEMENT SYSTEM')
        self.root.geometry('1550x800+0+0')

        self.menu = Frame(self.root ,bg = 'chocolate1', relief=RIDGE)
        self.menu.place(x = 0 , y = 200 ,width=1550,height=590)

        self.high = IntVar()
        self.low = IntVar()
        self.close = IntVar()

        self.f1  = Frame(self.menu ,bg = 'chocolate1', relief=RIDGE)
        self.f1.place(x = 0 , y = 0 , width = 770 , height = 550)

        input = Label(self.f1 , text="CPR INPUTS" , bg = "silver",  fg = "black",font="cursive 20 bold",bd = 4 , relief=RIDGE)
        input.place(x = 5 , y = 5 , width=760 , height=60)

        self.f2  = Frame(self.f1  ,bg = 'pale green', relief=RIDGE ,padx = 70 ,pady = 50)
        self.f2.place(x = 30 , y = 80, width = 700 , height = 450)

        high_label = Label(self.f2, text= 'ENTER THE HIGH' ,bg = 'pale green',height=1, font="Helvetica 10 bold")
        high_label.grid(row = 1 ,column=1)

        high_entry = Entry(self.f2, textvariable=self.high,width=40 ,bd = 2 )
        high_entry.grid(row = 1 ,column=3,padx=30,pady=20)

        low_label = Label(self.f2, text= 'ENTER THE LOW' ,bg = 'pale green',height=1, font="Helvetica 10 bold")
        low_label.grid(row = 2 ,column=1)

        low_entry = Entry(self.f2,textvariable=self.low,width=40 , bd = 2 )
        low_entry.grid(row = 2 ,column=3 ,padx=30,pady=20)

        close_label = Label(self.f2, text= 'ENTER THE CLOSE' ,bg = 'pale green',height=1, font="Helvetica 10 bold")
        close_label.grid(row = 3,column=1)

        close_entry = Entry(self.f2, textvariable=self.close, width=40 ,bd = 2 )
        close_entry.grid(row = 3 ,column=3,padx=30,pady=20)

        button  = Button(self.f2 , text= "GET LEVELS" ,width= 30 ,command=self.get_levels, bg = 'yellow')
        button.grid(row = 4 ,column=3 , pady=20 ,padx = 30)

if __name__ == "__main__":

    root = Tk()
    obj=Stocks(root)
    root.mainloop()