from app.tela import Tela
import random

class Game():
    lista_palavras = ['abacate', 'banana', 'abacaxi', 'pera', 'tangerina', 'caqui']

    def __init__(self):
        self.chance = 6
        self.palavra = self.choiceWord()
        self.letras_descobertas = self.getDescobertas()
        self.letras_erradas = []

        print("\nBem-vindo(a) ao jogo da forca!")
        print("Advinhe a palavra abaixo:\n")

        while self.chance > 0:
            self.rodada()
            if "_" not in self.letras_descobertas:
                self.voceVenceu()
                break

            if self.chance == 0:
                self.vocePerdeu()

    def rodada(self):
        print("".join(self.letras_descobertas))
        print(f"\nChances restantes: {self.chance}")
        print(f"Letras erradas: ", " ".join(self.letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in self.palavra:
            self.setDescoberta(tentativa)
        else:
            self.reduzirChance()
            self.setLetrasErradas(tentativa)

    @classmethod
    def choiceWord(self):
        return random.choice(self.lista_palavras)
    
    def reduzirChance(self):
        self.chance -= 1
    
    def getDescobertas(self):
        return ['_' for letra in self.palavra]
    
    def setDescoberta(self, tentativa):
        index = 0
        for letra in self.palavra:
            if letra == tentativa:
                self.letras_descobertas[index] = letra
            index += 1

    def setLetrasErradas(self, tentativa):
        self.letras_erradas.append(tentativa)
        print(f"Letra incorreta. Tentativas restantes: {self.chance}!")
    
    def voceVenceu(self):
        Tela.limpar()
        print(f"Parabéns, você venceu!\nA palavra é {self.palavra.upper()}")
    
    def vocePerdeu(self):
        Tela.limpar()
        print(f"Você perdeu!\nA palavra é {self.palavra.upper()}")
