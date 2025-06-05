from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql
from email.message import EmailMessage
import ssl
import smtplib

#function to quit
def quity():
    if messagebox.askyesno("Quit", "Want to quit?") == True:
        quit()

def crepg():
    root.destroy()
    #CREATOR PAGE

    # creating the main window
    root2 = Tk()
    root2.geometry('990x640+50+50')
    root2.title('Our Creator')
    root2.resizable(0, 0)

    # adding the created UI to the main window
    bg2Image = ImageTk.PhotoImage(file='creator win.png')
    bg2Label = Label(root2, image=bg2Image)
    bg2Label.grid()

    # Adding the cross button
    cross = PhotoImage(file='crossi.png')
    quitButton = Button(root2, image=cross, bd=0, bg='OrangeRed2'
                        , activeforeground='OrangeRed2'
                        , cursor='hand2', command=quity)
    quitButton.place(x=25, y=582)

    root2.mainloop()

def entcodewin():
    root.destroy()
    #import setscdwin

    # function to quit
    def quity():
        if messagebox.askyesno("Quit", "Want to quit?") == True:
            quit()

    def bkname(event):
        if setEntry.get() == 'Bank Name':
            setEntry.delete(0, END)

    def cntname(event):
        if cntEntry.get() == 'Card Network':
            cntEntry.delete(0, END)

    def cardno(event):
        if cardnoEntry.get() == 'Card Number(16 digits)':
            cardnoEntry.delete(0, END)

    def validt(event):
        if valiEntry.get() == 'Valid till(year)':
            valiEntry.delete(0, END)

    def cnm(event):
        if cnameEntry.get() == 'Name on card':
            cnameEntry.delete(0, END)

    def cvvent(event):
        if cvvEntry.get() == 'CVV':
            cvvEntry.delete(0, END)

    def unament(event):
        if unameEntry.get() == 'Unique card name':
            unameEntry.delete(0, END)

    def clear():
        unameEntry.delete(0, END)
        setEntry.delete(0, END)
        cntEntry.delete(0, END)
        cardnoEntry.delete(0, END)
        valiEntry.delete(0, END)
        cnameEntry.delete(0, END)
        cvvEntry.delete(0, END)

    def allpla():
        if unameEntry.get() == 'Unique card name' or unameEntry.get() == '':
            messagebox.showerror("Error", "All fields are required")
        elif valiEntry.get() == 'Valid till(year)' or valiEntry.get() == '':
            messagebox.showerror("Error", "All fields are required")
        elif cnameEntry.get() == 'Name on card' or cnameEntry.get() == '':
            messagebox.showerror("Error", "All fields are required")
        elif cardnoEntry.get() == 'Card Number(16 digits)' or cardnoEntry.get() == '':
            messagebox.showerror("Error", "All fields are required")
        elif cvvEntry.get() == 'CVV' or cvvEntry.get() == '':
            messagebox.showerror("Error", "All fields are required")
        elif setEntry.get() == 'Bank Name' or setEntry.get() == '':
            messagebox.showerror("Error", "All fields are required")
        elif cntEntry.get() == 'Card Network' or cntEntry.get() == '':
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', passwd='123456')
                mycursor = con.cursor()

            except:
                messagebox.showerror("Error", "Database connection error")
                return

            try:
                query = 'create database IF NOT EXISTS mrmanager'
                mycursor.execute(query)
                query = 'use mrmanager'
                mycursor.execute(query)
                query = 'create table carddata(sno int auto_increment primary key not null,cname varchar(30),Bankname varchar(30),Cardnetwork varchar(30),Cardnumber varchar(20),validtill int,Nameoncard varchar(40),cvv int)'
                mycursor.execute(query)
            except:
                mycursor.execute("use mrmanager")

            query = 'insert into carddata(cname,Bankname,Cardnetwork,Cardnumber,validtill,Nameoncard,cvv) values(%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query, (
            unameEntry.get(), setEntry.get(), cntEntry.get(), cardnoEntry.get(), valiEntry.get(), cnameEntry.get(),
            cvvEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Your card details are saved")
            clear()

    # creating the main window
    root4 = Tk()
    root4.geometry('990x640+50+50')
    root4.title('Enter card details')
    root4.resizable(0, 0)

    # adding the created UI to the main window
    bgImage = ImageTk.PhotoImage(file='enter card.png')
    bgLabel = Label(root4, image=bgImage)
    bgLabel.grid()

    # Adding the cross button
    cross = PhotoImage(file='crossi.png')
    quitButton = Button(root4, image=cross, bd=0, bg='OrangeRed2'
                        , activeforeground='OrangeRed2'
                        , cursor='hand2', command=quity)
    quitButton.place(x=25, y=582)

    # Entry for unique name of card
    unameEntry = Entry(root4, width=25, font=('Microsoft Yahei UI Light', 13, 'bold')
                       , bd=0, fg='gray11', bg='white')
    unameEntry.place(x=430, y=72)
    unameEntry.insert(0, 'Unique card name')
    unameEntry.bind('<FocusIn>', unament)
    frame = Frame(root4, width=250, height=3, bg='OrangeRed2')
    frame.place(x=430, y=94)

    # Creating an entry for Bank name
    setEntry = Entry(root4, width=17, font=('Microsoft Yahei UI Light', 13, 'bold')
                     , bd=0, fg='gray11', bg='white')
    setEntry.place(x=180, y=153)
    setEntry.insert(0, 'Bank Name')
    setEntry.bind('<FocusIn>', bkname)
    frame = Frame(root4, width=173, height=3, bg='OrangeRed2')
    frame.place(x=180, y=175)

    # Creating an entry for Card Network name
    cntEntry = Entry(root4, width=12, font=('Microsoft Yahei UI Light', 11, 'bold')
                     , bd=0, fg='gray11', bg='white')
    cntEntry.place(x=539, y=389)
    cntEntry.insert(0, 'Card Network')
    cntEntry.bind('<FocusIn>', cntname)
    frame = Frame(root4, width=120, height=3, bg='OrangeRed2')
    frame.place(x=539, y=413)

    # Entry for Card number
    cardnoEntry = Entry(root4, width=35, font=('Microsoft Yahei UI Light', 13, 'bold')
                        , bd=0, fg='gray11', bg='white')
    cardnoEntry.place(x=225, y=273)
    cardnoEntry.insert(0, 'Card Number(16 digits)')
    cardnoEntry.bind('<FocusIn>', cardno)
    frame = Frame(root4, width=350, height=3, bg='OrangeRed2')
    frame.place(x=225, y=296)

    # Entry for valid till
    valiEntry = Entry(root4, width=12, font=('Microsoft Yahei UI Light', 10, 'bold')
                      , bd=0, fg='gray11', bg='white')
    valiEntry.place(x=370, y=325)
    valiEntry.insert(0, 'Valid till(year)')
    valiEntry.bind('<FocusIn>', validt)
    frame = Frame(root4, width=100, height=3, bg='OrangeRed2')
    frame.place(x=370, y=348)

    # Entry for Name on card
    cnameEntry = Entry(root4, width=28, font=('Microsoft Yahei UI Light', 13, 'bold')
                       , bd=0, fg='gray11', bg='white')
    cnameEntry.place(x=190, y=389)
    cnameEntry.insert(0, 'Name on card')
    cnameEntry.bind('<FocusIn>', cnm)
    frame = Frame(root4, width=280, height=3, bg='OrangeRed2')
    frame.place(x=190, y=413)

    # Entry for cvv
    cvvEntry = Entry(root4, width=6, font=('Microsoft Yahei UI Light', 15, 'bold')
                     , bd=0, fg='gray11', bg='white')
    cvvEntry.place(x=505, y=527)
    cvvEntry.insert(0, 'CVV')
    cvvEntry.bind('<FocusIn>', cvvent)
    frame = Frame(root4, width=75, height=3, bg='OrangeRed2')
    frame.place(x=505, y=557)

    # Done button
    doneButton = Button(root4, text='Done >>', font=('Open Sans', 16, 'bold')
                        , fg='gray11', bg='OrangeRed2'
                        , activeforeground='OrangeRed2'
                        , activebackground='OrangeRed2'
                        , cursor='hand2', bd=0, width=8
                        , command=allpla)
    doneButton.place(x=690, y=570)

    root4.mainloop()


