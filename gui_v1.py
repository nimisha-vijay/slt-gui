import PySimpleGUI as pysg
import subprocess
import time 

def showTranslated(text):
	window["TEXT"].update(text,visible=True)

def record():
	window["RECORD"].update(visible=False)
	window["CANCEL"].update(visible=True)
	window["TEXT"].update(visible=False)
	window["PROMPT"].update("Start recording in 3...")
	window.read(timeout=1000)
	window["PROMPT"].update("Start recording in 2...")
	window.read(timeout=1000)
	window["PROMPT"].update("Start recording in 1...")
	window.read(timeout=1000)
	
	sp = subprocess.Popen("python3 camera.py", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	window["PROMPT"].update("")
	while sp.poll() is None:
		pass

	text = "Nice to meet you"
	showTranslated(text)
		


pysg.theme('LightBlue')	 # Add a touch of color
# All the stuff inside your window.
layout = [	[pysg.Text("No data available", key="TEXT", visible=False)],[pysg.Text('Press record to start recording ', key="PROMPT")],  
						[pysg.Button('Record', key='RECORD'), pysg.Button('Cancel', key="CANCEL", visible=False)] ]

# Create the Window
window = pysg.Window('Sign Language Translator', layout, return_keyboard_events=True)
# Event Loop to process "events" and get the "values" of the inputs
while True:
	event, values = window.read()
	if event == pysg.WIN_CLOSED or event == 'Cancel' or event == 'q': # if user closes window or clicks cancel
		break
	if event == 'RECORD':
		record()		

		window["PROMPT"].update('Press record to start recording ')
		window["CANCEL"].update(visible=False)
		window["RECORD"].update(visible=True)

window.close()