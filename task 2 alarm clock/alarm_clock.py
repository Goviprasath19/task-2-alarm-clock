from threading import Thread
from tkinter.ttk import *
from tkinter import *

from PIL import Image, ImageTk

from pygame import mixer
from datetime import datetime
from datetime import datetime

from time import sleep


#colors for alarms 
bg_color = '#ffffff'
border_color = '#FFAC33'
border_color2 = 'white'



window = Tk()
window.title('Timer')
window.geometry('350x150')
window.configure(bg=bg_color)

# change and add a color for border orange
time_lines = Frame(window,width=500,height=6,bg=border_color)
time_lines.grid(row=0,column=0)


#background color for body to black
time_lines_body = Frame(window,width=500,height=400,bg=border_color2)
time_lines_body.grid(row=1,column=0)





#show image to body use icons 
image_timer = Image.open('icons.png')
image_timer.resize((100,100))
image_timer = ImageTk.PhotoImage(image_timer)

image_label = Label(time_lines_body,height=100,image=image_timer)
image_label.place(x=10,y=10)


# show text for heading
name = Label(time_lines_body,text='Alarm',height=1,font=('Ivy 14 bold'),bg=bg_color)
name.place(x=127,y=8)


hours = Label(time_lines_body,text='Hours',height=1,font=('Ivy 8 bold'),bg=bg_color)
hours.place(x=130,y=38)


select_hours = Combobox(time_lines_body,width=2,font='arial 14')
select_hours['values']=tuple(f"{i:02d}" for i in range(13))
select_hours.set('00')
select_hours.current(0)
select_hours.place(x=130,y=58)



hours = Label(time_lines_body,text='Minute',height=1,font=('Ivy 8 bold'),bg=bg_color)
hours.place(x=177,y=38)

select_minutes = Combobox(time_lines_body,width=2,font='arial 14')
select_minutes['values']=tuple(f"{i:02d}" for i in range(60))
select_minutes.set('00')
select_minutes.current(0)
select_minutes.place(x=180,y=58)





hours = Label(time_lines_body,text='Second',height=1,font=('Ivy 8 bold'),bg=bg_color)
hours.place(x=227,y=38)

select_seconds = Combobox(time_lines_body,width=2,font='arial 14')
select_seconds['values']=tuple(f"{i:02d}" for i in range(60))
select_seconds.set('00')
select_seconds.current(0)
select_seconds.place(x=230,y=58)





hours = Label(time_lines_body,text='Period',height=1,font=('Ivy 8 bold'),bg=bg_color)
hours.place(x=277,y=38)

select_amorpm = Combobox(time_lines_body,width=3,font='arial 14')
select_amorpm['values']=('AM','PM')
select_amorpm.set('')
select_amorpm.current(0)
select_amorpm.place(x=280,y=58)



def activateAlarm():
    time = Thread(target=alarm)
    time.start()


def deactivateAlarm():
    print('Deactivated',select.get())
    mixer.music.stop()

select = IntVar()

Button1 = Radiobutton(time_lines_body,font='arial 12 bold',text='Active',value=1,command=activateAlarm,variable=select)
Button1.place(x=125,y=95)







def AlarmSound():
    mixer.music.load('alarm mp3.mp3')
    mixer.music.play()
    select.set(0)

    Button2 = Radiobutton(time_lines_body,font='arial 12 bold',text='Deactive',value=2,command=deactivateAlarm,variable=select)
    Button2.place(x=210,y=95)




def alarm():
    while True:
        control = 1
        print(control)



        # Fetch the selected time from the Comboboxes
        alarm_hour = int(select_hours.get())
        alarm_minute = int(select_minutes.get())
        alarm_second = int(select_seconds.get())
        alarm_period = select_amorpm.get().upper()

        # Get the current time
        currentDateandTime = datetime.now()

        # Convert the current time to 12-hour format
        current_hour = int(currentDateandTime.strftime('%I'))
        current_minute = int(currentDateandTime.strftime('%M'))
        current_second = int(currentDateandTime.strftime('%S'))
        current_period = currentDateandTime.strftime('%p').upper()


        if control == 1:
            if alarm_period == current_period:
                if alarm_hour == current_hour:
                    if alarm_second == current_second:
                        print("Time to Wake Up")
                        AlarmSound()
                        break
        sleep(1)                



mixer.init()

#AlarmSound()



window.mainloop()