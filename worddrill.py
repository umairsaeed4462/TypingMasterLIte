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
word1 = "";
word2 = "";
word3 = "";
key_Presse = finalTime = initialTime = keyCount = totatSpace = totalWords = Item = keyCorrect = keyWrong = your_porgress = 0;
words_Array = [];
active_text_pos = 0;
highlight_word = 0;
import time
#$$$$$$$$$$$$$$$$$$$$$$ End Global's variables of key lesson function $$$$$$$$$$$$$$$$$$$$$$$$$$
def word_drill_ftn(all_words):
    def reset_data(event=None):
        global key_Presse, finalTime, initialTime, keyCount, totatSpace, totalWords, Item, keyCorrect, keyWrong, your_porgress;
        global active_text_pos,highlight_word,words_Array;
        key_Presse = finalTime = initialTime = keyCount = totatSpace = totalWords = Item = keyCorrect = keyWrong = your_porgress = 0;
        words_Array = [];
        active_text_pos = 0;
        highlight_word = 0;
    reset_data();
    def gettimes():
        result = time.localtime()
        hours = int(time.strftime("%H",result))
        minutes = int(time.strftime("%M",result))
        seconds = int(time.strftime("%S",result))
        return (hours*60*60)+(minutes*60)+seconds;
    global keys_pressed,yourporgress,key_count,total_space,Item,text_pos;
    left_side_bg = "#f0ffd6"
    right_side_bg = "#d2f69f"
    #get hand image
    handget = Image.open("images\\hand.jpg");
    sizeable_hand = handget.resize((480,165))
    hand_img = ImageTk.PhotoImage(image=sizeable_hand);
    #get keybord image
    keybordget = Image.open("images\\keybord.png");
    resize_keybord = keybordget.resize((500,180))
    keybord_img = ImageTk.PhotoImage(image=resize_keybord);
    # -------------------------- Define right side Frame 
    right_side_Frame = Frame(main_box,bg=right_side_bg,width=192,height=window_height/2+60)
    right_canvas = Canvas(right_side_Frame,bg=right_side_bg,width=185,height=window_height/2+60)
    # --------------------- left Side frame --------------------
    left_side_Frame = Frame(main_box,bg=left_side_bg,width=628,height=window_height/2+43)
    left_canvas = Canvas(left_side_Frame,bg=left_side_bg,width=630,height=window_height/2+38);
    ################################ Keybord key layout &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    keybord_Key_Pos = {"q" : f"{45},{9-45},{75},{40-45}","w" : f"85,{9-45},110,{40-45}","e" : f"125,{9-45},150,{40-45}","r" : f"160,{9-45},185,{40-45}", 
    "t" : f"{280-80},{242-233-45},{285-80},{287-237-45}","y" : f"{315-80},{242-233-45},{340-80},{287-237-45}",
    "i" : f"{390-80},{242-233-45},{415-80},{287-237-45}","u" : f"{355-80},{242-233-45},{380-80},{287-237-45}",
    "o" : f"{428-80},{242-233-45},{455-80},{287-237-45}","p" : f"{465-80},{242-233-45},{493-80},{287-237-45}", 
    "a" : f"{128-80},{287-233-45},{160-80},{320-237-45}","s" : f"{170-80},{287-233-45},{197-80},{320-237-45}",
    "d" : f"{210-80},{287-233-45},{234-80},{320-237-45}","f" : f"{245-80},{287-233-45},{281-80-10},{320-237-45}",
    "g" : f"{285-80-8},{287-233-45},{288-80+20},{320-237-45}","h" : f"{320-80},{287-233-45},{345-80},{320-237-45}",
    "j" : f"{360-80},{287-233-45},{382-80},{320-237-45}","k" : f"{395-80},{287-233-45},{419-80},{320-237-45}", 
    "l" : f"{435-80},{287-233-45},{459-80},{320-237-45}",";" : f"{470-80},{287-233-45},{500-80},{320-237-45}",
    "z" : f"{150-80},{328-233-45},{178-80},{360-237-45}","x" : f"{190-80},{328-233-45},{215-80},{362-237-45}", 
    "." : f"{450-80},{328-233-45},{477-80},{363-237-45}","/" : f"{490-80},{328-233-45},{514-80},{363-237-45}",
    "c" : f"{225-80},{328-233-45},{252-80},{363-237-45}","v" : f"{265-80},{328-233-45},{289-80},{363-237-45}",
    "b" : f"{280-80+15},{328-233-45},{326-80},{363-237-45}","n" : f"{340-80},{328-233-45},{363-80},{363-237-45}", 
    "m" : f"{375-80},{328-233-45},{403-80},{363-237-45}","," : f"{415-80},{328-233-45},{440-80},{363-237-45}",
    "space" : f"{125},{142-45},{370},{170-45}","shift_r" : f"{450-80+73},{328-233-45},{477-80+95},{363-237-45}",
    "shift_l" : f"{150-80-60},{328-233-45},{178-80-40},{360-237-45}"};
    ################################ End Keybord key layout &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    def draw_word_on_GUI(x,y,word):
        i = 90;
        if len(word) <= 4:
            i = 90;
        else:
            i = 80;
        for count in range(3):
            for item in word:
                if count == 0:
                    left_canvas.create_text(i+x,100,text=f"{item}",font=('Cordia New',60,"bold"),fill='blue');
                else:
                    left_canvas.create_text(i+x,100,text=f"{item}",font=('Cordia New',60,"bold"));
                i += 28;
            if len(word) <= 4:
                x += 100;
            else:
                x += 75;
    def highlighted_ftn(word):
        i = 90;
        x = 0
        global highlight_word;
        if len(word) <= 4:
            i = 90;
        else:
            i = 80;
        for count in range(3):
            for item in word:
                if count == highlight_word+1:
                    left_canvas.create_text(i+x,100,text=f"{item}",font=('Cordia New',60,"bold"),fill='blue');
                i += 28;  
            if len(word) <= 4:
                x += 100;
            else:
                x += 75;
        highlight_word += 1;  
        if highlight_word == 3:
            highlight_word = 0;
        
    def words_update(event=None):
        global word1, word2, word3, totalWords;
        word1 = word2 = word3 = all_words[totalWords];
        totalWords += 1;
        draw_word_on_GUI(0,0,word2);
    words_update();
    def word_Array_Update(event=None):
        global words_Array;
        words_Array = list(word1 + word2 + word3)
        for i in range(3):
            words_Array.remove('\n');
        words_Array.insert(len(word1)-1,"space");
        words_Array.insert(len(word1)*2-1,"space");
        words_Array.insert(len(word1)*3-1,"space");
    word_Array_Update();
    def progress_update(event=None):
        if your_porgress == 50:
            right_canvas.create_rectangle(145,90+15,170,250+15,fill='green')
        elif your_porgress == 40:
            right_canvas.create_rectangle(115-3,120+15,140-3,250+15,fill='green')
        elif your_porgress == 30:
            right_canvas.create_rectangle(85-6,150+15,110-6,250+15,fill='green')
        elif your_porgress == 20:
            right_canvas.create_rectangle(55-9,180+15,80-9,250+15,fill='green')
        elif your_porgress == 10:
            right_canvas.create_rectangle(25-12,210+15,50-12,250+15,fill='green')
    # display keyboard and hand on screen
    left_canvas.create_image(100,390,image=hand_img,anchor='nw')
    left_canvas.create_image(328,280,image=keybord_img,anchor='center')

    word_drill_text_font = ('Cordia New',60,"bold");
    global active_text_pos;
    if len(word1) <= 4:
        active_text_pos = 90;
    else:
        active_text_pos = 80;
    def ok_ftn(event=None):
        global btn_X, btn_Y;
        btn_X = 640;
        btn_Y = 80;
        left_side_Frame.place_forget();
        right_side_Frame.pack_forget();
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
    okBtn = Button(right_canvas,text="OK",font=("time new roman",15),activebackground=right_side_bg,padx=5,relief="solid",bg="#d2f69f",bd=1,width=10,command=ok_ftn);
    def funExit(event=None):
        global finalTime,keyCorrect,keyWrong;
        keyCorrect = keyCorrect//5
        keyWrong = keyWrong//5
        Label(left_side_Frame,font=bg_title_font,bg=left_side_bg,text="Exercise Result").place(x=5,y=5);
        Label(left_side_Frame,bg=left_side_bg,font=main_text_font,text="Time Used       :").place(x=40,y=125);
        Label(left_side_Frame,bg=left_side_bg,font=main_text_font,text="Gross Speed    :").place(x=40,y=175);
        Label(left_side_Frame,bg=left_side_bg,font=main_text_font,text="Accuracy        :").place(x=40,y=225);
        Label(left_side_Frame,bg=left_side_bg,font=main_text_font,text="Net Speed       :").place(x=40,y=275);
        left_canvas.pack_forget()
        exit_btn.place_forget();
        okBtn.place(x=30,y=450);
        finalTime = gettimes();
        total_time = finalTime-initialTime;
        Min = Sec = t_m = 0;
        gross = net = accuracy = 1;
        if(total_time >= 60):
            Min = total_time//60;
            Sec = total_time%60;
        else:
            Sec = total_time;
        if key_Presse >=5:
            t_m = total_time/60;
            gross = (keyCorrect+keyWrong)//t_m;
            net = gross-keyWrong//t_m;
            accuracy = 100.0 * net//gross;
        else:
            gross = net = accuracy = '0';
        Label(left_side_Frame,bg=left_side_bg,font=main_text_font,text=f"{Min} : {Sec} min").place(x=240,y=125);
        Label(left_side_Frame,bg=left_side_bg,font=main_text_font,text=f"{int(gross)} WPM").place(x=240,y=175);
        Label(left_side_Frame,bg=left_side_bg,font=main_text_font,text=f"{int(accuracy)} %").place(x=240,y=225);
        Label(left_side_Frame,bg=left_side_bg,font=main_text_font,text=f"{int(net)} WPM").place(x=240,y=275);
        if int(net) <= 15:
            Label(left_side_Frame,bg=left_side_bg,font=main_text_font,fg="red",text="Not Good Work! Next time do best").place(x=30,y=400);
        elif int(net) <= 16:
            Label(left_side_Frame,bg=left_side_bg,font=main_text_font,fg="red",text="Good Work! Next time do best").place(x=30,y=400);
        elif int(net) <= 28:
            Label(left_side_Frame,bg=left_side_bg,font=main_text_font,fg="red",text="Greet Work! Next time do best").place(x=30,y=400);
        else:
            Label(left_side_Frame,bg=left_side_bg,font=main_text_font,fg="red",text="Excelent Work! Next time do best").place(x=30,y=400);
    exit_btn = Button(right_canvas,text="Next",font=("time new roman",15),activebackground=right_side_bg,padx=5,relief="solid",bg="#d2f69f",bd=1,width=10,command=funExit);
    exit_btn.place(x=30,y=450);
    def keypresse(event=None):
        global Item,keyCount,totatSpace,active_text_pos,your_porgress,keyCorrect,keyWrong,key_Presse,initialTime;
        if key_Presse == 0:
            initialTime = gettimes();
        key_Presse += 1;
        char = event.keysym;
        sub_left_canvas = Canvas(left_canvas,bg=left_side_bg,width=500,height=150);
        if char == words_Array[Item]:
            keyCorrect += 1;
            Item += 1;
            keyCount += 1;
            if char != 'space':
                left_canvas.create_text(active_text_pos,100,text=f"{char}",font=word_drill_text_font,fill=left_side_bg);
            active_text_pos += 28;
            if char == 'space':
                totatSpace += 1;
                if len(word1) <= 4:
                    active_text_pos += 100;
                else:
                    active_text_pos += 75;
                highlighted_ftn(word1); 
            if totatSpace == 3:
                left_canvas.delete("all");
                left_canvas.create_image(100,390,image=hand_img,anchor='nw')
                left_canvas.create_image(328,280,image=keybord_img,anchor='center')
                words_update();
                word_Array_Update();
                your_porgress += 1;
                Item = keyCount = totatSpace = 0;
                if len(word1) <= 4:
                    active_text_pos = 90;
                else:
                    active_text_pos = 80;
            if your_porgress%10 == 0:
                progress_update();
            if your_porgress == 50:
                funExit();
            sub_left_canvas.place_forget()
            sub_left_canvas.create_image(248,45,image=keybord_img,anchor='center')
            sub_left_canvas.place(x=80,y=235);
        else:
            if words_Array[Item] != 'space':
                left_canvas.create_text(active_text_pos,100,text=f"{words_Array[Item]}",font=word_drill_text_font,fill='red');
            keyWrong += 1;
            key_pos = keybord_Key_Pos.get(char.lower());
            x1,y1,x2,y2 = key_pos.split(',');
            sub_left_canvas.place_forget()
            sub_left_canvas.create_image(248,45,image=keybord_img,anchor='center')
            sub_left_canvas.create_line(int(x1),int(y1),int(x2),int(y2),width=3,fill="red");
            sub_left_canvas.place(x=80,y=235)
    window.bind("<Key>",keypresse) 

    left_canvas.pack()
    
        
    left_side_Frame.place(x=0,y=0);
    # &&&&&&&&&&&&&&&&&&&& End left side frame &&&&&&&&&&&&&&&&&
    #----------------------- Right side Frame --------------------  
    right_canvas.create_text(60,20+50,text="Your Progress",font=('Calibri (Body)',11,'bold'));
    right_canvas.create_line(10,34+50,180,34+50,fill="#bfbfbf",width=1)
    #progress Table
    right_canvas.create_rectangle(145,90+15,170,250+15)
    right_canvas.create_rectangle(115-3,120+15,140-3,250+15)
    right_canvas.create_rectangle(85-6,150+15,110-6,250+15)
    right_canvas.create_rectangle(55-9,180+15,80-9,250+15)
    right_canvas.create_rectangle(25-12,210+15,50-12,250+15)
    

    right_canvas.pack();

    right_side_Frame.pack(anchor='e',side='top')
    

# %*#@($*(#*$ &&&&&&&&&&&&&&@#($*(@#$*()@#$*@$*(#$* (@&@$( )))))))
file = open("word_files\lesson_1.txt");
all_words = file.readlines()
file.close();
word_drill_ftn(all_words)
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