from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import time
import tkinter.messagebox as tmsg
window = Tk()
window_width =  window.winfo_screenwidth();
window_height = window.winfo_screenheight();
# window_width = 1000;
# window_height = 700;
'''
     if window width is 900x800
          x=window_width/6-110,y=window_height/6+28

'''

#---------------------------- Window Settimg Part --------------------------

window.geometry(f"{window_width-10}x{window_height}+0+0")
window.title("Typing Master")
window.iconbitmap("images\\Icons\\7.tif")
window.maxsize(window_width, window_height)
window.minsize(window_width, window_height)
window.resizable(False, True)

#&&&&&&&&&&&&&&&&&&&&&&&&&& End Window Settimg Part &&&&&&&&&&&&&&&&&&&&&&&&&&
# -------------------------- Background Image --------------------------

# get and resize the background image
getimg = Image.open("images\\Lite\\15.jpg");
#set value which we wanted to width - of window widht 
sizeable_img = getimg.resize((window_width,window_height))
img = ImageTk.PhotoImage(image=sizeable_img);

# &&&&&&&&&&&&&&&&&&&&&&&&& End Background Image &&&&&&&&&&&&&&&&&&&&&&&&&

# ------------------------ Set Main Manue Background ------------------------
mainManue = Frame(window,bg="lightgreen",width=window_width,height=window_height);
Label(mainManue,image=img).pack();
mainManue.pack()
# &&&&&&&&&&&&&&&&&&&&&&&& End Set Main Manue Background &&&&&&&&&&&&&&&&&&&&&&&&

# ------------------------- Create Main Box -------------------------
# Set Different collor code
# bg_color = "#548dd4";
bg_color = "#daf5b2";
bg_text_color = "#0d0d0d";
bg_main_title_color = "#333280";
# main_bg_color = "#17365d";
main_bg_color = "#624ad2";
main_bg_text_color = "#ffc000";
acitve_main_fg_color = "#1d1b11";
#set Font size code
bg_title_font = ("Agency FB",28,"underline");
bg_text_font = ("Cordia New",18,"bold","italic","underline");
main_text_font = ("AngsanaUPC",26);
acitve_main_font = ("Clarendon Lt BT",16,"bold");
cursor_pointer = "hand2";

#Create Main box
main_box = Frame(mainManue,bg=main_bg_color,bd=9);
main_box.place(x=window_width/6,y=window_height/6+50,height=570,width=840);
# main_box.place(x=window_width/6,y=window_height/6+50,height=window_height/2+60,width=window_width/2+200);

#function that perform the main manue bar button

def select_studying(event=None):
    studying_btn.config(bg=bg_color,fg=acitve_main_fg_color,font=acitve_main_font);
    typingTest_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    games_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    setting_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    about_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    studying_Fram.pack(anchor='nw',side='top');
    typingtext_Fram.pack_forget();
    setting_Fram.pack_forget();
    games_Fram.pack_forget();
    about_Fram.pack_forget();


def select_typingtest(event=None):
    studying_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    typingTest_btn.config(bg=bg_color,fg=acitve_main_fg_color,font=acitve_main_font);
    games_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    setting_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    about_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    studying_Fram.pack_forget()
    typingtext_Fram.pack(anchor='nw',side='top');
    setting_Fram.pack_forget();
    games_Fram.pack_forget();
    about_Fram.pack_forget();

    
def select_games(event=None):
    studying_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    games_btn.config(bg=bg_color,fg=acitve_main_fg_color,font=acitve_main_font);
    typingTest_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    setting_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    about_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    studying_Fram.pack_forget();
    typingtext_Fram.pack_forget();
    games_Fram.pack(anchor='nw',side='top');
    setting_Fram.pack_forget();
    about_Fram.pack_forget();
def select_setting(event=None):
    studying_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    setting_btn.config(bg=bg_color,fg=acitve_main_fg_color,font=acitve_main_font);
    games_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    typingTest_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    about_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    studying_Fram.pack_forget();
    typingtext_Fram.pack_forget();
    setting_Fram.pack(anchor='nw',side='top');
    games_Fram.pack_forget();
    about_Fram.pack_forget();
def select_about(event=None):
    studying_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    about_btn.config(bg=bg_color,fg=acitve_main_fg_color,font=acitve_main_font);
    games_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    setting_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    typingTest_btn.config(bg=main_bg_color,fg=main_bg_text_color,font=main_text_font);
    studying_Fram.pack_forget();
    typingtext_Fram.pack_forget();
    setting_Fram.pack_forget();
    games_Fram.pack_forget();
    about_Fram.pack(anchor='nw',side='top');
