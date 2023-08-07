import time
import subprocess
import datetime
import os
from playsound import playsound

today = datetime.datetime.now().date()

minute = 60000
p = 25*minute
b = 5*minute
h = 60*minute
deep = 90*minute
napping = 20*minute
vartti = 15*minute

count = 1

#1 import
import PySimpleGUI as sg

#2 layout
def start(count=1):
    sg.theme('DarkAmber')
    layout = [[sg.Text(f'Pomodoro number {count}', size=( 0,1))],
              [sg.Text('What is the ONE THING I CAN DO, such as BY DOING IT, everything else becomes easier or unnecessary?')],
              [sg.Input(key='-INPUT-')],
              [sg.Button('DEEP'), sg.Button('Start', bind_return_key=True), sg.Button('Short Break'), sg.Button('Long Break'), sg.Button('Kill Pomodoro')],
              [sg.Text('20% Solution')]
              ]

    #3 create window
    window = sg.Window('Pomodoro Timer', layout, keep_on_top = True)

    #4 Input window
    event, values = window.read()
    global working_on
    working_on = values['-INPUT-']

    #5 close window
    if event == 'Start':
        file = open('pomodoro.txt', 'a')
        file.write('\n')
        file.write(str(today) + ' ')
        file.write(str(count) + ' ')
        file.write(str(working_on))
        file.close()
        window.close()
        work(count)
    elif event == 'DEEP':
        file = open('pomodoro.txt', 'a')
        file.write('\n')
        file.write(str(today) + ' ')
        file.write('DEEP ')
        file.write(str(working_on))
        file.close()
        window.close()
        deep(count)
    elif event == 'Short Break':
        window.close()
        breaks(count)
    elif event == 'Long Break':
        window.close()
        long_break(count)       
    else:
        window.close()
    
def work(count):
    sg.theme('DarkBlue2')
    layout   = [[sg.Text(f'Pomodoro number {count}', size=(20,1))],
                [sg.Text(f'Your ONE THING TO DO is {working_on}')],
                [sg.Text(size=(20,1), key='-OUT-')],
                [sg.Button('Got distracted'), sg.Button('Kill Pomodoro')],
                ]
    window = sg.Window('WORK', layout, keep_on_top = True,location=(1300,100))

    timer = p

    while timer > 0:
        event, values = window.read(timeout=1000)
        if event is None or event == 'Kill Pomodoro':
            window.close()
            break
        elif event == 'Got distracted':
            window.close()
            start(count)
        window['-OUT-'].update(int(timer/60000))
        timer -= 1000
        
    if timer < 1:
        count +=1
        if count == 5 or count == 9:
#long pause music
            playsound("smb3_airship_clear.wav")
            #subprocess.Popen(['start', 'smb3_airship_clear.wav'], shell=True)
            #time.sleep(10)
            #os.system('TASKKILL /F /IM mpc-be64.exe')
            window.close()
            long_break(count)
        else:
        #music done work
            playsound("smb_world.wav")
            window.close()
            breaks(count)                    
            window.close()

def deep(count):
    sg.theme('DarkGreen5')
    layout   = [[sg.Text(f'Deep Focus', size=(20,1))],
                [sg.Text(f'{working_on}')],
                [sg.Text(size=(20,1), key='-OUT-')],
                [sg.Button('Got distracted'), sg.Button('Kill Pomodoro')],
                ]
    window = sg.Window('DEEP', layout, keep_on_top = True,location=(1300,100))

    timer = 5400000

    while timer > 0:
        event, values = window.read(timeout=1000)
        if event is None or event == 'Kill Pomodoro':
            window.close()
            break
        elif event == 'Got distracted':
            window.close()
            start(count)
        window['-OUT-'].update(int(timer/60000))
        timer -= 1000
        
    if timer < 1:
        #long pause music
        playsound("smb3_airship_clear.wav")
        window.close()
        long_break(count)


def test():
    while timer > 0:
        event, values = window.read(timeout=1000)
        if event is None or event == 'Kill Pomodoro':
            window.close()
            break
        elif event == 'Got distracted':
            window.close()
            start(count)
        window['-OUT-'].update(int(timer/60000))
        timer -= 1000
        
    if timer < 1:
            #long pause music
            playsound("smb3_airship_clear.wav")
            window.close()
            long_break(count)            
            
def breaks(count):
    sg.theme('DarkGreen1')
    layout   = [[sg.Text('BREAK', size=(20,1))],
                [sg.Text('One breath, Break and Move')],
                [sg.Text('Remaining break')],
                [sg.Text(size=(20,1), key='-OUT-')],
                [sg.Button('New Pomodoro'), sg.Button('Kill Pomodoro')],
                ]
    window = sg.Window('BREAK', layout, keep_on_top = True)

    timer = b
    while timer > 0:
        event, values = window.read(timeout=1000)
        if event is None or event == 'Kill Pomodoro':
            break
        elif event == 'New Pomodoro':
            window.close()
            start(count)
        window['-OUT-'].update(int(timer/60000))
        timer -= 1000
    if timer < 1:
#music to start working
        playsound("smw_course_clear.wav")
#        subprocess.Popen(['start', 'smw_course_clear.wav'], shell=True)
#        time.sleep(9)
#        os.system('TASKKILL /F /IM mpc-be64.exe')
        window.close()
        start(count)        
    else:
        window.close()
    

def long_break(count):
    sg.theme('DarkPurple1')
    layout   = [[sg.Text('LONG BREAK', size=(20,1))],
                [sg.Text('One breath, Break and Move')],
                [sg.Text('Remaining break')],
                [sg.Text(size=(20,1), key='-OUT-')],
                [sg.Button('New Pomodoro'), sg.Button('Kill Pomodoro')],
                ]
    window = sg.Window('LONG BREAK', layout, keep_on_top = True)
    
    timer = h
    while timer > 0:
        event, values = window.read(timeout=1000)
        if event is None or event == 'Kill Pomodoro':
            break
        elif event == 'New Pomodoro':
            window.close()
            start(count)
        window['-OUT-'].update(int(timer/60000))
        timer -= 1000        
    if timer < 1:
        #music to start working
        playsound('smw_course_clear.wav')
        window.close()
        start(count)
    else:
        window.close()

start()
