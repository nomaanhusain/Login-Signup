import tkinter as tk
name=['a','b','c']
pas=['p1','p2','p3']
ct=int(input('Number of actions'))
def sig():
    nu=entry1.get()
    np=entry2.get()
    name.append(nu)
    pas.append(np)
    labelsin=tk.Label(win1,text='Not a stranger No more')
    labelsin.place(x=160,y=150)
def login():
    uname=entryu.get()
    upas=entryp.get()
    etin=tk.Label(win2,text='Logged in',bg='Grey',fg='Green')
    etout=tk.Label(win2,text='Wrong Pass',bg='Black',fg='Yellow')
    etwr=tk.Label(win2,text='Not found',bg='Black',fg='Red')
    if uname in name:
        if upas in pas and name.index(uname)==pas.index(upas):
            etin.place(x=2,y=150)
        else:
            etout.place(x=2,y=150)
    else:
        etwr.place(x=2,y=150)
while ct!=0:
    a=int(input('Press 1 for Login, 2 For signup'))
    if a==2:
        ct=ct-1
        print('See the Window')
        win1=tk.Tk()
        win1.title('Sign Up')
        win1.geometry('400x400')
        greetlb=tk.Label(win1,text='Welcome Stranger')
        greetlb.place(x=160,y=1)
        label1=tk.Label(win1,text='Enter username')
        label1.place(x=2,y=20)
        entry1=tk.Entry(win1,relief='flat')
        entry1.place(x=2,y=45)
        label2=tk.Label(win1,text='Enter Password')
        label2.place(x=2,y=70)
        entry2=tk.Entry(win1,relief='flat')
        entry2.place(x=2,y=95)
        button=tk.Button(win1,text='Sign Up',command=sig)
        button.place(x=2,y=120)
    elif a==1:
        ct=ct-1
        print('See the window')
        win2=tk.Tk()
        win2.title('Login')
        win2.geometry('400x400')
        labelgr=tk.Label(win2,text='Come on In sport')
        labelgr.place(x=160,y=2)
        labelu=tk.Label(win2,text='User Name')
        labelu.place(x=2,y=20)
        entryu=tk.Entry(win2,relief='flat')
        entryu.place(x=2,y=45)
        labelp=tk.Label(win2,text='and password')
        labelp.place(x=2,y=70)
        entryp=tk.Entry(win2,relief='flat')
        entryp.place(x=2,y=95)
        button1=tk.Button(win2,text='Login',command=login)
        button1.place(x=2,y=120)    
    