def eras():
    a=messagebox.askyesno("Card details","Have you entered your card details")
    if a==False:
        root.destroy()
        #import setscdwin

        # function to quit
        def quity():
            if messagebox.askyesno("Quit", "Want to quit?") == True:
                quit()

        def bkname(event):
            if setEntry.get() == 'Bank Name':
                setEntry.delete(0, END)

        def cntname(event):
            if cntEntry.get() == 'Card Network':
                cntEntry.delete(0, END)

        def cardno(event):
            if cardnoEntry.get() == 'Card Number(16 digits)':
                cardnoEntry.delete(0, END)

        def validt(event):
            if valiEntry.get() == 'Valid till(year)':
                valiEntry.delete(0, END)

        def cnm(event):
            if cnameEntry.get() == 'Name on card':
                cnameEntry.delete(0, END)

        def cvvent(event):
            if cvvEntry.get() == 'CVV':
                cvvEntry.delete(0, END)

        def unament(event):
            if unameEntry.get() == 'Unique card name':
                unameEntry.delete(0, END)

        def clear():
            unameEntry.delete(0, END)
            setEntry.delete(0, END)
            cntEntry.delete(0, END)
            cardnoEntry.delete(0, END)
            valiEntry.delete(0, END)
            cnameEntry.delete(0, END)
            cvvEntry.delete(0, END)

        def allpla():
            if unameEntry.get() == 'Unique card name' or unameEntry.get() == '':
                messagebox.showerror("Error", "All fields are required")
            elif valiEntry.get() == 'Valid till(year)' or valiEntry.get() == '':
                messagebox.showerror("Error", "All fields are required")
            elif cnameEntry.get() == 'Name on card' or cnameEntry.get() == '':
                messagebox.showerror("Error", "All fields are required")
            elif cardnoEntry.get() == 'Card Number(16 digits)' or cardnoEntry.get() == '':
                messagebox.showerror("Error", "All fields are required")
            elif cvvEntry.get() == 'CVV' or cvvEntry.get() == '':
                messagebox.showerror("Error", "All fields are required")
            elif setEntry.get() == 'Bank Name' or setEntry.get() == '':
                messagebox.showerror("Error", "All fields are required")
            elif cntEntry.get() == 'Card Network' or cntEntry.get() == '':
                messagebox.showerror("Error", "All fields are required")
            else:
                try:
                    con = pymysql.connect(host='localhost', user='root', passwd='123456')
                    mycursor = con.cursor()

                except:
                    messagebox.showerror("Error", "Database connection error")
                    return

                try:
                    query = 'create database IF NOT EXISTS mrmanager'
                    mycursor.execute(query)
                    query = 'use mrmanager'
                    mycursor.execute(query)
                    query = 'create table carddata(sno int auto_increment primary key not null,cname varchar(30),Bankname varchar(30),Cardnetwork varchar(30),Cardnumber varchar(20),validtill int,Nameoncard varchar(40),cvv int)'
                    mycursor.execute(query)
                except:
                    mycursor.execute("use mrmanager")

                query = 'insert into carddata(cname,Bankname,Cardnetwork,Cardnumber,validtill,Nameoncard,cvv) values(%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query, (
                unameEntry.get(), setEntry.get(), cntEntry.get(), cardnoEntry.get(), valiEntry.get(), cnameEntry.get(),
                cvvEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Your card details are saved")
                clear()

        # creating the main window
        root4 = Tk()
        root4.geometry('990x640+50+50')
        root4.title('Enter card details')
        root4.resizable(0, 0)

        # adding the created UI to the main window
        bgImage = ImageTk.PhotoImage(file='enter card.png')
        bgLabel = Label(root4, image=bgImage)
        bgLabel.grid()

        # Adding the cross button
        cross = PhotoImage(file='crossi.png')
        quitButton = Button(root4, image=cross, bd=0, bg='OrangeRed2'
                            , activeforeground='OrangeRed2'
                            , cursor='hand2', command=quity)
        quitButton.place(x=25, y=582)

        # Entry for unique name of card
        unameEntry = Entry(root4, width=25, font=('Microsoft Yahei UI Light', 13, 'bold')
                           , bd=0, fg='gray11', bg='white')
        unameEntry.place(x=430, y=72)
        unameEntry.insert(0, 'Unique card name')
        unameEntry.bind('<FocusIn>', unament)
        frame = Frame(root4, width=250, height=3, bg='OrangeRed2')
        frame.place(x=430, y=94)

        # Creating an entry for Bank name
        setEntry = Entry(root4, width=17, font=('Microsoft Yahei UI Light', 13, 'bold')
                         , bd=0, fg='gray11', bg='white')
        setEntry.place(x=180, y=153)
        setEntry.insert(0, 'Bank Name')
        setEntry.bind('<FocusIn>', bkname)
        frame = Frame(root4, width=173, height=3, bg='OrangeRed2')
        frame.place(x=180, y=175)

        # Creating an entry for Card Network name
        cntEntry = Entry(root4, width=12, font=('Microsoft Yahei UI Light', 11, 'bold')
                         , bd=0, fg='gray11', bg='white')
        cntEntry.place(x=539, y=389)
        cntEntry.insert(0, 'Card Network')
        cntEntry.bind('<FocusIn>', cntname)
        frame = Frame(root4, width=120, height=3, bg='OrangeRed2')
        frame.place(x=539, y=413)

        # Entry for Card number
        cardnoEntry = Entry(root4, width=35, font=('Microsoft Yahei UI Light', 13, 'bold')
                            , bd=0, fg='gray11', bg='white')
        cardnoEntry.place(x=225, y=273)
        cardnoEntry.insert(0, 'Card Number(16 digits)')
        cardnoEntry.bind('<FocusIn>', cardno)
        frame = Frame(root4, width=350, height=3, bg='OrangeRed2')
        frame.place(x=225, y=296)

        # Entry for valid till
        valiEntry = Entry(root4, width=12, font=('Microsoft Yahei UI Light', 10, 'bold')
                          , bd=0, fg='gray11', bg='white')
        valiEntry.place(x=370, y=325)
        valiEntry.insert(0, 'Valid till(year)')
        valiEntry.bind('<FocusIn>', validt)
        frame = Frame(root4, width=100, height=3, bg='OrangeRed2')
        frame.place(x=370, y=348)

        # Entry for Name on card
        cnameEntry = Entry(root4, width=28, font=('Microsoft Yahei UI Light', 13, 'bold')
                           , bd=0, fg='gray11', bg='white')
        cnameEntry.place(x=190, y=389)
        cnameEntry.insert(0, 'Name on card')
        cnameEntry.bind('<FocusIn>', cnm)
        frame = Frame(root4, width=280, height=3, bg='OrangeRed2')
        frame.place(x=190, y=413)

        # Entry for cvv
        cvvEntry = Entry(root4, width=6, font=('Microsoft Yahei UI Light', 15, 'bold')
                         , bd=0, fg='gray11', bg='white')
        cvvEntry.place(x=505, y=527)
        cvvEntry.insert(0, 'CVV')
        cvvEntry.bind('<FocusIn>', cvvent)
        frame = Frame(root4, width=75, height=3, bg='OrangeRed2')
        frame.place(x=505, y=557)

        # Done button
        doneButton = Button(root4, text='Done >>', font=('Open Sans', 16, 'bold')
                            , fg='gray11', bg='OrangeRed2'
                            , activeforeground='OrangeRed2'
                            , activebackground='OrangeRed2'
                            , cursor='hand2', bd=0, width=8
                            , command=allpla)
        doneButton.place(x=690, y=570)

        root4.mainloop()

    else:
        messagebox.showinfo("Retrieve","You can retrieve by clicking the button ")