#Create Main Manue Button
def select_close(event=None):
    window.destroy();
close_btn = Button(main_box,text="X",bd=0,relief=FLAT,activebackground=main_bg_color,activeforeground=main_bg_text_color,bg=main_bg_color,fg=main_bg_text_color,font="20",command=select_close)
close_btn.place(x=800,y=5,width=20,height=20);
btn_width = 190;
btn_height = 50;
btn_X = 640;
btn_Y = 80;
btn_height_dif = 70;
    
studying_btn = Button(main_box,justify="center",activebackground=bg_color,bg=bg_color,fg=acitve_main_fg_color,text="Studying",font=acitve_main_font,bd=0,relief=FLAT,command=select_studying);

# studying_btn.bind('<<Ctrl + c>>',run)
btn_Y += btn_height_dif;
typingTest_btn = Button(main_box,justify="center",activebackground=bg_color,bg=main_bg_color,fg=main_bg_text_color,text="Typing Test",font=main_text_font,bd=0,relief=FLAT,command=select_typingtest);
btn_Y += btn_height_dif;
games_btn = Button(main_box,justify="center",activebackground=bg_color,bg=main_bg_color,fg=main_bg_text_color,text="Gammes",font=main_text_font,bd=0,relief=FLAT,command=select_games);
btn_Y += btn_height_dif;
setting_btn = Button(main_box,justify="center",activebackground=bg_color,bg=main_bg_color,fg=main_bg_text_color,text="Setting",font=main_text_font,bd=0,relief=FLAT,command=select_setting);
btn_Y += btn_height_dif;
about_btn = Button(main_box,justify="center",activebackground=bg_color,bg=main_bg_color,fg=main_bg_text_color,text="About",font=main_text_font,bd=0,relief=FLAT,command=select_about);
#create logo into the main manue
img_logo = Image.open("images\\logo.png");
logo_img=img_logo.resize((40,40))
logo = ImageTk.PhotoImage(image=logo_img);
set_icone = Label(main_box,text=" Typing Master",image=logo,fg="#88b622",bg=main_bg_color,compound=LEFT,font=("Times New Roman (Headings CS)",12,"bold"))

def gettimes():
    result = time.localtime()
    hours = int(time.strftime("%H",result))
    minutes = int(time.strftime("%M",result))
    seconds = int(time.strftime("%S",result))
    return (hours*60*60)+(minutes*60)+seconds;

#get hand image
handget = Image.open("images\\hand.jpg");
sizeable_hand = handget.resize((480,165))
hand_img = ImageTk.PhotoImage(image=sizeable_hand);
#get keybord image
keybordget = Image.open("images\\keybord.png");
resize_keybord = keybordget.resize((500,180))
keybord_img = ImageTk.PhotoImage(image=resize_keybord);

def sub_ok_ftn(event=None):
    global btn_X, btn_Y;
    btn_X = 640;
    btn_Y = 80;
    studying_Fram.pack(anchor='nw',side='top')
    studying_btn.place(x=btn_X,y=btn_Y,width=btn_width,height=btn_height);
    btn_Y += btn_height_dif;
    typingTest_btn.place(x=btn_X,y=btn_Y,width=btn_width,height=btn_height);
    btn_Y += btn_height_dif;
    games_btn.place(x=btn_X,y=btn_Y,width=btn_width,height=btn_height);
    btn_Y += btn_height_dif;
    setting_btn.place(x=btn_X,y=btn_Y,width=btn_width,height=btn_height);
    btn_Y += btn_height_dif;
    about_btn.place(x=btn_X,y=btn_Y,width=btn_width,height=btn_height);
    set_icone.place(x=660,y=490);

