from tkinter import *

# Main
window = Tk();
window.title('Glossário de Ciência da Computação')
window.configure(background='black')

# Função de saída
def close_window():
    window.destroy()
    exit()

# Função keydown
def click():
    entered_text = textentry.get().lower() # Irá coletar o texto da caixa de entrada de textos
    output.delete(0.0, END)
    try:
        definition = comp_dict[entered_text]
    except:
        definition = 'desculpe, não temos essa palavra'
    output.insert(END, definition)

# Foto
photo = PhotoImage(file='comp.png')
Label(window, image=photo, bg='black').grid(row=0, column=0, sticky=W)

# Criar label
Label(window, text="Entre a palavra que você deseja uma definição", bg='black', fg='white', font='none 12 bold').grid(row=1, column=0, sticky=W)

# Criar uma caixa de entrada de textos
textentry = Entry(window, width=20, bg='white')
textentry.grid(row=2, column=0, sticky=W)

# Adicionar um botão de submissão
Button(window, text='Enviar', width=6, command=click).grid(row=3, column=0, sticky=W)

# Criar outra label
Label(window, text='\nDefinição:', bg='black', fg='white', font='none 12 bold').grid(row=4, column=0, stick=W)

# Criar uma caixa de texto
output = Text(window, width=75, height=6, wrap=WORD, background='white')
output.grid(row=5, column=0, columnspan=2, sticky=W)

# Dicionário de termos computacionais
comp_dict = {
	'algorithm': 'step by step instructions to complete a task',
	'bug': 'pedaço de código que causa um programa a falhar'
}

# Label de saída
Label(window, text='clique para sair', bg='black', fg='white', font='none 12 bold').grid(row=6, column=0, sticky=W)

# Botão de saída
Button(window, text='Exit', width=14, command=close_window).grid(row=7, column=0, sticky=W)

# Roda o loop principal
window.mainloop()