import time, pyautogui, logging

class Modulo:
    def clique(id, qtd_cliques):
        tentativa = 0
        try:
            while tentativa < 10:
                if pyautogui.click(id, clicks=qtd_cliques):
                    logging.info('Clicando no botão '+ id +' encontrado.')
                    break
                else:
                    time.sleep(1)
                    tentativa += 1
        except:
            logging.error('Não conseguiu localizar o: '+ id)
    
    def escrever(texto):
        tentativa = 0
        try:
            while tentativa < 10:
                try:
                    pyautogui.write(texto)
                    break
                except:
                    time.sleep(1)
                    tentativa += 1
                    print('Não digitou '+ texto)
        except:
            logging.error('Não foi possivel digitar: '+ texto)

    def clicar_imagem(imagem, qtd_cliques):
        tentativa = 0
        try:
            while tentativa < 10:
                if pyautogui.locateCenterOnScreen(imagem, confidence=0.9):
                    logging.info('Figura '+ imagem +' encontrada')
                    clique_imagem = pyautogui.locateCenterOnScreen(imagem)
                    pyautogui.click(clique_imagem, clicks=qtd_cliques)
                    break
                else:
                    time.sleep(1)
                    tentativa += 1
        except:
            logging.error('Não encontrou a figura '+ imagem)