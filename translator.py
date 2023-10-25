import ttkbootstrap as ttk
from googletrans import Translator

def translation():
    firstLan = oneVar.get()
    secondLan = twoVar.get()
    
    textTwo.delete("1.0","end-1c")
    toTranslate = textOne.get("1.0","end-1c")
    
    translator = Translator()
    translated = translator.translate(toTranslate, src=firstLan, dest=secondLan)
    
    textTwo.insert("end-1c", translated.text)


window = ttk.Window()
window.title("TranslatorApp")
window.geometry('640x275')

textOne = ttk.Text(window, font='Roboto 12')
textTwo = ttk.Text(window, font='Roboto 12')

oneVar = ttk.StringVar(value='pl')
optionsOne = ttk.Combobox(window, textvariable=oneVar, font='roboto 10')
optionsOne.place(x=20, y=170, width=300)
optionsOne['values'] = ['pl', 'en']

twoVar = ttk.StringVar(value='en')
optionsTwo = ttk.Combobox(window, textvariable=twoVar, font='roboto 10')
optionsTwo.place(x=320, y=170, width=300)
optionsTwo['values'] = ['pl', 'en']

button = ttk.Button(text='Translate', command=translation)
button.place(x=20, y=220, width=600)


textOne.place(x=20,y=20, width=300, height=150)
textTwo.place(x=320,y=20, width=300, height=150)

window.mainloop()