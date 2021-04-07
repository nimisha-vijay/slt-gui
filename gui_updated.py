import PySimpleGUI as sg
import cv2
import numpy as np

"""
Demo program that displays a webcam using OpenCV
"""


def main():

    sg.theme('Black')

    # define the window layout
    layout = [
    					#[sg.Text('OpenCV Demo', size=(40, 1), justification='center', font='Helvetica 20')],
              [sg.Image(filename='', key='image')],
              [sg.Button('Record', key="RECORD", size=(10, 1), font='Helvetica 14'),
               sg.Button('Stop', size=(10, 1), font='Any 14'),
               sg.Button('Exit', size=(10, 1), font='Helvetica 14'), ]]


    window = sg.Window('OpenCV Integration',
                       layout, location=(800, 400))

    cap = cv2.VideoCapture(0)
    recording = True

    while True:
        event, values = window.read(timeout=20)
        
        if event == 'Exit' or event == sg.WIN_CLOSED:
            return

        elif event == "RECORD":
        		recording = True
        		window["RECORD"].update(text="Recording", button_color="#FFFF00")    

        elif event == 'Stop':
            recording = False
            window["RECORD"].update(text="Record", button_color="#FFFFFF")   
         #   img = np.full((480, 640), 255)
            # this is faster, shorter and needs less includes
            imgbytes = cv2.imencode('.png', frame)[1].tobytes()
            window['image'].update(data=imgbytes)

        if recording:
            ret, frame = cap.read()
            imgbytes = cv2.imencode('.png', frame)[1].tobytes()  # ditto
            window['image'].update(data=imgbytes)


main()