# '''
symbleget_enter = Image.open("symbols\\enter_btn.jpg");
symble_img_enter = ImageTk.PhotoImage(image=symbleget_enter);
symbleget = Image.open("symbols\\s1.gif");
symble_img = ImageTk.PhotoImage(image=symbleget);
welcom_get = Image.open("symbols\\wlm.bmp");
wcm_resize = welcom_get.resize((460,300))
welcome_img = ImageTk.PhotoImage(image=wcm_resize);
user_name = StringVar();
loading_count = 0;
def login_window(event=None):
    box_bg = "#d9f5b0"
    login_fome = Frame(main_box,bg='#eefed7',width=192,height=1024/2+60);
    login_fome.pack(fill='both',expand=True);
    welcome_pic = Label(login_fome,image=welcome_img)
    welcome_pic.place(x=190,y=130);
    loading_lable = Label(login_fome,text="Loading",bg='#eefed7',font=('Cordia New',44))
    loading_lable.place(x=10,y=8);
    def User_window(event=None):
        login_box = Frame(login_fome,bg=box_bg,bd=1,relief='solid',width=350,height=450)
        login_box.pack(anchor='n',side='bottom');
        Label(login_fome,text='Welcome to Typing Master Lite',bg=box_bg,font=('Agency FB',17)).place(x=255,y=125);
        Label(login_fome,image=symble_img,bg=box_bg).place(x=250,y=190);
        Label(login_fome,text='Enter Your Name',bg=box_bg,font=('Times',15,"bold")).place(x=280,y=188);
        userName_Entry = Entry(login_fome,textvariable=user_name,bd=4,relief=SUNKEN,width=20,font=("time new roman",15));
        userName_Entry.place(x=280,y=225);
        login_btn = Label(login_fome,image=symble_img_enter,cursor=cursor_pointer); 
        login_btn.place(x=430,y=460);
        userName_Entry.focus_set();
        def enter_ftn(event=None):
            if  len(user_name.get().strip()) <= 2:
                user_name.set('');
                tmsg.showwarning('Waring',f"You cn't enter a valid User Name (min len is 3)");
            else:
                print("User Name : ",user_name.get().strip().title());
                login_fome.pack_forget();
                sub_ok_ftn();

        userName_Entry.bind('<Return>',enter_ftn)
        login_btn.bind('<Button-1>',enter_ftn)
    def loading(event=None):
        global loading_count;
        a = '.'*loading_count
        loading_lable.config(text=f'Loading{a}');
        loading_count += 1;
        if loading_count != 5:
            loading_lable.after(700,loading);
        else:
            loading_lable.place_forget();
            welcome_pic.place_forget()
            User_window();
    loading();


    
    


login_window()

#--------------------------- studying Frame ---------------------------

 
studying_Fram = Frame(main_box,bg=bg_color,width=640,height=572)
Label(studying_Fram,text="Touch Typing Course",fg=bg_text_color,bg=bg_color,font=bg_title_font).place(x=5,y=0);

#lesson 1 fuctions
def les1(event=None):
    lesson_1.config(bg="white",fg="black");
    lesson_2.config(bg=bg_color,fg="red");
    lesson_3.config(bg=bg_color,fg="red");
    lesson_1_frame.pack(anchor='w',pady=50,expand=1,fill='both');
    lesson_2_frame.pack_forget();
    lesson_3_frame.pack_forget();
def les2(event=None):
    lesson_2.config(bg="white",fg="black");
    lesson_1.config(bg=bg_color,fg="red");
    lesson_3.config(bg=bg_color,fg="red");
    lesson_1_frame.pack_forget();
    lesson_2_frame.pack(anchor='w',pady=50,expand=1,fill='both');
    lesson_3_frame.pack_forget();
def les3(event=None):
    lesson_3.config(bg="white",fg="black");
    lesson_2.config(bg=bg_color,fg="red");
    lesson_1.config(bg=bg_color,fg="red");
    lesson_1_frame.pack_forget();
    lesson_2_frame.pack_forget();
    lesson_3_frame.pack(anchor='w',pady=50,expand=1,fill='both');

