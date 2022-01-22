import time, os, pyautogui
from log import *
from Modulo import Modulo
from pywinauto import application

class Sankhya:
    def __init__(self):
        self.diretorio = r'C:\Sankhya\Sankhya'
        self.executavel_sankhya = "NavegadorSankhya.exe"
        self.dir_imagens = r'C:\RPA\sankhya-processamento-retorno-python\Imagens'
        self.usuario = 'DIGITE AQUI O USUÁRIO'
        self.senha = 'DIGITE AQUI A SENHA'

    def abrir(self):
        os.chdir(self.diretorio)
        try:
            navegador = application.Application().start(self.executavel_sankhya)
            pyautogui.getActiveWindow(navegador)
            time.sleep(5)
            return navegador
        except Exception as e:
            logging.error(e) 
      
    def login(self):
        os.chdir(self.dir_imagens)
        try:
            Modulo.clicar_imagem('usuario.png', 2)
            Modulo.clicar_imagem('senha.png', 2)
            Modulo.escrever(self.senha)
            Modulo.clicar_imagem('entrar.png', 1)
            Modulo.clicar_imagem('processamento.png', 1)
        except Exception as e:
            logging.error(e)
            print(pyautogui.position())

    def fechar(self, navegador):
        sair = pyautogui.move(x=1342, y=75)
        Modulo.clique_duplo(sair)
        try:
            if pyautogui.locateCenterOnScreen('sair.png', confidence = 0.9) != None:
                button_sair = pyautogui.locateCenterOnScreen('sair.png')
                pyautogui.click(button_sair)
                navegador.kill()
            else:
                print('Não encontrou o botão sair')
        except Exception as e:
            logging.error(e)