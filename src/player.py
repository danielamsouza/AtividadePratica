import pygame
import os
from src.laser import Laser

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

        #velocidade de movimento da nave
        self.velocidade = 15

        #cria uma lista vazia para armazenar os tiros
        self.lasers = []
        #trava do gatilho
        self.pode_atirar = True
        self.tempo_utlimo_disparo = 0
        #tempo de recarga entre os tiros (em ms)
        self.cooldown = 150

    def update(self):
        #key.get(pressed) captura as teclas pressionadas
        teclas_pressionadas = pygame.key.get_pressed()

        #verificando as teclas pressionadas
        if teclas_pressionadas[pygame.K_a]:
            self.rect.x -= self.velocidade
        if teclas_pressionadas[pygame.K_d]:
            self.rect.x += self.velocidade

        #impedidno que a nave saia da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.largura_tela:
            self.rect.right = self.largura_tela

        #verifica se o jogador apertou espaço e a situação da trava
        if teclas_pressionadas[pygame.K_SPACE] and self.pode_atirar:
            self.atirar()
        self.recarregar()

        for laser in self.lasers:
            laser.update()

            # Se a base do laser passar do topo da tela (y <= 0), removemos ele da lista
            if laser.rect.bottom <= 0:
                self.lasers.remove(laser)

    def atirar(self):
        novo_tiro = Laser(self.rect.centerx, self.rect.top)
        #adiciona esse tiro a lista
        self.lasers.append(novo_tiro)
        #trava o gatilho
        self.pode_atirar = False
        #regista o tempo atual do disparo
        self.tempo_utlimo_disparo = pygame.time.get_ticks()

    def recarregar(self):
        if not self.pode_atirar:
            tempo_atual = pygame.time.get_ticks()

            if tempo_atual - self.tempo_utlimo_disparo >= self.cooldown:
                self.pode_atirar = True

    def desenhar(self, surface): #metodo para exibir a nave

        #blit é o comando que insere a self.image na surface usando as coordenadas atuais do self.rect
        surface.blit(self.image, self.rect)

        for laser in self.lasers:
            laser.desenhar(surface)
