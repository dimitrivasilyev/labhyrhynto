import pygame

# pygame setup
pygame.init()
pygame.display.set_caption("O Labhyrhynto")
pygame.display.set_icon(pygame.image.load('favicon.png'))
largura,altura=630,630
screen = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()
running = True
dt = 0
# cor
PRETO=(0,0,0)
BRANCO=(255,255,255)
VERDE=(0,255,0)
VERMELHO=(255,0,0)
# configuração jogador
jogador_tamanho=20
jogador_posicao=[1,1]
jogador_velocidade=5
# labirinto
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# labirinto_largura=largura//jogador_tamanho
# labirinto_altura=altura//jogador_tamanho
# labirinto=[]

# for y in range(labirinto_altura):
#     fileira=[]
#     for x in range(labirinto_largura):
#         fileira.append(1)
#     labirinto.append(fileira)
def criar_jogador():
    pygame.draw.rect(screen, VERDE, (jogador_posicao[0] * 30, jogador_posicao[1] * 30, 30, 30))

def mover_jogador(dx,dy):
    novo_x=jogador_posicao[0]+dx
    novo_y=jogador_posicao[1]+dy
    if labirinto[novo_y][novo_x]:
        jogador_posicao[0]=novo_x
        jogador_posicao[1]=novo_y
    

# def gerar_labirinto():
#     for y in range(labirinto_altura):
#         for x in range(labirinto_largura):
#             if random.random() > 0.3:
#                 labirinto[y][x] = 0
#     labirinto[0][1]=0
#     labirinto[labirinto_altura-1][labirinto_largura-2]=0

# gerar_labirinto()

def gerar_labirinto():
    for y in range(len(labirinto)):
        for x in range(len(labirinto[y])):
            if labirinto[x][y] == 1:
                pygame.draw.rect(screen,PRETO,(x * 30,y * 30, 30, 30))
            else:
                pygame.draw.rect(screen,BRANCO,(x * 30,y * 30, 30, 30))
    pygame.draw.rect(screen,VERMELHO,(1 * 30,1 * 30, 30, 30))
    pygame.draw.rect(screen,VERMELHO,(19 * 30,19 * 30, 30, 30))

def mover_jogador(dx,dy):
    novo_x=jogador_posicao[0]+dx
    novo_y=jogador_posicao[1]+dy
    if labirinto[novo_x][novo_y]==0:
        jogador_posicao[0]=novo_x
        jogador_posicao[1]=novo_y

while running:
    keys = pygame.key.get_pressed()
    clock = pygame.time.Clock()
    # poll for events
    # for y in range(len(labirinto)):
    #     for x in range(len(labirinto[y])):
    #         if labirinto[y][x]==1:
    #             pygame.draw.rect(screen, WHITE, (x * jogador_tamanho, y * jogador_tamanho, jogador_tamanho, jogador_tamanho))
                
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            running = False
        if keys[pygame.K_LEFT] and jogador_posicao[0]>0 or keys[pygame.K_a]:
            mover_jogador(-1,0)
            print("esquerda")
        if keys[pygame.K_RIGHT] and jogador_posicao[0]<len(labirinto[0])-1 or keys[pygame.K_d]:
            mover_jogador(1,0)
            print("direita")
        if keys[pygame.K_UP] and jogador_posicao[1]>0 or keys[pygame.K_w]:
            mover_jogador(0,-1)
            print("cima")
        if keys[pygame.K_DOWN] and jogador_posicao[1]<len(labirinto)-1 or keys[pygame.K_s]:
            mover_jogador(0,1)
            print("baixo")
        
    # RENDER YOUR GAME HERE
    screen.fill(BRANCO)
    gerar_labirinto()
    criar_jogador()
    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.time.Clock().tick(30)
pygame.quit()