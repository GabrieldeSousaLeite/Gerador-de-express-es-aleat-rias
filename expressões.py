import random
import tkinter as tk


def criar_expressão():
    def meio_expressão():
        global expressão
        if quantidade_separadores == 1:
            expressão += '( '
            for index, numero_ in enumerate(numeros[numero_por_seção+1:numero_por_seção*2]):
                if index + 2 == numero_por_seção:
                    expressão += str(numero_) + ' '
                else: expressão += str(numero_) + ' ' + random.choice(operadores) + ' '
            expressão += ')'

        elif quantidade_separadores == 2:
            if random.choice(antes_ou_depois):
                expressão += '[ '
                for numero_ in numeros[numero_por_seção+1:numero_por_seção*2]:
                    expressão += str(numero_) + ' ' + random.choice(operadores) + ' '
                expressão += '( '
                for index, numero_ in enumerate(numeros[numero_por_seção*2+1:numero_por_seção*3]):
                    if index + 2 == numero_por_seção:
                        expressão += str(numero_) + ' '
                    else: expressão += str(numero_) + ' ' + random.choice(operadores) + ' '
                expressão += ') ] '
            
            else:
                expressão += '[ ( '
                for numero_ in numeros[numero_por_seção+1:numero_por_seção*2]:
                    expressão += str(numero_) + ' ' + random.choice(operadores) + ' '
                expressão = expressão[:-2]
                expressão += ' ) '
                for numero_ in numeros[numero_por_seção*2+1:numero_por_seção*3]:
                    expressão += random.choice(operadores) + ' ' + str(numero_) + ' '
                expressão += ']'

        elif quantidade_separadores == 3:
            if random.choice(antes_ou_depois):
                expressão += '{ '
                for numero_ in numeros[numero_por_seção+1:numero_por_seção*2]:
                    expressão += str(numero_) + ' ' + random.choice(operadores) + ' '
                expressão += '[ '
                for numero_ in numeros[numero_por_seção*2+1:numero_por_seção*3]:
                    expressão += str(numero_) + ' ' + random.choice(operadores) + ' '
                expressão += '( '
                for index, numero_ in enumerate(numeros[numero_por_seção*3+1:numero_por_seção*4]):
                    if index + 2 == numero_por_seção:
                        expressão += str(numero_) + ' '
                    else: expressão += str(numero_) + ' ' + random.choice(operadores) + ' '
                expressão += ') ] }'
            
            else:
                expressão += '{ [ ( '
                for numero_ in numeros[numero_por_seção+1:numero_por_seção*2]:
                    expressão += str(numero_) + ' ' + random.choice(operadores) + ' '
                expressão = expressão[:-2]
                expressão += ') '
                for numero_ in numeros[numero_por_seção*2+1:numero_por_seção*3]:
                    expressão += random.choice(operadores) + ' ' + str(numero_) + ' '
                expressão += '] '
                for numero_ in numeros[numero_por_seção*3+1:numero_por_seção*4]:
                    expressão += random.choice(operadores) + ' ' + str(numero_) + ' '
                expressão += '}'

    global resultado
    global expressão

    expre.tag_configure("center", justify='center')
    resposta.tag_configure("center", justify='center')

    expressão = ''
    expre.delete('1.0', 'end')
    quantidade_numeros = random.randint(12, 12)
    quantidade_separadores = random.randint(0, 3)
    numeros = [random.randint(1, 9) for i in range(quantidade_numeros)]
    numero_por_seção = int(quantidade_numeros/(quantidade_separadores + 1))
    primeiro_depois = random.choice(antes_ou_depois)

    if primeiro_depois:
        for index, numero_ in enumerate(numeros[:numero_por_seção]):
            if index + 1 == numero_por_seção and quantidade_separadores == 0:
                expressão += str(numero_) + ' '
            else: expressão += str(numero_) + ' ' + random.choice(operadores) + ' '

        if quantidade_separadores > 0:
            meio_expressão()
    
    elif quantidade_separadores > 0:
        meio_expressão()

        for index, numero_ in enumerate(numeros[:numero_por_seção]):
            expressão += ' ' + random.choice(operadores) + ' ' + str(numero_)
    
    else: expressão = '1/2'

    try:
        resultado = eval(expressão.replace('[', '(').replace(']', ')').replace('}', ')').replace('{', '('))
    except: resultado = 1.3

    if not isinstance(resultado, float):
        expre.insert(tk.END, expressão, "center")
    else:
        criar_expressão()


def inserir_resposta():
    resposta.delete('1.0', 'end')
    resposta.insert(tk.END, resultado, "center")


operadores = ['+', '-', '*', '/']
antes_ou_depois = [True, False]

janela = tk.Tk()
janela.geometry('400x137')
janela.configure(bg='dark gray')

gerar = tk.Button(text='Gerar expressão aleatória', bg='gray', font=('Arial', 12), command=criar_expressão)
gerar.pack(padx=6, pady=6)

expre = tk.Text(height=1, bg='gray', font=('Arial', 12))
expre.pack(padx=6)

mostrar = tk.Button(text='Mostrar resposta', bg='gray', font=('Arial', 12), command=inserir_resposta)
mostrar.pack(padx=6, pady=6)

resposta = tk.Text(height=1, bg='gray', font=('Arial', 12))
resposta.pack(padx=6)

janela.mainloop()