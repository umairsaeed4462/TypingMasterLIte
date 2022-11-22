# file = open("para.txt");
# all_words = file.read()
# file.close();
# print(717)
# # print(all_words)

# print(len(all_words))
# print(len(all_words)//717)

# start_p = 0;
# end_p = 722;
# word = all_words.replace('\n',' ');
# display_words = '';
# for item in range(start_p,end_p):
#     display_words += word[item];
# print(display_words)
# print(len(display_words))

# d = '  skadksdf akd ks dfkasdf sdksdkd';

# s = d[1:len(d)]

# print(s);
# print(len(s));

time_Min = 0;
time_Sec = 60;

def run_time():
    global time_Min,time_Sec;
    if time_Sec != 0:
        time_Sec -= 1;
    print("Time : ",time_Min,":",time_Sec);
    if time_Sec == 0 and time_Min !=0:
        time_Min -= 1;
        time_Sec = 60;
import time
for i in range(200):
    run_time();