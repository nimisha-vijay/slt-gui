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
                        sg.Button('Help', key="HELP", size=(8, 1), font='Helvetica 14'), ]
                ]
               
    messageScreen = [
                        [sg.Text('Nice to meet you', size=(40, 2), justification='left', font='Helvetica 20')],
                        [sg.Button('Back', key="BACK", size=(8, 1), font='Helvetica 14'),]
                    ]
    layout = [
                [   sg.Column(startScreen, visible=True, key="STARTSCREEN"), 
                    sg.Column(appScreen, visible=False, key="APPSCREEN"),
                    sg.Column(messageScreen, visible=False, key="MSGSCREEN"),]]

    window = sg.Window('Sign Language Translator',
                       layout, location=(0, 0),
                       no_titlebar=True,
                       size=(480,320))

    cap = cv2.VideoCapture(0)
    recording = False
    video = []

    while True:
        event, values = window.read(timeout=10)
        
        if event == 'Exit' or event == sg.WIN_CLOSED:
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
            recording = False
              

        ret, frame = cap.read()
        # cv2.waitKey(1)
        img = frame[0:240, 0:480]
        imgbytes = cv2.imencode('.png', img)[1]
        # .tobytes()  # ditto
        # cv2.imwrite("temp.png", img)
        # print(img)
        imgbytes = imgbytes.tobytes()
        window['image'].update(data=imgbytes)
        
        if recording:
            video.append([frame])
            cnt += 1
            window["RECORD"].update(text="Recording... " + str(int(cnt/7) + 1), button_color="#FFFF00")
            window["STOP"].update(visible=True)
            window["HELP"].update(visible=False)
        else:
            cnt = 0
            window["RECORD"].update(text="Record", button_color="#FFFFFF") 
            window["STOP"].update(visible=False)
            window["HELP"].update(visible=True)
        
        if cnt == 20:
            # processVideo(video)
            video = []
            recording = False
            cnt = 0
            window["STARTSCREEN"].update(visible=False)
            window["APPSCREEN"].update(visible=False)
            window["MSGSCREEN"].update(visible=True)
        


main()
