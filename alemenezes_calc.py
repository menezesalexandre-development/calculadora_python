# BIBLIOTECAS:
from time import sleep
from tkinter import *
from tkinter import ttk

# CORES:
preto = '#000'
branco = '#fff'
azul1 = '#0f2fff'
azul_escuro1 = '#030912'
laranja1 = '#ff7105'

janela = Tk()
janela.title('Alemenezes Calc')
janela.geometry('265x305')
janela.config(bg=azul_escuro1)
janela.resizable(width=False, height=False)
janela.iconbitmap('media/calc_icon.ico')

# FRAMES:
visor = Frame(janela, width=300, height=50, bg=azul_escuro1)
visor.grid(row=0, column=0)

principal = Frame(janela, width=300, height=268, bg=azul_escuro1)
principal.grid(row=1, column=0)

# TODOS OS VALORES:
expressao = ''
entrada_nova = ''
memoria_temporaria = 0
simbolo_event = False

# LABEL:
labelTexto = StringVar()


# FUNÇÃO DA CALCULADORA:
def entrar_valor(event):
    global memoria_temporaria
    global simbolo_event
    global expressao

    ultimo_caractere = len(expressao) - 1

    if event == '+' or event == '-' or event == '*' or event == '/':
        simbolo_event = True
    else:
        simbolo_event = False

    if len(expressao) == 0 and memoria_temporaria == 0 and simbolo_event == True:
        expressao = ''
    elif memoria_temporaria >= 0.1 >= len(expressao) and simbolo_event == True:
        expressao = expressao + str(memoria_temporaria) + str(event)
    else:
        expressao = expressao + str(event)

    labelTexto.set(expressao)


# FUNÇÃO PARA CALCULAR:
def calcular():
    global expressao

    calculado = eval(expressao)
    if calculado // 1 == calculado:
        calculado = int(calculado)
    expressao = '' + str(calculado)
    print(calculado)

    global memoria_temporaria
    memoria_temporaria = calculado
    labelTexto.set(calculado)
    sleep(0.1)
    expressao = ''


# FUNÇÃO PARA LIMPAR VISOR:
def limpar_visor():
    global memoria_temporaria
    global expressao

    expressao = ''
    memoria_temporaria = 0
    labelTexto.set('')


# LABEL:
appLabel = Label(visor, textvariable=labelTexto, width=18, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT,
                 font='helvetica 18', bg=azul_escuro1, fg=branco)
appLabel.place(x=0, y=0)

# BOTÕES:
botaoClear = Button(principal, command=limpar_visor, text='C', width=22, height=2, font='Helvetica', relief=RAISED,
                    overrelief=RIDGE)
botaoClear.place(x=0, y=0)

botaoDivisao = Button(principal, command=lambda: entrar_valor('/'), text='/', width=5, height=2, font='Helvetica',
                      bg=laranja1, fg=branco, relief=RAISED,
                      overrelief=RIDGE)
botaoDivisao.place(x=209, y=0)

botaoMultiplicacao = Button(principal, command=lambda: entrar_valor('*'), text='*', width=5, height=2, font='Helvetica',
                            bg=laranja1, fg=branco,
                            relief=RAISED, overrelief=RIDGE)
botaoMultiplicacao.place(x=209, y=51)

botaoSubtracao = Button(principal, command=lambda: entrar_valor('-'), text='-', width=5, height=2, font='Helvetica',
                        bg=laranja1, fg=branco, relief=RAISED,
                        overrelief=RIDGE)
botaoSubtracao.place(x=209, y=102)

botaoSoma = Button(principal, command=lambda: entrar_valor('+'), text='+', width=5, height=2, font='Helvetica',
                   bg=laranja1, fg=branco, relief=RAISED,
                   overrelief=RIDGE)
botaoSoma.place(x=209, y=153)

botaoIgual = Button(principal, command=calcular, text='=', width=5, height=2, font='Helvetica', bg=azul1, fg=branco,
                    relief=RAISED,
                    overrelief=RIDGE)
botaoIgual.place(x=209, y=204)

botaoSete = Button(principal, command=lambda: entrar_valor('7'), text='7', width=6, height=2, font='Helvetica',
                   relief=RAISED, overrelief=RIDGE)
botaoSete.place(x=0, y=51)

botaoOito = Button(principal, command=lambda: entrar_valor('8'), text='8', width=6, height=2, font='Helvetica',
                   relief=RAISED, overrelief=RIDGE)
botaoOito.place(x=71, y=51)

botaoNove = Button(principal, command=lambda: entrar_valor('9'), text='9', width=6, height=2, font='Helvetica',
                   relief=RAISED, overrelief=RIDGE)
botaoNove.place(x=141, y=51)

botaoQuatro = Button(principal, command=lambda: entrar_valor('4'), text='4', width=6, height=2, font='Helvetica',
                     relief=RAISED, overrelief=RIDGE)
botaoQuatro.place(x=0, y=102)

botaoCinco = Button(principal, command=lambda: entrar_valor('5'), text='5', width=6, height=2, font='Helvetica',
                    relief=RAISED, overrelief=RIDGE)
botaoCinco.place(x=71, y=102)

botaoSeis = Button(principal, command=lambda: entrar_valor('6'), text='6', width=6, height=2, font='Helvetica',
                   relief=RAISED, overrelief=RIDGE)
botaoSeis.place(x=141, y=102)

botaoUm = Button(principal, command=lambda: entrar_valor('1'), text='1', width=6, height=2, font='Helvetica',
                 relief=RAISED, overrelief=RIDGE)
botaoUm.place(x=0, y=153)

botaoDois = Button(principal, command=lambda: entrar_valor('2'), text='2', width=6, height=2, font='Helvetica',
                   relief=RAISED, overrelief=RIDGE)
botaoDois.place(x=71, y=153)

botaoTres = Button(principal, command=lambda: entrar_valor('3'), text='3', width=6, height=2, font='Helvetica',
                   relief=RAISED, overrelief=RIDGE)
botaoTres.place(x=141, y=153)

botaoZero = Button(principal, command=lambda: entrar_valor('0'), text='0', width=14, height=2, font='Helvetica',
                   relief=RAISED, overrelief=RIDGE)
botaoZero.place(x=0, y=204)

botaoPonto = Button(principal, command=lambda: entrar_valor('.'), text='•', width=6, height=2, font='Helvetica',
                    relief=RAISED, overrelief=RIDGE)
botaoPonto.place(x=141, y=204)

janela.mainloop()
