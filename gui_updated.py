import PySimpleGUI as sg
import cv2
import numpy as np
import time
import asyncio



async def main():
    
    
    sg.theme('Black')

    # define the window layout
    startScreen = [
                [sg.Text('Sign Language Translator', size=(40, 1), justification='left', font='Helvetica 20')],
                [sg.Text('Point the camera towards the signer and press record', size=(40, 1), justification='left', font='Helvetica 14')],
                [sg.Button('Start', key="START", size=(8, 1), font='Helvetica 14'),]
                    ]
    
    appScreen = [
              [sg.Image(filename='', key='image')],
              [sg.Button('Record', key="RECORD", size=(8, 1), font='Helvetica 14'),
               sg.Button('Stop', size=(8, 1), font='Helvetica 14'), ]
               ]
               
    messageScreen = [
                        [sg.Text('Nice to meet you', size=(40, 1), justification='left', font='Helvetica 14')],
                        [sg.Button('Back', key="BACK", size=(8, 1), font='Helvetica 14'),]
                    ]
    layout = [
                [sg.Column(startScreen, visible=True, key="STARTSCREEN"), 
                sg.Column(appScreen, visible=False, key="APPSCREEN"),
                sg.Column(messageScreen, visible=False, key="MSGSCREEN"),]]

    window = sg.Window('OpenCV Integration',
                       layout, location=(0, 0),
                       no_titlebar=True,
                       size=(480,320))

    cap = cv2.VideoCapture(0)
    recording = False
    video = []

    while True:
        event, values = window.read(timeout=100)
        
        if event == 'Exit' or event == sg.WIN_CLOSED:
            return
        
        elif event == "START":
            window["STARTSCREEN"].update(visible=False)
            window["APPSCREEN"].update(visible=True)

        elif event == "RECORD":
            recording = True 

        elif event == 'Stop':
            recording = False
              

        ret, frame = cap.read()
        # cv2.waitKey(1)
        img = frame[0:270, 0:480]
        imgbytes = cv2.imencode('.png', img)[1].tobytes()  # ditto
        window['image'].update(data=imgbytes)
        
        if recording:
            video.append([frame])
            cnt += 1
            window["RECORD"].update(text="Recording", button_color="#FFFF00")
        else:
            cnt = 0
            window["RECORD"].update(text="Record", button_color="#FFFFFF") 
        
        if cnt == 20:
            # processVideo(video)
            video = []
            recording = False
            cnt = 0
        print(cnt, round(time.time()*1000))


asyncio.run(main())