studying_lesson = Frame(studying_Fram,bg=bg_color);
lesson_1 = Button(studying_lesson,text="1",bd=0,relief=FLAT,activebackground="white",activeforeground="black",padx=6,bg="white",fg="black",font=('Calibri (Body)',15,"bold"),command=les1);
lesson_1.place(x=0,y=0);
lesson_2 = Button(studying_lesson,text="2",bd=0,relief=FLAT,activebackground="white",activeforeground="black",padx=6,bg=bg_color,fg="red",font=('Calibri (Body)',15,"bold"),command=les2);
lesson_2.place(x=60,y=0);
lesson_3 = Button(studying_lesson,text="3",bd=0,relief=FLAT,activebackground="white",activeforeground="black",padx=6,bg=bg_color,fg="red",font=('Calibri (Body)',15,"bold"),command=les3);
lesson_3.place(x=120,y=0);
#--------------------- create lession 1 frame -------------------
lesson_1_frame = Frame(studying_lesson,bg=bg_color)
#lesson 1 title
Label(lesson_1_frame,text="Lesson 1: Focus on Home Key’s",bg=bg_color,fg=main_bg_text_color,font=('Calibri (Body)',16)).pack(anchor='nw')
#lesson 1 keys
lesson_1_keyDrill = Label(lesson_1_frame,text="Key Drill",fg=acitve_main_fg_color,bg=bg_color,font=('Cordia New',28,'bold','italic','underline'))
lesson_1_keyDrill.place(x=10,y=50)
lesson_1_worldDrill = Label(lesson_1_frame,text="World Drill",fg=acitve_main_fg_color,bg=bg_color,font=('Cordia New',28,'bold','italic','underline'))
lesson_1_worldDrill.place(x=10,y=110)
lesson_1_tipTypingDrill = Label(lesson_1_frame,text="Tip: Typing Drill",fg=acitve_main_fg_color,bg=bg_color,font=('Cordia New',28,'bold','italic','underline'))
lesson_1_tipTypingDrill.place(x=10,y=170)
lesson_1_paragraphDrill = Label(lesson_1_frame,text="Paragraph Drill",fg=acitve_main_fg_color,bg=bg_color,font=('Cordia New',28,'bold','italic','underline'))
lesson_1_paragraphDrill.place(x=10,y=228)

def oh(event=None):
    print("ho")    
lesson_1_keyDrill.bind('<Button-1>',oh)

lesson_1_frame.pack(anchor='w',pady=50,expand=1,fill='both');
#==================== End create lession 1 fram====================
#--------------------- create lession 2 frame -------------------
lesson_2_frame = Frame(studying_lesson,bg=bg_color)
#lesson 2 title
Label(lesson_2_frame,text="Lesson 2: Focus on Top Row Key’s",bg=bg_color,fg=main_bg_text_color,font=('Calibri (Body)',16)).pack(anchor='nw')
#lesson 2 keys
lesson_2_keyDrill = Label(lesson_2_frame,text="Key Drill",fg=acitve_main_fg_color,bg=bg_color,font=('Cordia New',28,'bold','italic','underline'))
lesson_2_keyDrill.place(x=10,y=50)
lesson_2_worldDrill = Label(lesson_2_frame,text="World Drill",fg=acitve_main_fg_color,bg=bg_color,font=('Cordia New',28,'bold','italic','underline'))
lesson_2_worldDrill.place(x=10,y=110)
lesson_2_tipTypingDrill = Label(lesson_2_frame,text="Tip: Typing Drill",fg=acitve_main_fg_color,bg=bg_color,font=('Cordia New',28,'bold','italic','underline'))
lesson_2_tipTypingDrill.place(x=10,y=170)
lesson_2_paragraphDrill = Label(lesson_2_frame,text="Paragraph Drill",fg=acitve_main_fg_color,bg=bg_color,font=('Cordia New',28,'bold','italic','underline'))
lesson_2_paragraphDrill.place(x=10,y=228)

# lesson_2_frame.pack(anchor='w',pady=50,expand=1,fill='both');
#==================== End create lession 2 fram====================
#--------------------- create lession 3 frame -------------------
lesson_3_frame = Frame(studying_lesson,bg=bg_color)
#lesson 3 title
Label(lesson_3_frame,text="Lesson 3: Focus on Buttom Row Key’s",bg=bg_color,fg=main_bg_text_color,font=('Calibri (Body)',16)).pack(anchor='nw')
#lesson 3 keys
lesson_3_keyDrill = Label(lesson_3_frame,text="Key Drill",fg=acitve_main_fg_color,bg=bg_color,font=('Cordia New',28,'bold','italic','underline'))
lesson_3_keyDrill.place(x=10,y=50)
lesson_3_worldDrill = Label(lesson_3_frame,text="World Drill",fg=acitve_main_fg_color,bg=bg_color,font=('Cordia New',28,'bold','italic','underline'))
lesson_3_worldDrill.place(x=10,y=110)
lesson_3_tipTypingDrill = Label(lesson_3_frame,text="Tip: Typing Drill",fg=acitve_main_fg_color,bg=bg_color,font=('Cordia New',28,'bold','italic','underline'))
lesson_3_tipTypingDrill.place(x=10,y=170)
lesson_3_paragraphDrill = Label(lesson_3_frame,text="Paragraph Drill",fg=acitve_main_fg_color,bg=bg_color,font=('Cordia New',28,'bold','italic','underline'))
lesson_3_paragraphDrill.place(x=10,y=228)

