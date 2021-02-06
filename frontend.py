from backend import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from tkinter import *
driver = driver()


#Outerwindow
w = Tk()
w.geometry("800x620")
w.title("I n s t a :) B o t")
bg = PhotoImage(file = "bg.png")
label1 = Label( w  , image = bg)
label1.place(x = 0, y = 0)

#labels and entries
Label(w, text='I.n.s.t.a :) B.o.t' , font=("Helvetica", 32) , bg = "#b1eff2" , foreground = "DeepPink3").place(x=250,y=20)
Label(w, text=' INSTAGRAM ID : ' ,font=("Helvetica", 12) , bg = "#b1eff2").place(x=230,y=100)
Label(w, text='PASSWORD :' ,font=("Helvetica", 12) ,  bg ="#b1eff2" ).place(x=255,y=140)
id = StringVar()
pas = StringVar()
e1 = Entry(w, textvariable= id , font=("Helvetica", 12) )
e1.place(x=370,y=100)
e2 = Entry(w, textvariable = pas , font=("Helvetica", 12) , show = "*")
e2.place(x=370,y=140)



#listbox
listbox = Listbox(w,  width=75, font=("Helvetica", 12))
listbox.place(x= 60 , y = 300 )


#Aboutfunction
def about():
    w2 = Toplevel()
    w2.geometry("400x400")
    w2.title("About...:) ")
    bg = PhotoImage(file="bg.png")
    label1 = Label(w2 , image=bg)
    label1.place(x=0, y=0)
    listbox = Listbox(w2 , height = 18 , width=40, font=("Helvetica", 12))
    listbox.place(x=20, y=20)
    listbox.insert(1 , "This is an easy to use Insta :) bot .....")
    listbox.insert(2,  "that can be used by public accounts to ")
    listbox.insert(3 , "find their unfollowers(people who you are")
    listbox.insert(4,  "following but they do not follow you back)," )
    listbox.insert(5 , " followers and following list......:)" , "\n")
    listbox.insert(6 , "what else can this bot do....? ", "\n" )
    listbox.insert(7 , "-send an automated message to a set of users" , "\n")
    listbox.insert(8 , "-like or comment on posts in a particular hashtag", "\n")
    listbox.insert(9 , "to increase your reach you enter your username and", "\n")
    listbox.insert(10 ,"password press the login button so the bot ", "\n")
    listbox.insert(11 , "can start working!....:)")
    w2.mainloop()

#menu
menu = Menu(w)
w.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=w.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About' , command = about )

#Direct Message
def win2():
    w2 = Toplevel()
    w2.geometry("400x400")
    w2.title("Direct Message...:) ")
    bg = PhotoImage(file="bg.png")
    label1 = Label(w2 , image=bg)
    label1.place(x=0, y=0)
    txt =Text(w2 , height = 15 , width = 42 )
    txt.place(x=30 , y = 90)
    cb1 = IntVar()
    cb2 = IntVar()
    cb3 = IntVar()
    Checkbutton(w2 , text= "Followers" , bg = "#b1eff2" , variable = cb1 ).place(x=55 , y = 40)
    Checkbutton(w2, text="Following" , bg = "#b1eff2" , variable = cb2 ).place(x=150, y=40)
    Checkbutton(w2, text="Un-Followers", bg="#b1eff2", variable=cb3).place(x=250, y=40)
    def dmsg():
        username = id.get()
        message = txt.get("1.0",END)
        if cb1.get() == 1 :
            user = followers(driver, username)
        elif cb2.get() == 1:
            user = following(driver, username)
        elif cb3.get() == 1:
            get_unfollowers(driver, username)
        automate_message(driver, username, message, user)
    button5 = Button(w2, text='Send=>', width=10, activebackground="magenta2", bd=3, bg="plum1", font="Lato" , command = dmsg )
    button5.place(x=250, y=350)
    w2.mainloop()



#To like hashtag
def win3():
    w2 = Toplevel()
    w2.geometry("400x250")
    w2.title("Like ")
    bg = PhotoImage(file="bg.png")
    label1 = Label(w2 , image=bg)
    label1.place(x=0, y=0)
    Label(w2, text='Add a hashtag to be Liked....:)', font=("Helvetica", 15), bg="#b1eff2" , foreground = "DeepPink2").place(x=30, y=20)
    txt =Text(w2 , height = 5 , width = 42 )
    txt.place(x=30 , y = 90)
    def like():
        hashtag = txt.get("1.0", END)
        like_posts(driver, hashtag)
    button5 = Button(w2, text='Like Us', width=10, activebackground="magenta2", bd=3, bg="plum1", font="Lato" , command = like)
    button5.place(x=250, y=200)
    w2.mainloop()


#Login function
def log():
    username=id.get()
    pw= pas.get()
    if login(driver, username, pw):
        listbox.insert(END , "Login successfull....!" , "\n")
    else :
        listbox.insert(END, "Login unsuccessfull....!")
#Un-followers function
def unfol():
    username = id.get()
    listbox.delete(0,END)
    unfollowers = get_unfollowers(driver, username)
    for i in range(len(unfollowers)):
        n = i+1
        listbox.insert(END , (n ,":" ,unfollowers[i]) , "\n")

#Followers function
def foll():
    username = id.get()
    listbox.delete(0, END)
    follower = followers(driver, username)
    for i in range(len(follower)):
        n = i+1
        listbox.insert(END , (n ,":" ,follower[i] ), "\n")

#Following function
def foling():
    username = id.get()
    listbox.delete(0, END)
    followin = following(driver, username)
    for i in range(len(followin)):
        n = i+1
        listbox.insert(END , (n ,":" ,followin[i] ) , "\n")

#Logout function
def logout1():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    listbox.delete(0, END)
    listbox.insert(END, "Logged out successfull....!")
    driver.close()


#buttons
button1 = Button(w, text='Log In', width=15 ,activebackground = "magenta2" , bd= 3 , bg = "LightSkyBlue1" , font = "Lato" , command = log )
button1.place(x= 310 , y = 180)
button2 = Button(w, text='Un-followers', width=15 , activebackground = "magenta2" , bd= 3 , bg = "plum1", font = "Lato" , command = unfol )
button2.place(x= 90 , y= 250 )
button3 = Button(w, text='Followers', width=15, activebackground = "magenta2" , bd= 3 , bg = "plum1" , font = "Lato" , command = foll)
button3.place(x= 310 , y= 250 )
button4 = Button(w, text='Following', width=15 , activebackground = "magenta2" , bd= 3 , bg = "plum1" , font = "Lato" , command = foling )
button4.place(x= 540 , y= 250 )
button4 = Button(w, text='DM', width=15 , activebackground = "magenta2" , bd= 3 , bg = "plum1" , font = "Lato" , command = win2)
button4.place(x= 90 , y= 510 )
button4 = Button(w, text='Log out', width=15 , activebackground = "magenta2" , bd= 3 , bg = "plum1" , font = "Lato" , command = logout1 )
button4.place(x= 540 , y= 510 )
button6 = Button(w, text='Like Me', width=15 , activebackground = "magenta2" , bd= 3 , bg = "plum1" , font = "Lato" , command = win3 )
button6.place(x= 310 , y= 510 )

w.mainloop()