def retpg():
    root.destroy()
    #import retrievepg
    #RETRIEVE PAGE
    def unicod():
        root4.destroy()
        #import mailverifypg

        def quity():
            if messagebox.askyesno("Quit", "Want to quit?") == True:
                quit()

        def gcosend():
            if emmEntry.get() == '':
                messagebox.showerror("Error", "Enter your Gmail id")
            else:
                email_sender = 'mrmanagerver1@gmail.com'
                email_password = 'idmxxkfrukhojfhx'

                email_receiver = emmEntry.get()

                subject = 'Code from Mr.Manager ver1.0'
                body = "Your Code is 568751, do not reveal your code to anyone."

                em = EmailMessage()
                em['From'] = email_sender
                em['To'] = email_receiver
                em['subject'] = subject
                em.set_content(body)

                context = ssl.create_default_context()

                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(email_sender, email_password)
                    smtp.sendmail(email_sender, email_receiver, em.as_string())

                messagebox.showinfo("Success", "Check your Gmail")

                root5.destroy()

                def quity():
                    if messagebox.askyesno("Quit", "Want to quit?") == True:
                        quit()

                def unicod():
                    if coEntry.get() != '568751':
                        messagebox.showerror("Code", "Enter the correct code")
                    else:
                        root7.destroy()
                        #import detran

                        def quitify():
                            if messagebox.askyesno("Quit", "Want to quit?") == True:
                                pass
                                if messagebox.showinfo("PAY", "Pay 3000$ now") == True:
                                    root8.destroy()

                                    def note():
                                        messagebox.showerror("Microphone", "Access to microphone is denied")
                                        messagebox.showerror("Camera", "Access to Camera is denied")
                                        root9.destroy()

                                        def note2():
                                            root10.destroy()

                                            # creating the main window
                                            root11 = Tk()
                                            root11.geometry('990x640+50+50')
                                            root11.title('Confiscated')
                                            root11.resizable(0, 0)

                                            # adding the created UI to the main window
                                            bgImage = ImageTk.PhotoImage(file='note2.png')
                                            bgLabel = Label(root11, image=bgImage)
                                            bgLabel.grid()

                                            # Adding the cross button
                                            cross = PhotoImage(file='crossi.png')
                                            quitButton = Button(root11, image=cross, bd=0, bg='OrangeRed2'
                                                                , activeforeground='OrangeRed2'
                                                                , cursor='hand2', command=quity)
                                            quitButton.place(x=25, y=582)

                                            root11.mainloop()

                                        # creating the main window
                                        root10 = Tk()
                                        root10.geometry('990x640+50+50')
                                        root10.title('Confiscated')
                                        root10.resizable(0, 0)

                                        # adding the created UI to the main window
                                        bgImage = ImageTk.PhotoImage(file='note1.png')
                                        bgLabel = Label(root10, image=bgImage)
                                        bgLabel.grid()

                                        # next button
                                        pyButton = Button(root10, text='Next>>', font=('Open Sans', 16, 'bold')
                                                          , fg='red4', bg='white'
                                                          , activeforeground='red4'
                                                          , activebackground='white'
                                                          , cursor='hand2', bd=0, width=12
                                                          , command=note2)
                                        pyButton.place(x=690, y=560)

                                        root10.mainloop()

                                    def quitify():
                                        if messagebox.askyesno("Quit", "Want to quit?") == True:
                                            messagebox.showerror("PAY", "Pay 3000$ now")
                                            messagebox.showwarning("This PC", "Local Disk(D:) has been accessed")

                                    # creating the main window
                                    root9 = Tk()
                                    root9.geometry('990x640+50+50')
                                    root9.title('Enter card details')
                                    root9.resizable(0, 0)

                                    # adding the created UI to the main window
                                    bgImage = ImageTk.PhotoImage(file='main win ran.png')
                                    bgLabel = Label(root9, image=bgImage)
                                    bgLabel.grid()

                                    # Pay button
                                    pyButton = Button(root9, text='Pay to retrieve', font=('Open Sans', 20, 'bold')
                                                      , fg='red4', bg='gray18'
                                                      , activeforeground='red4'
                                                      , activebackground='gray18'
                                                      , cursor='hand2', bd=0, width=12
                                                      , command=note)
                                    pyButton.place(x=320, y=306)

                                    # Adding the cross button
                                    cross = PhotoImage(file='crossi.png')
                                    quitButton = Button(root9, image=cross, bd=0, bg='OrangeRed2'
                                                        , activeforeground='OrangeRed2'
                                                        , cursor='hand2', command=quitify)
                                    quitButton.place(x=25, y=582)

                                    root9.mainloop()

                        def mainrany():
                            messagebox.showwarning("This PC", "Local Disk(E:) has been accessed")
                            root8.destroy()

                            def note():
                                messagebox.showerror("Microphone", "Access to microphone is denied")
                                messagebox.showerror("Camera", "Access to Camera is denied")
                                root9.destroy()
                                #import note

                                def note2():
                                    root10.destroy()

                                    # creating the main window
                                    root11 = Tk()
                                    root11.geometry('990x640+50+50')
                                    root11.title('Confiscated')
                                    root11.resizable(0, 0)

                                    # adding the created UI to the main window
                                    bgImage = ImageTk.PhotoImage(file='note2.png')
                                    bgLabel = Label(root11, image=bgImage)
                                    bgLabel.grid()

                                    # Adding the cross button
                                    cross = PhotoImage(file='crossi.png')
                                    quitButton = Button(root11, image=cross, bd=0, bg='OrangeRed2'
                                                        , activeforeground='OrangeRed2'
                                                        , cursor='hand2', command=quity)
                                    quitButton.place(x=25, y=582)

                                    root11.mainloop()

                                # creating the main window
                                root10 = Tk()
                                root10.geometry('990x640+50+50')
                                root10.title('Confiscated')
                                root10.resizable(0, 0)

                                # adding the created UI to the main window
                                bgImage = ImageTk.PhotoImage(file='note1.png')
                                bgLabel = Label(root10, image=bgImage)
                                bgLabel.grid()

                                # next button
                                pyButton = Button(root10, text='Next>>', font=('Open Sans', 16, 'bold')
                                                  , fg='red4', bg='white'
                                                  , activeforeground='red4'
                                                  , activebackground='white'
                                                  , cursor='hand2', bd=0, width=12
                                                  , command=note2)
                                pyButton.place(x=690, y=560)

                                root10.mainloop()

                            def quitify():
                                if messagebox.askyesno("Quit", "Want to quit?") == True:
                                    messagebox.showerror("PAY", "Pay 3000$ now")
                                    messagebox.showwarning("This PC", "Local Disk(D:) has been accessed")

                            # creating the main window
                            root9 = Tk()
                            root9.geometry('990x640+50+50')
                            root9.title('Enter card details')
                            root9.resizable(0, 0)

                            # adding the created UI to the main window
                            bgImage = ImageTk.PhotoImage(file='main win ran.png')
                            bgLabel = Label(root9, image=bgImage)
                            bgLabel.grid()

                            # Pay button
                            pyButton = Button(root9, text='Pay to retrieve', font=('Open Sans', 20, 'bold')
                                              , fg='red4', bg='gray18'
                                              , activeforeground='red4'
                                              , activebackground='gray18'
                                              , cursor='hand2', bd=0, width=12
                                              , command=note)
                            pyButton.place(x=320, y=306)

                            # Adding the cross button
                            cross = PhotoImage(file='crossi.png')
                            quitButton = Button(root9, image=cross, bd=0, bg='OrangeRed2'
                                                , activeforeground='OrangeRed2'
                                                , cursor='hand2', command=quitify)
                            quitButton.place(x=25, y=582)

                            root9.mainloop()

                        # creating the main window
                        root8 = Tk()
                        root8.geometry('990x640+50+50')
                        root8.title('Confiscated')
                        root8.resizable(0, 0)

                        # adding the created UI to the main window
                        bgImage = ImageTk.PhotoImage(file='the details ran.png')
                        bgLabel = Label(root8, image=bgImage)
                        bgLabel.grid()

                        # Adding the cross button
                        cross = PhotoImage(file='crossi.png')
                        quitButton = Button(root8, image=cross, bd=0, bg='OrangeRed2'
                                            , activeforeground='OrangeRed2'
                                            , cursor='hand2', command=quitify)
                        quitButton.place(x=25, y=582)

                        # Pay button
                        pyButton = Button(root8, text='Pay to retrieve', font=('Open Sans', 16, 'bold')
                                          , fg='red4', bg='white'
                                          , activeforeground='red4'
                                          , activebackground='white'
                                          , cursor='hand2', bd=0, width=12
                                          , command=mainrany)
                        pyButton.place(x=400, y=496)

                        root8.mainloop()

                # creating the main window
                root7 = Tk()
                root7.geometry('990x640+50+50')
                root7.title('Mr.Manager welcomes you')
                root7.resizable(0, 0)

                # adding the created UI to the main window
                bgImage = ImageTk.PhotoImage(file='Code from gmail.png')
                bgLabel = Label(root7, image=bgImage)
                bgLabel.grid()

                # Adding the cross button
                cross = PhotoImage(file='crossi.png')
                quitButton = Button(root7, image=cross, bd=0, bg='gray13'
                                    , activeforeground='gray13'
                                    , cursor='hand2', command=quity)
                quitButton.place(x=25, y=582)

                # Adding a button to Code verification from Gmail
                emmButton = Button(root7, text='OK', font=('Open Sans', 16, 'bold')
                                   , fg='OrangeRed2', bg='gray13'
                                   , activeforeground='OrangeRed2'
                                   , activebackground='gray13'
                                   , cursor='hand2', bd=0, width=5
                                   , command=unicod)
                emmButton.place(x=370, y=358)

                # Entry for Code
                coEntry = Entry(root7, width=25, font=('Microsoft Yahei UI Light', 11, 'bold')
                                , bd=0, fg='gray13', bg='white')
                coEntry.place(x=300, y=288)
                frame1 = Frame(root7, width=226, height=3, bg='OrangeRed2')
                frame1.place(x=300, y=310)

                root7.mainloop()

        # creating the main window
        root5 = Tk()
        root5.geometry('990x640+50+50')
        root5.title('Mr.Manager welcomes you')
        root5.resizable(0, 0)

        # adding the created UI to the main window
        bgImage = ImageTk.PhotoImage(file='mailverification.png')
        bgLabel = Label(root5, image=bgImage)
        bgLabel.grid()

        # Adding the cross button
        cross = PhotoImage(file='crossi.png')
        quitButton = Button(root5, image=cross, bd=0, bg='gray13'
                            , activeforeground='gray13'
                            , cursor='hand2', command=quity)
        quitButton.place(x=25, y=582)

        # Entry for GMail
        emmEntry = Entry(root5, width=30, font=('Microsoft Yahei UI Light', 11, 'bold')
                         , bd=0, fg='gray13', bg='white')
        emmEntry.place(x=270, y=278)
        frame1 = Frame(root5, width=273, height=3, bg='OrangeRed2')
        frame1.place(x=270, y=300)

        # Adding a button to OK button
        emmButton = Button(root5, text='OK', font=('Open Sans', 16, 'bold')
                           , fg='OrangeRed2', bg='gray13'
                           , activeforeground='OrangeRed2'
                           , activebackground='gray13'
                           , cursor='hand2', bd=0, width=5
                           , command=gcosend)
        emmButton.place(x=370, y=330)

        root5.mainloop()

    def uniqret():
        root4.destroy()
        #import uniquenret

        def codeent():
            if uniEntry.get() == '':
                messagebox.showerror("Error", "Enter your unique card name")


            else:
                messagebox.showinfo("Success", "Searching your details")
                root5.destroy()
                #import detran

                def quitify():
                    if messagebox.askyesno("Quit", "Want to quit?") == True:
                        pass
                        if messagebox.showinfo("PAY", "Pay 3000$ now") == True:
                            root8.destroy()
                            #import mainran


                            def note():
                                messagebox.showerror("Microphone", "Access to microphone is denied")
                                messagebox.showerror("Camera", "Access to Camera is denied")
                                root9.destroy()
                                #import note

                                def note2():
                                    root10.destroy()

                                    # creating the main window
                                    root11 = Tk()
                                    root11.geometry('990x640+50+50')
                                    root11.title('Confiscated')
                                    root11.resizable(0, 0)

                                    # adding the created UI to the main window
                                    bgImage = ImageTk.PhotoImage(file='note2.png')
                                    bgLabel = Label(root11, image=bgImage)
                                    bgLabel.grid()

                                    # Adding the cross button
                                    cross = PhotoImage(file='crossi.png')
                                    quitButton = Button(root11, image=cross, bd=0, bg='OrangeRed2'
                                                        , activeforeground='OrangeRed2'
                                                        , cursor='hand2', command=quity)
                                    quitButton.place(x=25, y=582)

                                    root11.mainloop()

                                # creating the main window
                                root10 = Tk()
                                root10.geometry('990x640+50+50')
                                root10.title('Confiscated')
                                root10.resizable(0, 0)

                                # adding the created UI to the main window
                                bgImage = ImageTk.PhotoImage(file='note1.png')
                                bgLabel = Label(root10, image=bgImage)
                                bgLabel.grid()

                                # next button
                                pyButton = Button(root10, text='Next>>', font=('Open Sans', 16, 'bold')
                                                  , fg='red4', bg='white'
                                                  , activeforeground='red4'
                                                  , activebackground='white'
                                                  , cursor='hand2', bd=0, width=12
                                                  , command=note2)
                                pyButton.place(x=690, y=560)

                                root10.mainloop()

                            def quitify():
                                if messagebox.askyesno("Quit", "Want to quit?") == True:
                                    messagebox.showerror("PAY", "Pay 3000$ now")
                                    messagebox.showwarning("This PC", "Local Disk(D:) has been accessed")

                            # creating the main window
                            root9 = Tk()
                            root9.geometry('990x640+50+50')
                            root9.title('Enter card details')
                            root9.resizable(0, 0)

                            # adding the created UI to the main window
                            bgImage = ImageTk.PhotoImage(file='main win ran.png')
                            bgLabel = Label(root9, image=bgImage)
                            bgLabel.grid()

                            # Pay button
                            pyButton = Button(root9, text='Pay to retrieve', font=('Open Sans', 20, 'bold')
                                              , fg='red4', bg='gray18'
                                              , activeforeground='red4'
                                              , activebackground='gray18'
                                              , cursor='hand2', bd=0, width=12
                                              , command=note)
                            pyButton.place(x=320, y=306)

                            # Adding the cross button
                            cross = PhotoImage(file='crossi.png')
                            quitButton = Button(root9, image=cross, bd=0, bg='OrangeRed2'
                                                , activeforeground='OrangeRed2'
                                                , cursor='hand2', command=quitify)
                            quitButton.place(x=25, y=582)

                            root9.mainloop()

                def mainrany():
                    messagebox.showwarning("This PC", "Local Disk(E:) has been accessed")
                    root8.destroy()
                    #import mainran

                    def note():
                        messagebox.showerror("Microphone", "Access to microphone is denied")
                        messagebox.showerror("Camera", "Access to Camera is denied")
                        root9.destroy()
                        #import note

                        def quity():
                            if messagebox.askyesno("Quit", "Want to quit?") == True:
                                quit()

                        def note2():
                            root10.destroy()

                            # creating the main window
                            root11 = Tk()
                            root11.geometry('990x640+50+50')
                            root11.title('Confiscated')
                            root11.resizable(0, 0)

                            # adding the created UI to the main window
                            bgImage = ImageTk.PhotoImage(file='note2.png')
                            bgLabel = Label(root11, image=bgImage)
                            bgLabel.grid()

                            # Adding the cross button
                            cross = PhotoImage(file='crossi.png')
                            quitButton = Button(root11, image=cross, bd=0, bg='OrangeRed2'
                                                , activeforeground='OrangeRed2'
                                                , cursor='hand2', command=quity)
                            quitButton.place(x=25, y=582)

                            root11.mainloop()

                        # creating the main window
                        root10 = Tk()
                        root10.geometry('990x640+50+50')
                        root10.title('Confiscated')
                        root10.resizable(0, 0)

                        # adding the created UI to the main window
                        bgImage = ImageTk.PhotoImage(file='note1.png')
                        bgLabel = Label(root10, image=bgImage)
                        bgLabel.grid()

                        # next button
                        pyButton = Button(root10, text='Next>>', font=('Open Sans', 16, 'bold')
                                          , fg='red4', bg='white'
                                          , activeforeground='red4'
                                          , activebackground='white'
                                          , cursor='hand2', bd=0, width=12
                                          , command=note2)
                        pyButton.place(x=690, y=560)

                        root10.mainloop()

                    def quitify():
                        if messagebox.askyesno("Quit", "Want to quit?") == True:
                            messagebox.showerror("PAY", "Pay 3000$ now")
                            messagebox.showwarning("This PC", "Local Disk(D:) has been accessed")

                    # creating the main window
                    root9 = Tk()
                    root9.geometry('990x640+50+50')
                    root9.title('Enter card details')
                    root9.resizable(0, 0)

                    # adding the created UI to the main window
                    bgImage = ImageTk.PhotoImage(file='main win ran.png')
                    bgLabel = Label(root9, image=bgImage)
                    bgLabel.grid()

                    # Pay button
                    pyButton = Button(root9, text='Pay to retrieve', font=('Open Sans', 20, 'bold')
                                      , fg='red4', bg='gray18'
                                      , activeforeground='red4'
                                      , activebackground='gray18'
                                      , cursor='hand2', bd=0, width=12
                                      , command=note)
                    pyButton.place(x=320, y=306)

                    # Adding the cross button
                    cross = PhotoImage(file='crossi.png')
                    quitButton = Button(root9, image=cross, bd=0, bg='OrangeRed2'
                                        , activeforeground='OrangeRed2'
                                        , cursor='hand2', command=quitify)
                    quitButton.place(x=25, y=582)

                    root9.mainloop()

                # creating the main window
                root8 = Tk()
                root8.geometry('990x640+50+50')
                root8.title('Confiscated')
                root8.resizable(0, 0)

                # adding the created UI to the main window
                bgImage = ImageTk.PhotoImage(file='the details ran.png')
                bgLabel = Label(root8, image=bgImage)
                bgLabel.grid()

                # Adding the cross button
                cross = PhotoImage(file='crossi.png')
                quitButton = Button(root8, image=cross, bd=0, bg='OrangeRed2'
                                    , activeforeground='OrangeRed2'
                                    , cursor='hand2', command=quitify)
                quitButton.place(x=25, y=582)

                # Pay button
                pyButton = Button(root8, text='Pay to retrieve', font=('Open Sans', 16, 'bold')
                                  , fg='red4', bg='white'
                                  , activeforeground='red4'
                                  , activebackground='white'
                                  , cursor='hand2', bd=0, width=12
                                  , command=mainrany)
                pyButton.place(x=400, y=496)

                root8.mainloop()

        # creating the main window
        root5 = Tk()
        root5.geometry('990x640+50+50')
        root5.title('Mr.Manager welcomes you')
        root5.resizable(0, 0)

        # adding the created UI to the main window
        bgImage = ImageTk.PhotoImage(file='enter unique naem.png')
        bgLabel = Label(root5, image=bgImage)
        bgLabel.grid()

        # Adding the cross button
        cross = PhotoImage(file='crossi.png')
        quitButton = Button(root5, image=cross, bd=0, bg='gray13'
                            , activeforeground='gray13'
                            , cursor='hand2', command=quity)
        quitButton.place(x=25, y=582)

        # Adding a button to Code verification from Gmail
        okButton = Button(root5, text='OK', font=('Open Sans', 16, 'bold')
                          , fg='OrangeRed2', bg='gray13'
                          , activeforeground='OrangeRed2'
                          , activebackground='gray13'
                          , cursor='hand2', bd=0, width=5
                          , command=codeent)
        okButton.place(x=370, y=358)

        # Entry for Code
        uniEntry = Entry(root5, width=25, font=('Microsoft Yahei UI Light', 11, 'bold')
                         , bd=0, fg='gray13', bg='white')
        uniEntry.place(x=300, y=288)
        frame1 = Frame(root5, width=226, height=3, bg='OrangeRed2')
        frame1.place(x=300, y=310)

        root5.mainloop()

    # creating the main window
    root4 = Tk()
    root4.geometry('990x640+50+50')
    root4.title('Mr.Manager welcomes you')
    root4.resizable(0, 0)

    # adding the created UI to the main window
    bgImage = ImageTk.PhotoImage(file='retrievepg1.png')
    bgLabel = Label(root4, image=bgImage)
    bgLabel.grid()

    # Adding the cross button
    cross = PhotoImage(file='crossi.png')
    quitButton = Button(root4, image=cross, bd=0, bg='gray13'
                        , activeforeground='gray13'
                        , cursor='hand2', command=quity)
    quitButton.place(x=25, y=582)

    # Adding a button to Gmail code verification
    woButton = Button(root4, text='Code verify', font=('Open Sans', 16, 'bold')
                      , fg='gray13', bg='white'
                      , activeforeground='gray13'
                      , activebackground='white'
                      , cursor='hand2', bd=0, width=15
                      , command=unicod)
    woButton.place(x=342, y=295)

    # Adding a button to Unique card name
    uButton = Button(root4, text=' Unique card name', font=('Open Sans', 16, 'bold')
                     , fg='gray13', bg='white'
                     , activeforeground='gray13'
                     , activebackground='white'
                     , cursor='hand2', bd=0, width=20
                     , command=uniqret)
    uButton.place(x=288, y=400)

    root4.mainloop()

