from app.tela import Tela
import random
import unidecode

class Game():
    lista_palavras = ['abacate', 'banana', 'abacaxi', 'pera', 'tangerina', 'caqui', 'manga', 'melancia', 'kiwi', 'romã']

    def __init__(self):
        self.chance = 6
        self.palavra = self.escolherPalavra()
        self.letras_descobertas = self.pegarDescobertas()
        self.letras_erradas = []
        self.jogar()


    def jogar(self):
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
        self.prepararRodada()

        tentativa = self.pegarTentativa()

        if unidecode.unidecode(tentativa) in unidecode.unidecode(self.palavra):
            self.setarDescoberta(tentativa)
        else:
            self.reduzirChance()
            self.setarLetrasErradas(tentativa)

    def prepararRodada(self):
        print("".join(self.letras_descobertas))
        print(f"\nChances restantes: {self.chance}")
        print(f"Letras erradas: ", " ".join(self.letras_erradas))
        self.forca()

    @classmethod
    def escolherPalavra(self):
        return random.choice(self.lista_palavras)
    
    def reduzirChance(self):
        self.chance -= 1
    
    def pegarDescobertas(self):
        return ['_' for letra in self.palavra]
    
    def setarDescoberta(self, tentativa):
        index = 0
        for letra in self.palavra:
            if unidecode.unidecode(letra) == unidecode.unidecode(tentativa):
                self.letras_descobertas[index] = letra
            index += 1

    def setarLetrasErradas(self, tentativa):
        self.letras_erradas.append(tentativa)
        print(f"Letra incorreta. Tentativas restantes: {self.chance}!")
    
    def voceVenceu(self):
        Tela.limpar()
        print(f"Parabéns, você venceu!\nA palavra é {self.palavra.upper()}")
    
    def vocePerdeu(self):
        Tela.limpar()
        self.forca()
        print(f"Você perdeu!\nA palavra é {self.palavra.upper()}")

    def pegarTentativa(self):
        while True:
            tentativa = input("\nDigite uma letra: ").lower()
            if len(self.letras_erradas) == 0:
                break
            elif not (unidecode.unidecode(tentativa) in [unidecode.unidecode(l) for l in self.letras_erradas]):
                break
            else:
                print(f"\nA letra \"{tentativa}\" já foi digitada!\n")
        return tentativa

    def forca(self):
        if self.chance == 6:
            print("_________")
            print("||      |")
            print("||")
            print("||")
            print("||")
            print("||")
            print("||________")
            print("||      ||")
        elif self.chance == 5:
            print("_________")
            print("||      |")
            print("||      O")
            print("||")
            print("||")
            print("||")
            print("||________")
            print("||      ||")
        elif self.chance == 4:
            print("_________")
            print("||      |")
            print("||     \\O")
            print("||")
            print("||")
            print("||")
            print("||________")
            print("||      ||")
        elif self.chance == 3:
            print("_________")
            print("||      |")
            print("||     \\O/")
            print("||")
            print("||")
            print("||")
            print("||________")
            print("||      ||")
        elif self.chance == 2:
            print("_________")
            print("||      |")
            print("||     \\O/")
            print("||      |")
            print("||")
            print("||")
            print("||________")
            print("||      ||")
        elif self.chance == 1:
            print("_________")
            print("||      |")
            print("||     \\O/")
            print("||      |")
            print("||     / ")
            print("||")
            print("||________")
            print("||      ||")
        elif self.chance == 0:
            print("_________")
            print("||      |")
            print("||     \\O/")
            print("||      |")
            print("||     / \\")
            print("||")
            print("||________")
            print("||      ||")

