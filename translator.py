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

def switchLan():
    firstLan = oneVar.get()
    secondLan = twoVar.get()
    
    oneVar.set(secondLan)
    twoVar.set(firstLan)

window = ttk.Window()
window.title("TranslatorApp")
window.geometry('640x275')

icon = ttk.PhotoImage(file='icon.png')
window.iconphoto(0,icon)

textOne = ttk.Text(window, font='Roboto 12')
textTwo = ttk.Text(window, font='Roboto 12')

oneVar = ttk.StringVar(value='pl')
optionsOne = ttk.Combobox(window, textvariable=oneVar, font='roboto 10')
optionsOne.place(x=20, y=170, width=255)
optionsOne['values'] = ['pl', 'en', 'fr' ,'ru', 'es']

twoVar = ttk.StringVar(value='en')
optionsTwo = ttk.Combobox(window, textvariable=twoVar, font='roboto 10')
optionsTwo.place(x=320, y=170, width=300)
optionsTwo['values'] = ['pl', 'en', 'fr', 'ru' ,'es']

switchIcon = ttk.PhotoImage(file='switch.png')
switch = ttk.Button(window, image=switchIcon, bootstyle="outline", command=switchLan)
switch.place(x=275, y=170, width=45, height=32)

button = ttk.Button(bootstyle="outline",text='Translate', command=translation)
button.place(x=20, y=220, width=600)

textOne.place(x=20,y=20, width=300, height=150)
textTwo.place(x=320,y=20, width=300, height=150)    

window.mainloop()