#==================== End create lession 3fram====================
studying_lesson.place(x=50,y=80,width=546,height=461);
# studying_Fram.pack(anchor='nw',side='top')
#&&&&&&&&&&&&&&&&&&& End studying Frame &&&&&&&&&&&&&&&&&&&


#-------------------- typing test frame --------------------
typingtext_Fram = Frame(main_box,bg=bg_color,width=640,height=572)
Label(typingtext_Fram,text="Typing Test",fg=bg_text_color,bg=bg_color,font=bg_title_font).place(x=5,y=0);
#title
Label(typingtext_Fram,text="Test Paragraph's",fg=main_bg_text_color,bg=bg_color,font=('Calibri (Body)',18,'italic')).place(x=60,y=110);
#insert Paragraphs
paragraphs_list = Listbox(typingtext_Fram,width=28,height=5,font=('Cordia New',20,'bold'))
paragraphs_list.place(x=60,y=160)
paragraphs_list.insert(END,"Paragraph 1: The Thristy Corw");
paragraphs_list.insert(END,"Paragraph 2: Quaid-e-Azam");
paragraphs_list.insert(END,"Paragraph 3: The Holey Profit");
paragraphs_list.insert(END,"Paragraph 4: Honesty is the best policy");
paragraphs_list.insert(END,"Paragraph 5: Greedy is Cris");
#start button
test_start = Button(typingtext_Fram,text="Start Test",font='18',bd=1,relief=SOLID,activebackground=main_bg_color,activeforeground="green",bg=main_bg_color,fg="white",width=10,height=2)
test_start.place(x=60,y=380)
# &&&&&&&&&&&&&&&&&& End typing test frame &&&&&&&&&&&&&&&&&&

#-------------------- games frame -----------------
games_Fram = Frame(main_box,bg=bg_color,width=640,height=572)
Label(games_Fram,text="Gammes",fg=bg_text_color,bg=bg_color,font=bg_title_font).place(x=5,y=0);
Label(games_Fram,text="Comming Soon",font="Arial 50 bold",bg=bg_color,fg=main_bg_text_color).place(x=90,y=200)
# &&&&&&&&&&&&&&&&&&& End games Frame &&&&&&&&&&&&&
# ---------------------- setting frame -----------------------
setting_Fram = Frame(main_box,bg=bg_color,width=640,height=572)
Label(setting_Fram,text="Typing Master Setting",fg=bg_text_color,bg=bg_color,font=bg_title_font).place(x=5,y=0);

