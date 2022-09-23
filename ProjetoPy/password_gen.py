from operator import truediv
import random
import PySimpleGUI as sg
import tkinter as tk
import os

#from macpath import join

class PassGen:
    def __init__(self):
        sg.theme("Black")

        layout = [
            [sg.Text("Site | Programa", size=(20, 1)),
            sg.Input(key='site', size=(20, 1))],

            [sg.Text("Email | Usuario", size=(20, 1)),
            sg.Input(key=('usuario'), size=(20,1))],

            [sg.Text("Quantidade de caracteres"), sg.Combo(values=list(range(1, 31)), key="total_carac", default_value = 1, size=(10, 1))],
            [sg.Output(size=(40,8))],
            [sg.Button("Gerar Senha")]
        ]
        
        # Declarando janela
        self.janela = sg.Window("Gerador de Senha", layout)

    def iniciar(self):
        while(True):
            event, valores = self.janela.read()
            if event == sg.WIN_CLOSED:
                break
            if event == "Gerar Senha":
                nova_senha  = self.gerarSenha(valores)
                print(nova_senha)
                self.salvarSenha(nova_senha, valores)

    def gerarSenha(self, valores):
        lista_carac = "abcdedfghijklmnopqrstuvxwyzABCDEDFGHIJKLMNOPQRSTUVXWYZ!@#$%*()1234567890"
        teste = random.choices(lista_carac,k=int(valores["total_carac"]))
        new_pass = "".join(teste)
        return new_pass

    def salvarSenha(self, nova_senha, valores):
        with open("senhas.txt", 'a', newline='') as arquivo:
            arquivo.write(f" Site: {valores['site']} \n Usuario: {valores['usuario']}\n Nova senha: {nova_senha}")
        
        print("Senha salva com sucesso !!")

gen = PassGen()
gen.iniciar()
