import pygame
import os

class Laser:
    def __init__(self, x, y):
        #caminho da imagem
        caminho_imagem = os.path.join("asset", "kenney_space-shooter-redux", "PNG", "Lasers", "laserRed01.png")
        #carrega a imagem e processa a transparencia
        self.image = pygame.image.load(caminho_imagem).convert_alpha()

         #cria o retangulo de colisão
        self.rect = self.image.get_rect()

        #centraliza o tiro no x que foi recebido
        self.rect.centerx = x
        #alinha a base do tiro com o y recebido
        self.rect.bottom = y

        #define a velocidade do tiro
        self.velocidade = 15

    def update(self):
        #o eixo Y diminui conforme subimos na tela, então subtraimos a velocidade para o tiro subir
        self.rect.y -= self.velocidade

    def desenhar(self, surface):
        #desenha a imagem do laser na tela usando as coordenadas atuais
        surface.blit(self.image, self.rect)