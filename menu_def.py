from tkinter import *
from tkinter import ttk

import main_users_def
import main_alunos
import janela_avaliacao
import janela_performance
import main_pagamentos
import gestaoaulas
import gestaocursos

# Definição de funções que limpam o content_frame (chamando a função clear_content_frame())
# e criam um rótulo com os nomes respetivos. O rótulo é adicionado ao content_frame


# Definir a aparência inicial da janela principal
root = Tk() # Cria uma instância da classe
root.title('Centro de formação') # Título da janela
root.geometry('1280x640+280+150') # Geometria da janela, especifica a largura, altura e posição inicial
root.resizable(FALSE, FALSE) # Bloquea a capacidade de alterar o tamanho em largura e altura

# Define a fonte das letras exibidas na interface
FONT = ('Arial', 12)

# Cria um frame dentro da janela raiz, define a sua altura, largura, cor de fundo
# Empacota o frame no local padrão e expande para ocupar o espaço disponível
main_frame = Frame(root, width=1280, height=720, bg='#F5F5F5')
main_frame.pack(fill='both', expand=True)

# Cria um frame dentro do main_frame, define a sua altura, largura, cor de fundo
# Empacota o frame à esquerda e preenche verticalmente o espaço disponível
menu_frame = Frame(main_frame, bg='#383838', width=200, height=720)
menu_frame.pack(side='left', fill='y')

# Cria um frame dentro do content_frame, define a sua altura, largura, cor de fundo
# Empacota o frame à esquerda e expande para ocupar o espaço disponível
content_frame = Frame(main_frame, bg='white', width=1080, height=720)
content_frame.pack(side='left', fill='both', expand=True)

# Define um dictionary para o estilo dos botões
button_styles = {
    'bg': '#008080',
    'fg': 'white',
    'activebackground': '#4C4C4C',
    'activeforeground': 'white',
    'font': FONT,
    'borderwidth': 0,
    'highlightthickness': 0,
    'relief': 'flat',
    'cursor': 'hand2',
}

# Define vários botões a partir do dicionário button_styles
# Empacota-os com preenchimento vertical (pady=10) preenchimento horizontal (padx=20) e preenchimento horizontal completo (fill='x').

# O primeiro botão (button1) em particular Define a função main_users_def.criar_interface(content_frame)
# como o comando a ser executado quando o botão é clicado.
button1 = Button(menu_frame, text='Gestão de Utilizadores', **button_styles, command=lambda: main_users_def.criar_interface(content_frame))
button1.pack(pady=10, padx=20, fill='x')

button2 = Button(menu_frame, text='Gestão de Alunos', **button_styles, command=lambda: main_alunos.gestao_alunos(content_frame))
button2.pack(pady=10, padx=20, fill='x')

button3 = Button(menu_frame, text='Gestão de Cursos', **button_styles, command=lambda: gestaocursos.gestao_cursos(content_frame))
button3.pack(pady=10, padx=20, fill='x')

button4 = Button(menu_frame, text='Gestão de Aulas e Horários', **button_styles, command=lambda: gestaoaulas.gestao_aulas(content_frame))
button4.pack(pady=10, padx=20, fill='x')

button5 = Button(menu_frame, text='Gestão de Pagamentos', **button_styles, command=lambda: main_pagamentos.show_gestao_pagamentos(content_frame))
button5.pack(pady=10, padx=20, fill='x')

button6 = Button(menu_frame, text='Avaliações de Alunos', **button_styles, command=lambda: janela_avaliacao.gestao_avaliacoes(content_frame))
button6.pack(pady=10, padx=20, fill='x')

button7 = Button(menu_frame, text='Performance de Alunos', **button_styles, command=lambda: janela_performance.gestao_performance(content_frame))
button7.pack(pady=10, padx=20, fill='x')

white_space = Label(content_frame)
white_space.pack(pady=100)

titulo = Label(content_frame, text='BEM VINDO \n AO \n CENTRO DE FORMAÇÃO', font='Arial 18')
titulo.pack(anchor='center')

# Inicia a loop do programa e exibe a janela
root.mainloop()