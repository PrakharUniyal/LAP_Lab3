import PySimpleGUI as sg 
import nltk
import os.path
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def processfile(textfile):
    
#from nltk.stem import WordNetLemmatizer
#from nltk.probability import FreqDist
    
    try:
    	f = open(textfile, encoding="utf8")
    	ftext = f.read()
    	nwln=ftext.split('\n')
    	nwords=0
    	for line in nwln:
        	nwords+=len(line.split())
    
    	# If you would like to work with the novel in nltk.Text format you can use 'text1'
    	tokens = nltk.word_tokenize(ftext)
    	sentences=nltk.sent_tokenize(ftext)
    
    	#text1 = nltk.Text(ftext)
    	sw=nltk.corpus.stopwords.words('english')
    	lemma=nltk.WordNetLemmatizer()
    	text=[lemma.lemmatize(w.lower()) for w in tokens if len(w)>2]
    	dist=nltk.FreqDist([word for word in text if word not in sw and len(word)>2])
    	dic=dict(dist)
    	sorteddic=sorted(dic.items(), key = lambda ele: ele[1], reverse = True)[:20]
    	window['-FILE CONTENT-'].print("Most frequent word:",sorteddic[0][0])
    	answer = "No. of words: " + str(len(tokens)) +'\nNo. of sentences: ' + str(len(sentences)) + "\nNo. of newlines: " + str(len(nwln)) + "\nMost frequent word: " + str(sorteddic[0][0])
    	window['-FILE CONTENT-'].update(value = answer)  
    
    	plt.bar([x[0] for x in f],[x[1] for x in f])
    	plt.xticks(rotation=45)
    except FileNotFoundError :
	pass
    
def extractline(textfile,keyword):
    f1 = open(textfile, encoding="utf8")
    f2 = open(keyword, encoding="utf8")
    ftext = f1.read()
    keywords=f2.read().split('\n')
    sentences=nltk.sent_tokenize(ftext)
    for sent in sentences:
        flag=False
        for word in keywords:
            if word in sent:
                flag=True
        if(flag):
            window['-EXTRACT-'].print(sent)
# sg.theme('BrightColors')
sg.theme("Black")

file_list_column = [

    [

        sg.Text("File"),

        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),

        sg.FileBrowse(),

    ],
    [sg.Button("Stats"), sg.Button("Refresh")],

    [

        sg.Multiline(

              size=(50, 5), key="-FILE CONTENT-"

        )

    ],
    [

        sg.Text("KeyWords File"),

        sg.In(size=(25, 1), enable_events=True, key="-KeyWord-"),

        sg.FileBrowse(),

    ],
    [
        sg.Button("Extract")
    ],
    [
        sg.Multiline(size=(50,5), key='-EXTRACT-')
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
    
    if event == 'Stats': 
        #plt.plot([0.1, 0.2, 0.5, 0.7])
        processfile(values['-FOLDER-'])
        #fig=plt.gcf()
        #fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, fig)
        
	

    if event == 'Refresh': 
        #plt.plot([0.1, 0.2, 0.5, 0.7])
        processfile(values['-FOLDER-'])
        #fig=plt.gcf()
        #fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, fig)



    if event == 'Extract':
        extractline(values['-FOLDER-'],values['-KeyWord-'])    
    #if event == 'Extract':
        
        #window['-FILE CONTENT-'].print(values['-FOLDER-'])
        #window['-FILE CONTENT-'].print("Bye")
        
        #print(values['-FOLDER-'])
        
        #Update the "output" text element 
        # to be the value of "input" element 
        
       # window['-OUTPUT-'].update(values['xx']) 

window.close() 
    
