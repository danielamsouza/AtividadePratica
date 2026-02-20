import pygame
import os

class Jogador: #definindo a Classe que vai criar os objetos da nave
    def __init__(self, largura_tela, altura_tela): #contrutor que recebe o tamanho da tela
        self.largura_tela = largura_tela #salva a largura da tela dentro do objeto

        #os.path.join une os nomes das pastas
        caminho_imagem = os.path.join("asset", "kenney_space-shooter-redux","PNG", "playerShip1_blue.png")

        #carrega a imagem da nave e o convert.alpha() processa a transparência
        self.image = pygame.image.load(caminho_imagem).convert_alpha()

        #extrai um retângulo invisível (rect) do tamanho exato da imagem (posição e colisão)
        self.rect = self.image.get_rect()

        #pega a coordenada x do centro do retângulo da nave e alinha com o centro da tela
        self.rect.centerx = largura_tela // 2

        #pega a borda inferior do retângulo (bottom) e posiciona 20px acima do final da tela
        self.rect.bottom = altura_tela - 20

    def desenhar(self, surface): #metodo para exibir a nave

        #blit é o comando que insere a self.image na surface usando as coordenadas atuais do self.rect
        surface.blit(self.image, self.rect)
