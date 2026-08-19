import os

def cls(): #Função serve para dar clear na tela, ela checa se o sistema operacional é Windows ou Linux/MacOS
    os.system('cls' if os.name=='nt' else 'clear')