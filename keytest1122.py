from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import time
window = Tk()
window_width =  window.winfo_screenwidth();
window_height = window.winfo_screenheight();
# window_width = 1000;
# window_height = 700;
'''
     if window width is 900x800
          x=window_width/6-110,y=window_height/6+30

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
bg_main_title_color = "#333300";
# main_bg_color = "#17365d";
main_bg_color = "#624ad2";
main_bg_text_color = "#ffc000";
acitve_main_fg_color = "#1d1b11";
#set Font size code
bg_title_font = ("Agency FB",28,"underline");
bg_text_font = ("Cordia New",18,"bold","italic","underline");
main_text_font = ("AngsanaUPC",26);
acitve_main_font = ("Clarendon Lt BT",16,"bold");


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


# '''

# &&&&&&&&&&&&================$$$$$$ Start keys Drill Window Frame &&&&&&&&&&&&================$$$$$$
######################## Global's variables of key lesson function #########################
word_1 = "";
word_2 = "";
word_3 = "";
word_4 = "";
key_exit_ftn = keys_pressed = final_time = initial_time = key_count = total_space = total_words = I = xx = yy = key_correct = key_wrong = yourporgress = 0;
text_pos = 80;
curr_rect_pos_x = 60;
curr_rect_pos_y = 100;
word = [];
import time
#$$$$$$$$$$$$$$$$$$$$$$ End Global's variables of key lesson function $$$$$$$$$$$$$$$$$$$$$$$$$$
def keylessons(file,allwords):
    global final_time, initial_time;
    def gettimes():
        result = time.localtime()
        hours = int(time.strftime("%H",result))
        minutes = int(time.strftime("%M",result))
        seconds = int(time.strftime("%S",result))
        return (hours*60*60)+(minutes*60)+seconds;
    initial_time = gettimes()
    left_side_bg = "#f0ffd6"
    right_side_bg = "#d2f69f"
    global key_exit_ftn;
    #get hand image
    handget = Image.open("images\\hand.jpg");
    sizeable_hand = handget.resize((480,150))
    hand_img = ImageTk.PhotoImage(image=sizeable_hand);
    #get keybord image
    keybordget = Image.open("images\\keybord.png");
    resize_keybord = keybordget.resize((500,180))
    keybord_img = ImageTk.PhotoImage(image=resize_keybord);
    # -------------------------- Define right side Frame 
    right_side_Frame = Frame(main_box,bg=right_side_bg,width=192,height=window_height/2+60)
    right_canvas = Canvas(right_side_Frame,bg=right_side_bg,width=185,height=window_height/2+60)
    # --------------------- left Side frame --------------------
    left_side_Frame = Frame(main_box,bg=left_side_bg,width=630,height=window_height/2+43)
    left_canvas = Canvas(left_side_Frame,bg=left_side_bg,width=630,height=window_height/2+38);
    def oks(event=None):
        print('oks called')
        

    ok_btn = Button(right_canvas,text="OK",font=("time new roman",15),activebackground=right_side_bg,padx=5,relief="solid",bg="#d2f69f",bd=1,width=10,command=oks);
    print("ok ftn value : ",oks())
    def fun_exit(event=None):
        global key_correct,key_wrong,key_exit_ftn;
        key_exit_ftn = 1;
        key_correct = key_correct//5
        key_wrong = key_wrong//5
        Label(left_side_Frame,font=bg_title_font,bg=left_side_bg,text="Exercise Result").place(x=5,y=5);
        Label(left_side_Frame,bg=left_side_bg,font=main_text_font,text="Time Used       :").place(x=40,y=125);
        Label(left_side_Frame,bg=left_side_bg,font=main_text_font,text="Gross Speed    :").place(x=40,y=175);
        Label(left_side_Frame,bg=left_side_bg,font=main_text_font,text="Accuracy        :").place(x=40,y=225);
        Label(left_side_Frame,bg=left_side_bg,font=main_text_font,text="Net Speed       :").place(x=40,y=275);
        # Label(left_side_Frame,bg=left_side_bg,font=main_text_font,fg="red",text="Remark about exercise").place(x=30,y=400);
        left_canvas.pack_forget()
        exit_btn.place_forget();
        ok_btn.place(x=30,y=450);
        # Calculation of Progress
        final_time = gettimes();
        total_time = final_time-initial_time
        print("Toatal Time = ",total_time)
        Min = Sec = t_m = 0;
        gross = net = accuracy = 1;
        if(total_time >= 60):
            Min = total_time//60;
            Sec = total_time%60;
        else:
            Sec = total_time;
        if keys_pressed >=5:
            t_m = total_time/60;
            gross = (key_correct+key_wrong)//t_m;
            net = gross-key_wrong//t_m;
            accuracy = 100.0 * net//gross;
        else:
            gross = net = accuracy = '0';
        Label(left_side_Frame,bg=left_side_bg,font=main_text_font,text=f"{Min} : {Sec} min").place(x=240,y=125);
        Label(left_side_Frame,bg=left_side_bg,font=main_text_font,text=f"{int(gross)} WPM").place(x=240,y=175);
        Label(left_side_Frame,bg=left_side_bg,font=main_text_font,text=f"{int(accuracy)} %").place(x=240,y=225);
        Label(left_side_Frame,bg=left_side_bg,font=main_text_font,text=f"{int(net)} WPM").place(x=240,y=275);    
        if int(net) <= 15:
            Label(left_side_Frame,bg=left_side_bg,font=main_text_font,fg="red",text="Not Good Work! Next time do best").place(x=30,y=400);
        elif int(net) >= 16:
            Label(left_side_Frame,bg=left_side_bg,font=main_text_font,fg="red",text="Good Work! Next time do best").place(x=30,y=400);
        elif int(net) >= 28:
            Label(left_side_Frame,bg=left_side_bg,font=main_text_font,fg="red",text="Greet Work! Next time do best").place(x=30,y=400);
        else:
            Label(left_side_Frame,bg=left_side_bg,font=main_text_font,fg="red",text="Excelent Work! Next time do best").place(x=30,y=400);
        ###################################################################
    exit_btn = Button(right_canvas,text="Next",font=("time new roman",15),activebackground=right_side_bg,padx=5,relief="solid",bg="#d2f69f",bd=1,width=10,command=fun_exit);
    exit_btn.place(x=30,y=450);
    def rectangle(x,y,word):
        j1 = 60;
        j2 = 100;
        for item in range(4):
            left_canvas.create_rectangle(j1+x,40+y,j2+x,80+y,fill="white")    
            j1 += 45;
            j2 += 45;
        left_canvas.create_rectangle(260-20+x,55+y,320-20+x,80+y,fill="white")
        left_canvas.create_text(270+x,67+y,text="Space",font=('Cordia New',20,"bold"));
        i = 80;
        for item in word:
            left_canvas.create_text(i+x,60+y,text=f"{item}",font=('Cordia New',30,"bold"));
            i += 45;
    # get all element from the file or lession
    # allwords = file.readlines()
    # file.close();
    ######################################
    # -------------update the words ---------------------
    def updateword(event=None):
        global word_1, word_2, word_3, word_4,total_words;
        # word_1 = allwords[total_words];
        # total_words += 1
        # word_2 = allwords[total_words];
        # total_words += 1
        # word_3 = allwords[total_words];
        # total_words += 1
        # word_4 = allwords[total_words];
        # total_words += 1
        word_1 = allwords[19];
        word_2 = allwords[20];
        word_3 = allwords[21];
        word_4 = allwords[22];
        rectangle(0,0,word_1);
        rectangle(290,0,word_2);
        rectangle(0,80,word_3);
        rectangle(290,80,word_4);
    ##########################################
    updateword();
    left_canvas.create_image(100,410,image=hand_img,anchor='nw')
    left_canvas.create_image(330,325,image=keybord_img,anchor='center')
       # key dict 
    keybord_Key_Pos = {"q" : "45,9,75,40","w" : "85,9,110,40","e" : "125,9,150,40","r" : "160,9,185,40", "t" : f"{280-80},{242-233},{305-80},{277-237}","y" : f"{315-80},{242-233},{340-80},{277-237}","i" : f"{390-80},{242-233},{415-80},{277-237}","u" : f"{355-80},{242-233},{380-80},{277-237}","o" : f"{430-80},{242-233},{455-80},{277-237}","p" : f"{465-80},{242-233},{493-80},{277-237}", "a" : f"{130-80},{287-233},{160-80},{320-237}", "s" : f"{170-80},{287-233},{197-80},{320-237}","d" : f"{210-80},{287-233},{234-80},{320-237}","f" : f"{245-80},{287-233},{271-80},{320-237}","g" : f"{285-80},{287-233},{308-80},{320-237}","h" : f"{320-80},{287-233},{345-80},{320-237}","j" : f"{360-80},{287-233},{382-80},{320-237}", "k" : f"{395-80},{287-233},{419-80},{320-237}", "l" : f"{435-80},{287-233},{459-80},{320-237}", ";" : f"{470-80},{287-233},{500-80},{320-237}","z" : f"{150-80},{330-233},{178-80},{360-237}","x" : f"{190-80},{330-233},{215-80},{362-237}", "c" : f"{225-80},{330-233},{252-80},{363-237}", "v" : f"{265-80},{330-233},{289-80},{363-237}","b" : f"{300-80},{330-233},{326-80},{363-237}","n" : f"{340-80},{330-233},{363-80},{363-237}", "m" : f"{375-80},{330-233},{403-80},{363-237}","," : f"{415-80},{330-233},{440-80},{363-237}","." : f"{450-80},{330-233},{477-80},{363-237}", "/" : f"{490-80},{330-233},{514-80},{363-237}","space" : f"{125},{142},{370},{170}",};
    left_canvas.pack()
    def wordsrtupdate(event=None):
        global word
        word = list(word_1 + word_2 + word_3 + word_4)
        print(word);
        word.remove('\n')
        word.remove('\n')
        word.remove('\n')
        word.remove('\n')
        word.insert(4,"space");
        word.insert(9,"space");
        word.insert(14,"space");
        word.insert(20,"space");
        print(word);
    wordsrtupdate();
    def progressupdate(event=None):
        if yourporgress == 15:
            right_canvas.create_rectangle(145,90+15,170,250+15,fill='green')
        elif yourporgress == 12:
            right_canvas.create_rectangle(115-3,120+15,140-3,250+15,fill='green')
        elif yourporgress == 9:
            right_canvas.create_rectangle(85-6,150+15,110-6,250+15,fill='green')
        elif yourporgress == 6:
            right_canvas.create_rectangle(55-9,180+15,80-9,250+15,fill='green')
        elif yourporgress == 3:
            right_canvas.create_rectangle(25-12,210+15,50-12,250+15,fill='green')
    rect_text_font = ('Cordia New',30,"bold");
    # first part of rectangle
    left_canvas.create_rectangle(60,40,100,80,fill="green")
    left_canvas.create_text(80,60,text=f"{word_1[0]}",font=rect_text_font,fill='white');
    def keypressed(event=None):
        global keys_pressed,yourporgress,key_count,total_space,I,curr_rect_pos_x,curr_rect_pos_y,xx,yy,text_pos,key_correct,key_wrong;
        char = event.keysym;
        keys_pressed += 1;
        key_pos = keybord_Key_Pos.get(char);
        x1,y1,x2,y2 = key_pos.split(',');
        sub_left_canvas = Canvas(left_canvas,bg=left_side_bg,width=500,height=180);
        if char == word[I]:
            key_count += 1;
            key_correct += 1;
            if word[I] == 'space':
                left_canvas.create_rectangle(260-20+xx,55+yy,320-20+xx,80+yy,fill="gray")
                left_canvas.create_text(270+xx,67+yy,text="Space",fill='white',font=('Cordia New',20,"bold"));    
            else:
                left_canvas.create_rectangle(curr_rect_pos_x+xx,40+yy,curr_rect_pos_y+xx,80+yy,fill="gray")
                left_canvas.create_text(text_pos+xx,60+yy,text=f"{word[I]}",font=rect_text_font,fill='white');
            I += 1;
            curr_rect_pos_x += 45;
            curr_rect_pos_y += 45;
            text_pos += 45;
            sub_left_canvas.place_forget()
            sub_left_canvas.create_image(250,90,image=keybord_img,anchor='center')
            sub_left_canvas.place(x=80,y=235);
            # rectangle working ------------------------------------------------
            if key_count == 5:
                total_space += 1;
                key_count = 0;
                curr_rect_pos_x = 60;
                curr_rect_pos_y = 100;
                text_pos = 80;
                if  total_space == 1:
                    xx = 290;
                    yy = 0;
                elif total_space == 2:
                    xx = 0;
                    yy = 80;
                elif total_space == 3:
                    xx = 290;
                    yy = 80;
                else:
                    updateword();
                    wordsrtupdate();
                    yourporgress += 1;
                    I = 0;
                    key_count = total_space = 0;
                    text_pos = 80;
                    curr_rect_pos_x = 60;
                    curr_rect_pos_y = 100;
                    xx = 0;
                    yy = 0;
            if word[I] != 'space':
                left_canvas.create_rectangle(curr_rect_pos_x+xx,40+yy,curr_rect_pos_y+xx,80+yy,fill="green")
                left_canvas.create_text(text_pos+xx,60+yy,text=f"{word[I]}",font=rect_text_font);
            else:
                left_canvas.create_rectangle(260-20+xx,55+yy,320-20+xx,80+yy,fill="green")
                left_canvas.create_text(270+xx,67+yy,text="Space",fill='white',font=('Cordia New',20,"bold"));
            if yourporgress%3==0:
                progressupdate();
            if yourporgress == 15:
                fun_exit();
            # ---------------------------------------------------------------------------
        else:
            key_wrong += 1;
            if word[I] == 'space':
                left_canvas.create_rectangle(260-20+xx,55+yy,320-20+xx,80+yy,fill="red")
                left_canvas.create_text(270+xx,67+yy,text="Space",fill='white',font=('Cordia New',20,"bold"));
            else:
                left_canvas.create_rectangle(curr_rect_pos_x+xx,40+yy,curr_rect_pos_y+xx,80+yy,fill="red")
                left_canvas.create_text(text_pos+xx,60+yy,text=f"{word[I]}",font=rect_text_font,fill='white');
            # sub_left_canvas.place_forget()
            # sub_left_canvas = Canvas(left_canvas,bg=left_side_bg,width=500,height=180);
            sub_left_canvas.place_forget()
            sub_left_canvas.create_image(250,90,image=keybord_img,anchor='center')
            sub_left_canvas.create_line(int(x1),int(y1),int(x2),int(y2),width=3,fill="red");
            sub_left_canvas.place(x=80,y=235)
        
    
    # left_side_Frame.pack(side='top',anchor='w')
    left_side_Frame.place(x=0,y=0);
    # &&&&&&&&&&&&&&&&&&&& End left side frame &&&&&&&&&&&&&&&&&
    # next button
    nextget = Image.open("images\\next.jpg");
    resize_next = nextget.resize((150,50))
    next_img = ImageTk.PhotoImage(image=resize_next);
    # cancel button
    cancelget = Image.open("images\\cancel.jpg");
    resize_cancel = cancelget.resize((150,50))
    cancel_img = ImageTk.PhotoImage(image=resize_cancel);
    #----------------------- Right side Frame --------------------
    # right_side_Frame = Frame(main_box,bg=right_side_bg,width=192,height=window_height/2+60)
    # right_canvas = Canvas(right_side_Frame,bg=right_side_bg,width=185,height=window_height/2+60)
    cross_btn = right_canvas.create_text(170,25,text="X",font=('Calibri (Body)',11,'bold'),fill=main_bg_text_color);
    right_canvas.create_text(60,20+50,text="Your Progress",font=('Calibri (Body)',11,'bold'));
    right_canvas.create_line(10,34+50,180,34+50,fill="#bfbfbf",width=1)
    #progress Table
    right_canvas.create_rectangle(145,90+15,170,250+15)
    right_canvas.create_rectangle(115-3,120+15,140-3,250+15)
    right_canvas.create_rectangle(85-6,150+15,110-6,250+15)
    right_canvas.create_rectangle(55-9,180+15,80-9,250+15)
    right_canvas.create_rectangle(25-12,210+15,50-12,250+15)

    # right_canvas.create_rectangle(50,450,150,500)

    # right_canvas.create_image(95,450,image=next_img,anchor="center")
    # right_canvas.create_image(95,500,image=cancel_img,anchor="center")

    right_canvas.pack();

    right_side_Frame.pack(anchor='e',side='top')
    # while key_exit_ftn == 0:
    window.bind("<Key>",keypressed)
    # if (key_exit_ftn == 1):
    #     return;
    # else:
    input()
    # if key_exit_ftn == 1:
    #     file = open("key_files\lesson_1.txt");
    #     keylessons(file);
        
        # return;
        # print(key_exit_ftn)
    #&&&&&&&&&&&&&&&&&&&&& End Right side Fra&&&&&&&&&&&&&&&&&&&&&
    # &&&&&&&&&&&&================****** End Start keys Drill Window Frame ****=====================$$$$$$