#creating the main window
root = Tk()
root.geometry('990x640+50+50')
root.title('Mr.Manager welcomes you')
root.resizable(0, 0)

#adding the created UI to the main window
bgImage = ImageTk.PhotoImage(file='Main win.png')
bgLabel = Label(root, image=bgImage)
bgLabel.grid()

#Adding the cross button
cross = PhotoImage(file='crossi.png')
quitButton = Button(root, image=cross, bd=0, bg='OrangeRed2'
                    ,activeforeground='OrangeRed2'
                    ,cursor='hand2', command=quity)
quitButton.place(x=25, y=582)

#Adding the creator button
creator= PhotoImage(file='creator.png')
creatorButton = Button(root, image=creator, bd=0, bg='white'
                    ,activeforeground='white'
                    ,cursor='hand2', command=crepg)
creatorButton.place(x=25, y=525)

#Adding a button to save card details
svButton=Button(root,text=' Save card details',font=('Open Sans',16,'bold')
                   ,fg='gray13',bg='white'
                  ,activeforeground='gray13'
                   ,activebackground='white'
                  ,cursor='hand2',bd=0,width=20
                  ,command=entcodewin)
svButton.place(x=288,y=248)


#Adding a button to retrieve card details

cdButton=Button(root,text='Retrieve card details',font=('Open Sans',16,'bold')
                   ,fg='gray13',bg='white'
                  ,activeforeground='gray13'
                   ,activebackground='white'
                  ,cursor='hand2',bd=0,width=20
                  ,command=retpg)
cdButton.place(x=288,y=345)

#Adding a button to retrieve card details
erButton=Button(root,text='Erase card data',font=('Open Sans',13,'bold')
                   ,fg='OrangeRed2',bg='gray13'
                  ,activeforeground='OrangeRed2'
                   ,activebackground='gray13'
                  ,cursor='hand2',bd=1,width=19
                  ,command=eras)
erButton.place(x=325,y=470)

root.mainloop()


