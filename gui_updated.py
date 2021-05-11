import PySimpleGUI as sg
import cv2
import numpy as np
import time

def main():

    sg.theme('LightBLue2')

    # define the window layout
    startScreen =   [
                        [sg.Text('Sign Language Translator', size=(40, 1), justification='left', font='Helvetica 20')],
                        [sg.Text('Point the camera towards the signer and press record', size=(40, 2), justification='left', font='Helvetica 14')],
                        [sg.Button('Start', key="START", size=(8, 1), font='Helvetica 14'),]
                    ]
    
    appScreen = [
                    [sg.Image(filename='', key='image')],
                    [   sg.Button('Record', key="RECORD", size=(10, 1), font='Helvetica 14'),
                        sg.Button('Stop', key="STOP", size=(8, 1), visible=False, font='Helvetica 14'),
                        sg.Button('Go Back', key="HELP", size=(8, 1), font='Helvetica 14'), 
                        sg.Button('Exit', key="EXIT", size=(8, 1), font='Helvetica 14'), ]
                ]
               
    messageScreen = [
                        [sg.Text('The translated text is', size=(40, 1), justification='left', font='Helvetica 16')],
                        [sg.Text('Take care', size=(40, 2), justification='left', font='Helvetica 20')],
                        [sg.Button('Back', key="BACK", size=(8, 1), font='Helvetica 14'), 
                            sg.Button('Exit', key="EXIT", size=(8, 1), font='Helvetica 14'),]
                    ]
    layout = [
                [   sg.Column(startScreen, visible=True, key="STARTSCREEN"), 
                    sg.Column(appScreen, visible=False, key="APPSCREEN"),
                    sg.Column(messageScreen, visible=False, key="MSGSCREEN"),]]

    window = sg.Window('Sign Language Translator',
                       layout, location=(0, 0),
                       no_titlebar=True,
                       size=(480,320))

    cap = cv2.VideoCapture("take care-12.mp4")
    recording = False
    video = []
    sec = 0
    stopped = False

    while True:
        event, values = window.read(timeout=1)
        
        if event == 'Exit' or event == sg.WIN_CLOSED or event == "EXIT":
            return
        
        elif event == "START":
            window["STARTSCREEN"].update(visible=False)
            window["APPSCREEN"].update(visible=True)
            window["MSGSCREEN"].update(visible=False)
            window["START"].update(text="Back")
        
        elif event == "BACK":
            window["STARTSCREEN"].update(visible=False)
            window["APPSCREEN"].update(visible=True)
            window["MSGSCREEN"].update(visible=False)
            
        elif event == "HELP":
            window["STARTSCREEN"].update(visible=True)
            window["APPSCREEN"].update(visible=False)
            window["MSGSCREEN"].update(visible=False)

        elif event == "RECORD":
            recording = True 

        elif event == 'STOP':
            time.sleep(1)
            stopped = True
              
        
        ret, frame = cap.read()
        
        img = cv2.resize(frame, (480, 240))
        imgbytes = cv2.imencode('.png', img)[1]
        # .tobytes()  # ditto
        # cv2.imwrite("temp.png", img)
        # print(img)
        imgbytes = imgbytes.tobytes()
        window['image'].update(data=imgbytes)
        
        if recording:
            video.append([frame])
            cnt += 1
            window["RECORD"].update(text="Recording... ", button_color="#FFFF00")
            window["STOP"].update(visible=True)
            window["HELP"].update(visible=False)
        else:
            cnt = 0
            window["RECORD"].update(text="Record") 
            window["STOP"].update(visible=False)
            window["HELP"].update(visible=True)
        
        if stopped:
            process = 1
            video = []
            recording = False
            cnt = 0
            window["STARTSCREEN"].update(visible=False)
            window["APPSCREEN"].update(visible=False)
            window["MSGSCREEN"].update(visible=True)
        


main()
