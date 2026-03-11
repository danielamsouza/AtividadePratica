import pygame
import os
import random
from asset.constantes import LARGURA, ALTURA
from src.player import Jogador
from src.enemy import Inimigo

#inicia a biblioteca
pygame.init()

#inicializa as fontes do pygame
pygame.font.init()
#cria um objeto de fonte
fonte_padrao = pygame.font.SysFont("Arial", 10, True)
fonte_titulo = pygame.font.SysFont("Arial", 50, True)
#variavel para armazenar o valor do score
pontuacao = 0

#configura a resolução da tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space Shooter Demo")

#criação do relógio de tempo de jogo
relogio = pygame.time.Clock()

#os.path.join cria o caminho seguro para as imagens dentro da pasta asset
caminho_fundo_menu = os.path.join("asset", "kenney_space-shooter-redux", "Backgrounds", "purple.png")
caminho_fundo_jogo = os.path.join("asset", "kenney_space-shooter-redux", "Backgrounds", "darkPurple.png")

#pygame.image.load carrega o arquivo de imagem para a memoria
#.convert() porque o fundo nao tem transparencia, economiza processamento
fundo_menu_original = pygame.image.load(caminho_fundo_menu).convert()
fundo_jogo_original = pygame.image.load(caminho_fundo_jogo).convert()

#as imagens originais sao pequenas
#o metodo pygame.transform.scale pega a imagem e estica ela para o tamanho da tela
fundo_menu = pygame.transform.scale(fundo_menu_original, (LARGURA, ALTURA))
fundo_jogo = pygame.transform.scale(fundo_jogo_original, (LARGURA, ALTURA))

#instancia o objeto nave
nave = Jogador(LARGURA, ALTURA)
#lista para armazenar os inimigos da tela
inimigos = []

#cria um evento para disparar
evento_criar_inimigo = pygame.USEREVENT + 1
#define que esse evento vai disparar a cada 1000 ms
pygame.time.set_timer(evento_criar_inimigo, 1000)

#variavel da tela de menu
tela_menu = True
#variavel de controle do jogo
rodando = True

#loop do menu
while tela_menu:
    relogio.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tela_menu = False
            rodando = False

        #verifica se alguma tecla foi pressionada
        if event.type == pygame.KEYDOWN:
            #se a tecla for enter
            if event.key == pygame.K_RETURN:
                tela_menu = False

    #blit carimba a imagem na tela
    tela.blit(fundo_menu, (0, 0))

    #o metodo render() transforma o texto em uma imagem
    #o True ativa o anti-aliasing e white define a cor como branca
    texto_titulo = fonte_titulo.render("SPACE SHOOTER", True, "white")
    texto_iniciar = fonte_padrao.render("Pressione ENTER para iniciar", True, "white")
    texto_comandos_menu = fonte_padrao.render("Comandos: [A] [D] Mover | [BARRA ESPAÇO] Atirar", True, "white")

    #blit carimba a imagem gerada na cordenada x,y
    #A matemática (LARGURA // 2 - largura_do_texto // 2) serve para centralizar o texto perfeitamente no eixo x
    tela.blit(texto_titulo, (LARGURA // 2 - texto_titulo.get_width() // 2, ALTURA // 3))
    tela.blit(texto_iniciar, (LARGURA // 2 - texto_iniciar.get_width() // 2, ALTURA // 2))
    tela.blit(texto_comandos_menu, (LARGURA // 2 - texto_comandos_menu.get_width() // 2, ALTURA // 2 + 50))

    pygame.display.flip()
#loop do jogo
while rodando:
    #limita o fps a 60
    relogio.tick(60)

    #verifica os eventos do sistema
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #verifica se o evento é clique no X
            rodando = False #se clicou no X, muda a variável para False

        #verifica se o evento foi o alarme de inimigo
        if event.type == evento_criar_inimigo:
            #se sim, é criado um novo inimigo
            novo_inimigo = Inimigo(LARGURA, ALTURA)
            #adiciona o novo inimigo na lista
            inimigos.append(novo_inimigo)
    #atualiza a lógica do jogo
    nave.update()

    #faz um clone da lista [:] e atualiza a posição do inimigo na tela
    for inimigo in inimigos[:]:
        inimigo.update()

        #se o inimigo passar da tela
        if inimigo.rect.top > ALTURA:
            #é removido da lista para liberar memoria
            inimigos.remove(inimigo)

    #clonamos a lista de inimigos para iterar de forma segura
    for inimigo in inimigos[:]:
        #verificando colisao inimigo vs nave
        #colliderect retorna true caso haja colisao
        if inimigo.rect.colliderect(nave.rect):
            print("GAME OVER")
            rodando = False

        #verifica colisao laser vs inimigo
        for laser in nave.lasers[:]:
            #retorna true caso haja colisao com o laser
            if laser.rect.colliderect(inimigo.rect):
                #remove o meteoro da lista de inimigos
                if inimigo in inimigos:
                    inimigos.remove(inimigo)
                    #adiciona pontuacao
                    pontuacao += 1
                #removemos tambem o laser que acertou o alvo
                if laser in nave.lasers:
                    nave.lasers.remove(laser)

                #o break interrompe a verificaçao desse laser, ele nao pode acertar dois alvos
                break
    #blit carimba a imagem na tela principal
    tela.blit(fundo_jogo, (0, 0))
    #executa o metodo da classe, mandando ela se desenhar na variavel tela
    nave.desenhar(tela)

    #percorre a lista de inimigos e cada um se desenha na tela
    for inimigo in inimigos:
        inimigo.desenhar(tela)

    #o metodo render() transforma o texto em uma imagem
    #o True ativa o anti-aliasing e white define a cor como branca
    texto_pontos = fonte_padrao.render(f"Pontuação: {pontuacao}", True, "white")
    texto_comandos = fonte_padrao.render("Comandos: [A] [D] Mover | [Barra Espaço] Atirar", True, "white")

    #blit carimba a imagem gerada na cordenada x,y
    tela.blit(texto_pontos, (10, 10))
    tela.blit(texto_comandos, (10, 30))

    #atualiza o display com o processamento de video feito no loop
    pygame.display.flip()

#encerra a biblioteca quando sair do loop
pygame.quit()