sound_label = Label(setting_Fram,text="Sound",bg=bg_color,fg=acitve_main_fg_color,font=acitve_main_font)
sound_label.place(x=50,y=80);
speed_label = Label(setting_Fram,text="Speed",bg=bg_color,fg=acitve_main_fg_color,font=acitve_main_font)
speed_label.place(x=240,y=80);
screensize_label = Label(setting_Fram,text="Screen Size",bg=bg_color,fg=acitve_main_fg_color,font=acitve_main_font)
screensize_label.place(x=428,y=80);
#Sound box
selected_sound = StringVar()
avaliable_sounds = ('Sound on','Sound of')
sound_box = ttk.Combobox(setting_Fram, width=15,textvariable=selected_sound, state='readonly')
sound_box['values'] = avaliable_sounds;
sound_box.current(avaliable_sounds.index('Sound on'))
sound_box.place(x=50,y=110)
#Speed box
selected_speed = StringVar()
avaliable_speed = ('KPM (keystrokes/min)','WPM (words/min)')
speed_box = ttk.Combobox(setting_Fram, width=20,textvariable=selected_speed, state='readonly')
speed_box['values'] = avaliable_speed;
speed_box.current(avaliable_speed.index("WPM (words/min)"));
speed_box.place(x=240,y=110)
#screensize box
selected_screensize = StringVar()
avaliable_screensize = ('Maximized Window','Small Window')
screensize_box = ttk.Combobox(setting_Fram, width=20,textvariable=selected_screensize, state='readonly')
screensize_box['values'] = avaliable_screensize;
screensize_box.current(avaliable_screensize.index("Maximized Window"));
screensize_box.place(x=428,y=110)
#playmusic
playmusicvar = StringVar();
playmusic = Checkbutton(setting_Fram,pady=10,padx=10,text="Play Music",onvalue=1,offvalue=0,variable=playmusicvar,font=bg_text_font,bd=0,relief=FLAT,activebackground=bg_color,activeforeground=main_bg_text_color,bg=bg_color,fg=main_bg_text_color)
playmusic.place(x=50,y=150);
#line
line = Label(setting_Fram,bd=1,relief=SOLID,bg="lightgray")
line.place(x=28,y=240,width=590,height=0);
# keyboard layour
Label(setting_Fram,text="Keyboard Layout",bg=bg_color,fg=main_bg_color,font=('time new roman',15,'bold')).place(x=50,y=280);
#set keyboard image
imgget = Image.open("images\\keyboard.png");
#set value which we wanted to width - of window widht 
resize_img = imgget.resize((400,200))
keyboard_img = ImageTk.PhotoImage(image=resize_img);
Label(setting_Fram,image=keyboard_img).place(x=120,y=310);
Label(setting_Fram,text="Default (English US)",bg=bg_color).place(x=280,y=520);
# setting_Fram.pack(anchor='nw',side='top');
# &&&&&&&&&&&&&&&&&&& End setting frame &&&&&&&&&&&&&&&&&&&&&&
#------------------------- about frame --------------------------------
about_Fram = Frame(main_box,bg=bg_color,width=640,height=572)
Label(about_Fram,text="Information",fg=bg_text_color,bg=bg_color,font=bg_title_font).place(x=5,y=0);
#title
Label(about_Fram,text="Typing Master Lite",bg=bg_color,fg=main_bg_text_color,pady=5,font=acitve_main_font).place(x=70,y=100)
#line
line = Label(about_Fram,bd=1,relief=SOLID,bg="lightgray")
line.place(x=80,y=140,width=280,height=0);
#information title
Label(about_Fram,text="Version   : ",bg=bg_color,fg="black",font="arial 12 bold").place(x=82,y=170);
Label(about_Fram,text="Build       : ",bg=bg_color,fg="black",font="arial 12 bold").place(x=82,y=220);
Label(about_Fram,text="User        : ",bg=bg_color,fg="black",font="arial 12 bold").place(x=82,y=280);
Label(about_Fram,text="License  : ",bg=bg_color,fg="black",font="arial 12 bold").place(x=82,y=320);
# title information
Label(about_Fram,text="1.0 [2021]",bg=bg_color,fg=main_bg_text_color,font=("Calibri (Body)",11,'bold')).place(x=200,y=170);
Label(about_Fram,text="Umair Saeed",bg=bg_color,fg=main_bg_text_color,font=("Calibri (Body)",11)).place(x=200,y=220);
Label(about_Fram,text="------",bg=bg_color,fg=main_bg_text_color,font=("Calibri (Body)",11)).place(x=200,y=280);
Label(about_Fram,text="Single Workstation",bg=bg_color,fg=main_bg_text_color,font=("Calibri (Body)",11)).place(x=200,y=320);
#line
line = Label(about_Fram,bd=1,relief=SOLID,bg="lightgray")
# line.place(x=80,y=400,width=280,height=0);
# about_Fram.pack(anchor='nw',side='top');
# &&&&&&&&&&&&&&&&&&&&&& End about frame &&&&&&&&&&&&&&&&&&&&&&
# &&&&&&&&&&&&&&&&&&&&&&&& End Create Main Box &&&&&&&&&&&&&&&&&&&&&&&&

#------------------------------- Main manue Button Functionality -------------------------------

# ----------------------------------- pack all manue button ------------------------------------
# studying_btn.place(x=btn_X,y=btn_Y,width=btn_width,height=btn_height);
# typingTest_btn.place(x=btn_X,y=btn_Y,width=btn_width,height=btn_height);
# games_btn.place(x=btn_X,y=btn_Y,width=btn_width,height=btn_height);
# setting_btn.place(x=btn_X,y=btn_Y,width=btn_width,height=btn_height);
# about_btn.place(x=btn_X,y=btn_Y,width=btn_width,height=btn_height);
# set_icone.place(x=660,y=490);
# ================================= End pack all manue button ====================================

#&&&&&&&&&&&&&&&&&&&&&&&&& End Main manue Button Functionality &&&&&&&&&&&&&&&&&&&&&&&&&
window.mainloop()