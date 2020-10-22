import PySimpleGUI as sg 
import nltk
import os.path
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def processfile(textfile):
    
#from nltk.stem import WordNetLemmatizer
#from nltk.probability import FreqDist
    
    
    f = open(textfile, encoding="utf8")
    ftext = f.read()
    nwln=ftext.split('\n')
    # If you would like to work with the novel in nltk.Text format you can use 'text1'
    tokens = nltk.word_tokenize(ftext)
    sentences=nltk.sent_tokenize(ftext)
    window['-FILE CONTENT-'].print("No. of words:",len(tokens))
    window['-FILE CONTENT-'].print("No. of sentences:",len(sentences))
    window['-FILE CONTENT-'].print("No. of newlines:",len(nwln))
    #text1 = nltk.Text(ftext)
    sw=nltk.corpus.stopwords.words('english')
    lemma=nltk.WordNetLemmatizer()
    text=[lemma.lemmatize(w.lower()) for w in tokens if len(w)>3]
    dist=nltk.FreqDist([word for word in text if word not in sw])
    dic=dict(dist)
    sorteddic=sorted(dic.items(), key = lambda ele: ele[1], reverse = True)[:20]
    window['-FILE CONTENT-'].print("Most frequent word:",sorteddic[0][0])
    
    f=[[x,y] for x,y in sorteddic]
    plt.bar([x[0] for x in f],[x[1] for x in f])
    plt.xticks(rotation=45)
    
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
    