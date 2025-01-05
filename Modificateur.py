from tkinter import filedialog 
from tkinter import *
from tkinter.messagebox import *

fichier_originale = filedialog.askopenfilename(title="Select File") 
fichier_modifier = filedialog.asksaveasfilename()


fenetre = Tk()
fenetre.title('Choose the element to replace and by what ?')
fenetre.resizable(False, False)
fenetre.geometry('430x150')
fenetre.config(background='#1466b8')

ancient = StringVar()
nouveau = StringVar()

def remplacer(ancien,nouveau):
    with open(fichier_originale, 'r', encoding='utf-8') as infile, open(fichier_modifier, 'w', encoding='utf-8') as outfile:
        for line in infile:
            no_space_line = line.replace(ancien,nouveau)
            outfile.write(no_space_line)
    showinfo('Modifier:', f'Votre fichier : {fichier_originale} a bien été modifier en {fichier_modifier}')
    fenetre.destroy()

p = PanedWindow(fenetre, orient=VERTICAL,bg = "#1466b8")
p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
p.add(Label(p, bg='#1466b8', fg = '#FFFFFF' ,text="Entrez l'ancien élément que vous voulez remplacer : ",  anchor=CENTER))
EntreeAncient = Entry(fenetre, textvariable=ancient, validate="key", width=4)
p.add(EntreeAncient)
p.add(Label(p, bg='#1466b8', fg = '#FFFFFF', text="Entrez le nouvelle élément  : ",  anchor=CENTER))
EntreeNouveau = Entry(fenetre, textvariable=nouveau, validate="key", width=4)
p.add(EntreeNouveau)
p.add(Button(fenetre, bg='#1466b8', fg = '#FFFFFF', text="Modifier", command=lambda: remplacer(EntreeAncient.get(), EntreeNouveau.get())))
fenetre.mainloop()




