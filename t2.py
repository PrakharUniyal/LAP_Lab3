import PySimpleGUI as sg 
import os.path
	
# sg.theme('BrightColors')
sg.theme('Topanga')

file_list_column = [

    [

        sg.Text("File"),

        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),

        sg.FileBrowse(),

    ],
    [sg.Button("Edit"), sg.Button("Refresh")],

    [

        sg.Listbox(

            values=['Sentences: __Words: __'], enable_events=True, size=(30, 10), key="-FILE CONTENT-"

        )

    ],
    [
        sg.Listbox(values=["__Histogram__"], size=(30, 10), key='histogram')
    ],
    [
        sg.Button("KeyWords")
    ],
    [
        sg.Listbox(values=[" __Sentences with keywords__"], size=(30,10), key='keywords')
    ],

]
layout = [

    [

        sg.Column(file_list_column),


    ]

]   


window = sg.Window('Introduction_LAP_LAB3', layout) 

while True: 
	event, values = window.read() 
	print(event, values) 
	
	if event in (None, 'Exit'): 
		break
	
	if event == 'Edit': 
		# Update the "output" text element 
		# to be the value of "input" element 
		window['-OUTPUT-'].update(values['xx']) 

window.close() 
