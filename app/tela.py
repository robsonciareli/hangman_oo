from os import system, name

class Tela():

    def limpar():
        system('cls') if name == 'nt' else system('clear')
