import PySimpleGUI as sg 
import nltk
import os.path
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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

        sg.Multiline(

              size=(50, 5), key="-FILE CONTENT-"

        )

    ],
    [
        sg.Canvas(size=(30, 5), key='-CANVAS-')
    ],
    [
        sg.Button("KeyWords")
    ],
    [
        sg.Multiline(size=(50,5), key='keywords')
    ],

]
layout = [

    [

        sg.Column(file_list_column),


    ]

]   

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

window = sg.Window('Introduction_LAP_LAB3', layout) 

while True: 
    event, values = window.read() 
    #print(event, values) 
    
    if event in (None, 'Exit'): 
        break
    
    if event == 'Edit': 
        #plt.plot([0.1, 0.2, 0.5, 0.7])
        processfile(values['-FOLDER-'])
        fig=plt.gcf()
        fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, fig)
        #window['-FILE CONTENT-'].print(values['-FOLDER-'])
        #window['-FILE CONTENT-'].print("Bye")
        
        #print(values['-FOLDER-'])
        
        #Update the "output" text element 
        # to be the value of "input" element 
        
       # window['-OUTPUT-'].update(values['xx']) 

window.close() 
    