# call the key lesson function


# %*#@($*(#*$ &&&&&&&&&&&&&&@#($*(@#$*()@#$*@$*(#$* (@&@$( )))))))
file = open("key_files\lesson_2.txt");
allwords = file.readlines()
keylessons(file,allwords)
file.close();
print("key lesson functon exit successfully ............");
# %*#@($*(#*$ &&&&&&&&&&&&&&@#($*(@#$*()@#$*@$*(#$* (@&@$( )))))))
# '''
# create frames of the above maue button
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
lesson_1_paragraphDrill.place(x=10,y=230)

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
lesson_2_paragraphDrill.place(x=10,y=230)

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
lesson_3_paragraphDrill.place(x=10,y=230)

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
paragraphs_list = Listbox(typingtext_Fram,width=30,height=5,font=('Cordia New',20,'bold'))
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
screensize_label.place(x=430,y=80);
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
screensize_box.place(x=430,y=110)
#playmusic
playmusicvar = StringVar();
playmusic = Checkbutton(setting_Fram,pady=10,padx=10,text="Play Music",onvalue=1,offvalue=0,variable=playmusicvar,font=bg_text_font,bd=0,relief=FLAT,activebackground=bg_color,activeforeground=main_bg_text_color,bg=bg_color,fg=main_bg_text_color)
playmusic.place(x=50,y=150);
#line
line = Label(setting_Fram,bd=1,relief=SOLID,bg="lightgray")
line.place(x=30,y=240,width=590,height=0);
# keyboard layour
Label(setting_Fram,text="Keyboard Layout",bg=bg_color,fg=main_bg_color,font=('time new roman',15,'bold')).place(x=50,y=270);
#set keyboard image
imgget = Image.open("images\\keyboard.png");
#set value which we wanted to width - of window widht 
resize_img = imgget.resize((400,200))
keyboard_img = ImageTk.PhotoImage(image=resize_img);
Label(setting_Fram,image=keyboard_img).place(x=120,y=310);
Label(setting_Fram,text="Default (English US)",bg=bg_color).place(x=270,y=520);
# setting_Fram.pack(anchor='nw',side='top');
# &&&&&&&&&&&&&&&&&&& End setting frame &&&&&&&&&&&&&&&&&&&&&&
#------------------------- about frame --------------------------------
about_Fram = Frame(main_box,bg=bg_color,width=640,height=572)
Label(about_Fram,text="Information",fg=bg_text_color,bg=bg_color,font=bg_title_font).place(x=5,y=0);
#title
Label(about_Fram,text="Typing Master Lite",bg=bg_color,fg=main_bg_text_color,pady=5,font=acitve_main_font).place(x=70,y=100)
#line
line = Label(about_Fram,bd=1,relief=SOLID,bg="lightgray")
line.place(x=80,y=140,width=300,height=0);
#information title
Label(about_Fram,text="Version   : ",bg=bg_color,fg="black",font="arial 12 bold").place(x=82,y=170);
Label(about_Fram,text="Build       : ",bg=bg_color,fg="black",font="arial 12 bold").place(x=82,y=220);
Label(about_Fram,text="User        : ",bg=bg_color,fg="black",font="arial 12 bold").place(x=82,y=270);
Label(about_Fram,text="License  : ",bg=bg_color,fg="black",font="arial 12 bold").place(x=82,y=320);
# title information
Label(about_Fram,text="1.0 [2021]",bg=bg_color,fg=main_bg_text_color,font=("Calibri (Body)",11,'bold')).place(x=200,y=170);
Label(about_Fram,text="Umair Saeed",bg=bg_color,fg=main_bg_text_color,font=("Calibri (Body)",11)).place(x=200,y=220);
Label(about_Fram,text="------",bg=bg_color,fg=main_bg_text_color,font=("Calibri (Body)",11)).place(x=200,y=270);
Label(about_Fram,text="Single Workstation",bg=bg_color,fg=main_bg_text_color,font=("Calibri (Body)",11)).place(x=200,y=320);
#line
line = Label(about_Fram,bd=1,relief=SOLID,bg="lightgray")
# line.place(x=80,y=400,width=300,height=0);
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