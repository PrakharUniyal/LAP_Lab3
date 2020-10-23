import PySimpleGUI as sg 
import nltk
import os.path
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def processfile(textfile):
    try:
        f = open(textfile, encoding="utf8")
        ftext = f.read()
        f.close()

        # Calculate number of lines
        no_of_lines = str(len(ftext.split('\n')))
    
        # Calculate number of sentences
        sentence_tokens = nltk.sent_tokenize(ftext)
        no_of_sentences = str(len(sentence_tokens))

        # Calculate number of words
        word_tokens = nltk.word_tokenize(ftext)
        punctuation_removed_word_tokens = [token for token in word_tokens if token.isalnum()]
        no_of_words = str(len(punctuation_removed_word_tokens))

        # Calculating most and least frequent words (excluding common words)
        lemma = nltk.WordNetLemmatizer()
        lemmatized_words = [lemma.lemmatize(token.lower()) for token in punctuation_removed_word_tokens]
        
        stop_words = set(nltk.corpus.stopwords.words('english'))
        relevant_words = [word for word in lemmatized_words if word not in stop_words and len(word)>2]

        freq_dist = nltk.FreqDist(relevant_words)
        freq_map = dict(freq_dist)

        sorted_freq_map = sorted(freq_map.items(), key = lambda elem: elem[1], reverse = True)
        most_freq = sorted_freq_map[0][0]
        least_freq = sorted_freq_map[-1][0]

        # Print stats
        answer = "No. of words: " + no_of_words +'\nNo. of sentences: ' + no_of_sentences + "\nNo. of newlines: " + no_of_lines + "\nMost frequent word: " + most_freq + "\nLeast frequent word: " + least_freq
        window['-FILE CONTENT-'].update(value = answer)
        
        # Plotting the frequency of 20 most frequent words
        f=[[x,y] for x,y in sorted_freq_map][:20]
        plt.clf()
        plt.bar([x[0] for x in f],[x[1] for x in f])
        plt.xticks(rotation=45)

    except FileNotFoundError:
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


window = sg.Window('Introduction_LAP_LAB3', layout)  


layout2 = [
    [sg.Text("Plot between words and frequency")],
    [sg.Canvas(key="-CANVAS-")],
]     

window2 = sg.Window(
    "Matplotlib Single Graph",
    layout2,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
)    

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


while True: 
    event, values = window.read() 
    #print(event, values) 
    
    if event in (None, 'Exit'): 
        break
    
    if event == 'Stats': 
        #plt.plot([0.1, 0.2, 0.5, 0.7])
        processfile(values['-FOLDER-'])
        fig=plt.gcf()
        fig_photo = draw_figure(window2['-CANVAS-'].TKCanvas, fig)
        
    

    if event == 'Refresh': 
        window2.close()
        layout2 = [
                        [sg.Text("Plot between words and frequency")],
                        [sg.Canvas(key="-CANVAS-")],
                      ]
        window2 = sg.Window(
                    "Matplotlib Single Graph",
                    layout2,
                    location=(0, 0),
                    finalize=True,
                    element_justification="center",
                    font="Helvetica 18",
                    ) 
        #plt.plot([0.1, 0.2, 0.5, 0.7])
        processfile(values['-FOLDER-'])
        fig=plt.gcf()
        fig_photo = draw_figure(window2['-CANVAS-'].TKCanvas, fig)



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
window2.close()