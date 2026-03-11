import pygame
import os
import random
import sre_constants

class Inimigo:
    def __init__(self, altura_tela, largura_tela ):
        self.altura_tela = altura_tela
        self.largura_tela = largura_tela

        #define o caminho da imagem
        caminho_imagem = os.path.join("asset", "kenney_space-shooter-redux", "PNG", "Meteors", "meteorBrown_med1.png")

        #carrega a imagem e processa a transparencia
        self.image = pygame.image.load(caminho_imagem).convert_alpha()

        #cria o retangulo de colisao
        self.rect = self.image.get_rect()

        #sorteamos uma posição x entre 0 e o limite direto da tela
        self.rect.x = random.randint(0, largura_tela - self.rect.width)

        #posiciona a base do meteoro no y = 0
        self.rect.bottom = 0

        #sorteia a velocidade de queda entre 2 e 6 fps
        self.velocidade = random.randint(2, 6)

    #funçao para atualizar a fisica do inimigo
    def update(self):
        self.rect.y += self.velocidade

    #funçao para exibir o inimigo na tela
    def desenhar(self, surface):
        surface.blit(self.image, self.rect)