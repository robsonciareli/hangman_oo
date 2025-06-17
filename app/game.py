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
            index = 0
            for letra in self.palavra:
                if letra == tentativa:
                    self.letras_descobertas[index] = letra
                index += 1
        else:
            self.chance -= 1
            self.letras_erradas.append(tentativa)
            print(f"Letra incorreta. Tentativas restantes: {self.chance}!")

    @classmethod
    def choiceWord(self):
        return random.choice(self.lista_palavras)
    
    def getDescobertas(self):
        return ['_' for letra in self.palavra]
    
    def voceVenceu(self):
        print(f"Parabéns, você venceu, a palavra é {self.palavra}!")
    
    def vocePerdeu(self):
        print(f"Você perdeu a palavra é {self.palavra}")
