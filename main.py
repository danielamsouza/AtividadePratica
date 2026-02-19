import pygame
from asset.constantes import LARGURA, ALTURA

#inicia a biblioteca
pygame.init()

#configura a resolução da tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space Shooter Demo")

#variavel de controle
rodando = True

#loop do jogo
while rodando:

#verifica os eventos do sistema
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

#preenche a tela com uma cor para apagar o frame anterior
    tela.fill("black")

#atualiza o display
    pygame.display.flip()

#encerra a biblioteca quando sair do loop
pygame.quit()