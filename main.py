import pygame
from asset.constantes import LARGURA, ALTURA
from src.player import Jogador

#inicia a biblioteca
pygame.init()

#configura a resolução da tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space Shooter Demo")

#criação do relógio de tempo de jogo
relogio = pygame.time.Clock()

nave = Jogador(LARGURA, ALTURA) #instancia o objeto nave

#variavel de controle
rodando = True

#loop do jogo
while rodando:
    #limita o fps a 60
    relogio.tick(60)

    #verifica os eventos do sistema
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #verifica se o evento é clique no X
            rodando = False #se clicou no X, muda a variável para False

    #atualiza a lógica do jogo
    nave.update()

    #preenche a tela com uma cor para apagar o frame anterior
    tela.fill("black")
    #executa o metodo da classe, mandando ela se desenhar na variavel tela
    nave.desenhar(tela)
    #atualiza o display com o processamento de video feito no loop
    pygame.display.flip()

#encerra a biblioteca quando sair do loop
pygame.quit()