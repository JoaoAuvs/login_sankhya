from log import *
from email import *
from sankhya import *

def main():
    tentativa = 0
    while 2:
        try:
            navegador = Sankhya().abrir()
            Sankhya().login()
            Sankhya().fechar(navegador)
            break
        except Exception as e:
            logging.error(e)
            navegador.kill()
            tentativa += 1 
            if tentativa == 2:
                print('Enviou email de falha')

if __name__ == '__main__':
    log = Log()
    main()
    